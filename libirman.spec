Summary:	libirman - accessing IRMAN hardware
Summary(pl.UTF-8):	libirman - dostęp do urządzeń IRMAN
Name:		libirman
Version:	0.4.5
Release:	2
License:	LGPL v2 (library), GPL v2 (utility)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lirc/%{name}-%{version}.tar.bz2
# Source0-md5:	4a2708d53b6c79659c073cfefed57f78
URL:		http://www.lirc.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libirman is a library for accessing the IRMAN hardware from Linux.

%description -l pl.UTF-8
Biblioteka libirman umożliwia dostęp do urządzenia IRMAN w Linuksie.

%package devel
Summary:	Header file for libirman library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libirman
License:	LGPL v2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libirman library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libirman.

%package static
Summary:	Static libirman library
Summary(pl.UTF-8):	Statyczna biblioteka libirman
License:	LGPL v2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libirman library.

%description static -l pl.UTF-8
Statyczna biblioteka libirman.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README TECHNICAL TODO
%attr(755,root,root) %{_bindir}/workmanir
%attr(755,root,root) %{_libdir}/libirman.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libirman.so.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/irman.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libirman.so
%{_libdir}/libirman.la
%{_includedir}/irman.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libirman.a
