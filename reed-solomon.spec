%define name reed-solomon
%define version 3.1.1
%define release %mkrel 5

%define major 3
%define libname %mklibname %name %major
%define libnamedevel %mklibname -d %name

Summary: A Reed-Solomon encoder/decoder library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ka9q.net/code/fec/%{name}-%{version}.tar.gz
Patch0: reed-solomon-destdir.patch
License: GPL
Group: System/Libraries
Url: http://www.ka9q.net/code/fec/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This library implements a general-purpose encoder/decoder for Reed-Solomon
error correcting codes. The decoder supports erasures. The user can specify
the parameters for any size code, limited only by machine resources. Hard-coded
routines for the CCSDS-standard (255,223) code are also included.

%package -n %libname
Summary: A Reed-Solomon encoder/decoder library
Group: System/Libraries
Provides: lib%{name} = %{version}-%{release}

%description -n %libname
This library implements a general-purpose encoder/decoder for Reed-Solomon
error correcting codes. The decoder supports erasures. The user can specify
the parameters for any size code, limited only by machine resources. Hard-coded
routines for the CCSDS-standard (255,223) code are also included.

%package -n %libnamedevel
Summary: A Reed-Solomon encoder/decoder library
Group: System/Libraries
Provides: %{name}-devel
Obsoletes: %mklibname %name
Requires: %libname = %{version}-%{release}

%description -n %libnamedevel
This library implements a general-purpose encoder/decoder for Reed-Solomon
error correcting codes. The decoder supports erasures. The user can specify
the parameters for any size code, limited only by machine resources. Hard-coded
routines for the CCSDS-standard (255,223) code are also included.

%prep
%setup -q
%patch -p0 -b .destdir

%build
export CFLAGS="%{optflags} -fPIC"
%configure 

%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}{%{_libdir},%{_mandir}/man3,%{_includedir}}
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*.h
%{_mandir}/*/*



%changelog
* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1.1-5mdv2009.0
+ Revision: 260206
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1.1-4mdv2009.0
+ Revision: 248333
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Olivier Thauvin <nanardon@mandriva.org> 3.1.1-2mdv2008.1
+ Revision: 101389
- fix devel name

* Mon Oct 22 2007 Olivier Thauvin <nanardon@mandriva.org> 3.1.1-1mdv2008.1
+ Revision: 101065
- initial mdv package
- create reed-solomon

