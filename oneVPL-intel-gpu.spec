%global mfx_ver_major 2
%global mfx_ver_minor 10

Name:           oneVPL-intel-gpu
Version:        24.2.0
Release:        1%{?dist}
Summary:        Intel oneVPL GPU Runtime
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/oneapi-src/%{name}/archive/intel-onevpl-%{version}/intel-onevpl-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  devtoolset-9-gcc-c++
BuildRequires:  libvpl-devel
BuildRequires:  pkgconfig(libdrm) >= 2.4
# Should be >= 1.9 but fails with libva < 2.12 (VAProcFilterCap3DLUT):
# https://github.com/oneapi-src/oneVPL-intel-gpu/issues/198
BuildRequires:  pkgconfig(libva) >= 1.12

Requires:       libvpl%{?_isa} >= 1:2.10.1

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel Gen
GPUs. Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n vpl-gpu-rt-intel-onevpl-%{version}

%build
mkdir build
pushd build

export VPL_BUILD_DEPENDENCIES="%{_prefix}"
. /opt/rh/devtoolset-9/enable
%cmake3 \
    -DBUILD_TESTS:BOOL='OFF' \
    -DCMAKE_BUILD_TYPE:STRING="Fedora" \
    ..
%cmake3_build

popd

%install
pushd build
%cmake3_install
popd

%{?ldconfig_scriptlets}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}.%{mfx_ver_minor}
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
* Mon Apr 15 2024 Simone Caronni <negativo17@gmail.com> - 24.2.0-1
- Update to 24.2.0.

* Wed Mar 20 2024 Simone Caronni <negativo17@gmail.com> - 24.1.5-1
- Update to 24.1.5.

* Tue Feb 20 2024 Simone Caronni <negativo17@gmail.com> - 24.1.3-2
- Import changes from Fedora.

* Mon Feb 19 2024 Simone Caronni <negativo17@gmail.com> - 24.1.3-1
- Update to 24.1.3.

* Thu Jan 25 2024 Simone Caronni <negativo17@gmail.com> - 24.1.1-1
- Update to 24.1.1.

* Thu Dec 14 2023 Simone Caronni <negativo17@gmail.com> - 23.4.3-1
- Update to 23.4.3.

* Thu Nov 02 2023 Simone Caronni <negativo17@gmail.com> - 23.4.0-1
- Update to 23.4.0.

* Tue Oct 03 2023 Simone Caronni <negativo17@gmail.com> - 23.3.4-1
- Update to 23.3.4.

* Tue Aug 08 2023 Simone Caronni <negativo17@gmail.com> - 23.3.1-1
- Update to 23.3.1.

* Fri Jul 14 2023 Simone Caronni <negativo17@gmail.com> - 23.3.0-1
- Update to 23.3.0.

* Tue May 23 2023 Simone Caronni <negativo17@gmail.com> - 23.2.2-1
- Update to 23.2.2.

* Wed Apr 19 2023 Simone Caronni <negativo17@gmail.com> - 23.2.0-1
- Update to 23.2.0.

* Thu Apr 13 2023 Simone Caronni <negativo17@gmail.com> - 23.1.5-1
- Update to 23.1.5.

* Sat Mar 11 2023 Simone Caronni <negativo17@gmail.com> - 23.1.3-1
- Update to 23.1.3.

* Fri Feb 24 2023 Simone Caronni <negativo17@gmail.com> - 23.1.2-1
- Update to 23.1.2.

* Mon Jan 30 2023 Simone Caronni <negativo17@gmail.com> - 23.1.0-1
- Update to 23.1.0.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 22.6.4-1
- Update to 22.6.4.

* Fri Nov 18 2022 Simone Caronni <negativo17@gmail.com> - 22.6.3-1
- Update to 22.6.3.

* Mon Oct 24 2022 Simone Caronni <negativo17@gmail.com> - 22.6.0-1
- Update to 22.6.0.

* Tue Oct 04 2022 Simone Caronni <negativo17@gmail.com> - 22.5.4-1
- Update to 22.5.4.

* Wed Aug 24 2022 Simone Caronni <negativo17@gmail.com> - 22.5.3-1
- Update to 22.5.3.

* Wed Aug 17 2022 Simone Caronni <negativo17@gmail.com> - 22.5.2-1
- Update to 22.5.2.

* Tue Aug 09 2022 Simone Caronni <negativo17@gmail.com> - 22.5.1-1
- Update to 22.5.1.

* Thu Jul 21 2022 Simone Caronni <negativo17@gmail.com> - 22.5.0-1
- Update to 22.5.0.

* Mon Jul 04 2022 Simone Caronni <negativo17@gmail.com> - 22.4.4-1
- Update to 22.4.4.

* Thu Jun 09 2022 Simone Caronni <negativo17@gmail.com> - 22.4.3-1
- Update to 22.4.3.

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 22.4.2-1
- Update to 22.4.2.

* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 22.4.0-1
- Update to 22.4.0.

* Sun Apr 03 2022 Simone Caronni <negativo17@gmail.com> - 22.3.2-1
- Update to 22.3.2.

* Wed Mar 30 2022 Simone Caronni <negativo17@gmail.com> - 22.3.1-2
- Adjust libva requirement.

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 22.3.1-1
- Update to 22.3.1.

* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 22.2.2-1
- Update to 22.2.2.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 22.2.1-1
- Update to 22.2.1.

* Tue Feb 08 2022 Simone Caronni <negativo17@gmail.com> - 22.2.0-1
- First build.
