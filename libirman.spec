Summary:	libirman
Summary(pl):	libirman
Name:		libirman
Version:	0.4.2
Release:	0
License:	GPL
Group:		Libraries
Source0:	http://www.lirc.org/software/snapshots/%{name}-%{version}.tar.gz
URL:		http://www.lirc.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libirman is a library for accessing the IRMAN hardware from Linux.

%description -l pl
Biblioteka libirman umo¿liwia dostêp do urz±dzenia IRMAN w Linuksie

%prep
%setup -q

%build
aclocal
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
%attr(755,root,root) %{_bindir}
%attr(755,root,root) %{_libdir}
%{_sysconfdir}
%{_includedir}
