#
# spec file for package libmysofa
#
# Copyright (c) 2021 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%global commit0 8423749934bfc09121261694b1ccfba7e6d5c955
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libmysofa
Version:        1.2.1
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
mkdir -p build
%cmake -B build \
  -DBUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_COLOR_MAKEFILE=ON -DCODE_COVERAGE=OFF -Wno-dev ..

%make_build -C build

%install
%make_install -C build
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

* Fri Oct 22 2021 David Va <davidva at tuta dot io> 1.2.1-1.git8423749
- Updated to 1.2.1-1.git8423749

* Tue Jan 26 2021 David Va <davidva at tuta dot io> 1.2-2.git8dda834
- Updated to 1.2-2.git8dda834

* Sat Jul 11 2020 David Va <davidva at tuta dot io> 1.1-2.gitcc9831f
- Fix https://github.com/UnitedRPMs/issues/issues/55

* Tue Jun 23 2020 David Va <davidva at tuta dot io> 1.1-1.gitcc9831f
- Updated to 1.1-1.gitcc9831f

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
