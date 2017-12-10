#
# Conditional build:
%bcond_with	lirc	# LIRC driver (for LIRC > 0.9.3)

Summary:	libirman - accessing IRMAN hardware
Summary(pl.UTF-8):	libirman - dostęp do urządzeń IRMAN
Name:		libirman
Version:	0.5.2
Release:	1
License:	LGPL v2 (library), GPL v2 (utility)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libirman/%{name}-%{version}.tar.gz
# Source0-md5:	1f1175995e527c41871077d278aa7448
Patch0:		%{name}-pc.patch
URL:		https://libirman.sourceforge.io/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
# lirc-driver
%{?with_lirc:BuildRequires:	lirc-devel >= 0.9.4}
BuildRequires:	pkgconfig
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

%package -n lirc-plugin-irman
Summary:	IRMAN plugin for LIRC
Summary(pl.UTF-8):	Wtyczka IRMAN dla LIRC-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lirc > 0.9.3

%description -n lirc-plugin-irman
IRMAN plugin for LIRC.

The irman driver is originally developed for the irman devices, see
<http://www.intolect.com/irmandetail.htm>. These are nowadays
discontinued. However, some modern hardware (notably the irtoy) is
able to emulate the irman protocol.

%description -n lirc-plugin-irman -l pl.UTF-8
Wtyczka IRMAN dla LIRC-a.

Sterownik irman pierwotnie powstał dla urządzeń irman (szczegóły na
stronie <http://www.intolect.com/irmandetail.htm>). Urządzenia te nie
są już produkowane, jednak niektóre nowsze urządzenia (np. irtoy)
potrafią emulować protokół irman.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-plugin%{!?with_lirc:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/test_{func,io,name}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libirman.la
%if %{with lirc}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lirc/plugins/irman.la
%endif

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
%{_includedir}/irman.h
%{_pkgconfigdir}/libirman.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libirman.a

%if %{with lirc}
%files -n lirc-plugin-irman
%defattr(644,root,root,755)
%doc lirc-plugin/irman.html
%attr(755,root,root) %{_libdir}/lirc/plugins/irman.so
%{_datadir}/lirc/configs/irman.conf
%endif
