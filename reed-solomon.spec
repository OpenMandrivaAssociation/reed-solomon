%define major 3
%define libname %mklibname %name %major
%define libnamedevel %mklibname -d %name

%define debug_package %{nil}

Summary: A Reed-Solomon encoder/decoder library
Name:    reed-solomon
Version: 3.1.1
Release: 7
Source0: http://www.ka9q.net/code/fec/%{name}-%{version}.tar.gz
Patch0:  reed-solomon-destdir.patch
License: GPL
Group:   System/Libraries
Url:     https://www.ka9q.net/code/fec/

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
mkdir -p %{buildroot}{%{_libdir},%{_mandir}/man3,%{_includedir}}
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*.h
%{_mandir}/*/*
