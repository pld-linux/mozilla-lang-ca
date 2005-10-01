Summary:	Catalan resources for Mozilla
Summary(ca):	Recursos catalans per a Mozilla
Summary(es):	Recursos catalanes para Mozilla
Summary(pl):	Kataloñskie pliki jêzykowe dla Mozilli
Name:		mozilla-lang-ca
Version:	1.7.12
#define		shortversion	1.712
# use "a", "b", or undefined
#%%define	bver	b
# use "Alpha", "Beta" or %{nil}
%define	fver	%{nil}
Release:	%{?bver:0.%{bver}.}1
License:	GPL
Group:		X11/Applications/Networking
#Source0:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/l10n/lang/moz%{shortversion}/mozilla-%{version}.ca-AD.langpack.xpi
Source0:	http://www.softcatala.org/fitxers/linux/mozilla-%{version}.ca-AD.langpack.xpi
# Source0-md5:	72bb62419f2a7828893ee9a437ef481f
Source1:	%{name}-installed-chrome.txt
Source2:	softcatala-installed-chrome.txt
URL:		http://www.softcatala.org/projectes/mozilla/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:%{version}%{?bver}
Requires(post,postun):	mozilla <= 5:%{version}
Requires(post,postun):	textutils
Requires:	mozilla >= 5:%{version}%{?bver}
Requires:	mozilla <= 5:%{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# %{_libdir}/mozilla/chrome is symlink pointing to the following
%define	_chromedir	%{_datadir}/mozilla/chrome

%description
Catalan resources for Mozilla.

%description -l ca
Recursos catalans per a Mozilla.

%description -l es
Recursos catalanes para Mozilla.

%description -l pl
Kataloñskie pliki jêzykowe dla Mozilli.

%package -n mozilla-theme-softcatala
Summary:	Softcatala theme
Summary(ca):	Tema de Softcatalà
Summary(es):	Tema de Softcatala
Summary(pl):	Motyw Softcatala
Group:		X11/Applications/Networking

%description -n mozilla-theme-softcatala
Classic theme adaptation.

%description -n mozilla-theme-softcatala -l ca
Una adaptació del tema Classic.

%description -n mozilla-theme-softcatala -l es
Una adaptación del tema Classic.

%description -n mozilla-theme-softcatala -l pl
Adaptacia motywu Classic.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_datadir}/mozilla/{searchplugins,defaults/{messenger,profile}}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_datadir}
mv -f $RPM_BUILD_ROOT%{_datadir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_datadir}/searchplugins/* \
	$RPM_BUILD_ROOT%{_datadir}/mozilla/searchplugins
mv -f $RPM_BUILD_ROOT%{_datadir}/defaults/messenger/* \
	$RPM_BUILD_ROOT%{_datadir}/mozilla/defaults/messenger
mv -f $RPM_BUILD_ROOT%{_datadir}/defaults/profile/* \
	$RPM_BUILD_ROOT%{_datadir}/mozilla/defaults/profile

# entries already in mozilla
rm -f $RPM_BUILD_ROOT%{_datadir}/mozilla/searchplugins/{Net,bug,dmoz,google.,jee,lxr,moz}*

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%post -n mozilla-theme-softcatala
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun -n mozilla-theme-softcatala
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/ca-AD.jar
%{_chromedir}/ca-unix.jar
%{_chromedir}/AD.jar
%{_chromedir}/%{name}-installed-chrome.txt
%{_datadir}/mozilla/searchplugins/*
%{_datadir}/mozilla/defaults/messenger/AD
%{_datadir}/mozilla/defaults/profile/AD

%files -n mozilla-theme-softcatala
%defattr(644,root,root,755)
%{_chromedir}/softcatala.jar
%{_chromedir}/softcatala-installed-chrome.txt
