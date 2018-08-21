%global commit0 49aa1c7f3013d399258d29886a250831b99ed8c8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libmysofa
Version:        0.6
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

sed -i 's|LIBRARY DESTINATION lib|LIBRARY DESTINATION lib64|g' src/CMakeLists.txt

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
%{_libdir}/libmysofa.so.0
%{_libdir}/libmysofa.so.0.5.1

%files devel
%{_includedir}/mysofa.h

%changelog

* Wed Oct 25 2017 David Vasquez <davidva at tutanota dot com> 0.6-1.git49aa1c7
- Initial build rpm
