Summary:	libirman - accessing IRMAN hardware
Summary(pl.UTF-8):   libirman - dostęp do urządzeń IRMAN
Name:		libirman
Version:	0.4.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://lirc.sourceforge.net/software/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	b28e9ab2fd9b1506201f5f84e10a8aa6
URL:		http://www.lirc.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libirman is a library for accessing the IRMAN hardware from Linux.

%description -l pl.UTF-8
Biblioteka libirman umożliwia dostęp do urządzenia IRMAN w Linuksie.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_sysconfdir},%{_includedir}}

install workmanir $RPM_BUILD_ROOT%{_bindir}
install libirman.a $RPM_BUILD_ROOT%{_libdir}
install irman.conf $RPM_BUILD_ROOT%{_sysconfdir}
install irman.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.a
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_includedir}/*.h
