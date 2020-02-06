%global commit0 c987d49b0925b64eccf0611b2fa6242e12d2c2d3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libmysofa
Version:        1.0
Release:    	1%{?gver}%{dist}
Summary:        C library to read HRTFs if they are stored in the AES69-2015 SOFA format

Group:          System Environment/Libraries
License:        BSD
URL:            https://hoene.github.io/libmysofa/
Source:         https://github.com/hoene/libmysofa/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	cmake 
BuildRequires:	zlib-devel
BuildRequires:  gcc-c++
Requires:	%{name}-libs = %{version}-%{release}

%description
C library to read HRTFs if they are stored in the AES69-2015 SOFA format.

%package libs
Summary: libmysofa library
Group: Development/Libraries

%description libs
libmysofa library for ffmpeg.
This package contains the shared library file.

%package devel
Summary: libmysofa development
Group: Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description devel
libmysofa library for ffmpeg.
This package contains the development files.

%prep
%autosetup -n %{name}-%{commit0}

sed -i 's|/lib|/%{_lib}/pkgconfig|g' libmysofa.pc.cmake
sed -i 's|lib/pkgconfig|%{_lib}/pkgconfig|g' CMakeLists.txt

%build
%cmake -DBUILD_TESTS:BOOL='OFF' \
 -DCMAKE_BUILD_TYPE:STRING='Release' \
 -DCMAKE_COLOR_MAKEFILE:BOOL='ON' \
 -Wno-dev .

make

%install
%make_install
rm -f %{buildroot}/%{_libdir}/libmysofa.a 
rm -f %{buildroot}/usr/lib/libmysofa.a

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_datadir}/%{name}/MIT_KEMAR_normal_pinna.sofa
%{_datadir}/%{name}/default.sofa

%files libs
%{_libdir}/libmysofa.so
%{_libdir}/libmysofa.so.*

%files devel
%{_includedir}/mysofa.h
%{_libdir}/pkgconfig/libmysofa.pc

%changelog

* Wed Feb 05 2020 David Va <davidva at tuta dot io> 1.0-1.gitc987d49
- Updated to 1.0-1.gitc987d49

* Mon Dec 09 2019 David Vasquez <davidva at tutanota dot com> 0.9.1-1.gitbe7ac15
- Updated to 0.9.1-1.gitbe7ac15

* Fri Nov 29 2019 David Vasquez <davidva at tutanota dot com> 0.9-1.gitf8762e9
- Updated to 0.9-1.gitf8762e9

* Sat Sep 14 2019 David Vasquez <davidva at tutanota dot com> 0.8-1.gite07edb3
- Updated to 0.8-1.gite07edb3

* Sat Apr 06 2019 David Vasquez <davidva at tutanota dot com> 0.7-1.git2ed84bb
- Updated to 0.7-1.git2ed84bb

* Wed Oct 25 2017 David Vasquez <davidva at tutanota dot com> 0.6-1.git49aa1c7
- Initial build rpm
