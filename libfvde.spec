Name: libfvde
Version: 20160918
Release: 1
Summary: Library to access the FileVault Drive Encryption (FVDE) format
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libfvde/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         openssl         zlib
BuildRequires:         openssl-devel        zlib-devel

%description
libfvde is a library to access the FileVault Drive Encryption (FVDE) format

%package devel
Summary: Header files and libraries for developing applications for libfvde
Group: Development/Libraries
Requires: libfvde = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libfvde.

%package tools
Summary: Several tools for accessing FileVault Drive Encryption volumes
Group: Applications/System
Requires: libfvde = %{version}-%{release}  fuse-libs
BuildRequires:  fuse-devel

%description tools
Several tools for accessing the FileVault Drive Encryption volumes

%package python
Summary: Python 2 bindings for libfvde
Group: System Environment/Libraries
Requires: libfvde = %{version}-%{release} python
BuildRequires: python-devel

%description python
Python 2 bindings for libfvde

%package python3
Summary: Python 3 bindings for libfvde
Group: System Environment/Libraries
Requires: libfvde = %{version}-%{release} python3
BuildRequires: python3-devel

%description python3
Python 3 bindings for libfvde

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfvde.pc
%{_includedir}/*
%{_mandir}/man3/*

%files tools
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/fvdeinfo
%attr(755,root,root) %{_bindir}/fvdemount
%attr(755,root,root) %{_bindir}/fvdewipekey
%{_mandir}/man1/*

%files python
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files python3
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%changelog
* Sun Sep 18 2016 Joachim Metz <joachim.metz@gmail.com> 20160918-1
- Auto-generated

