Name:           oneVPL-intel-gpu
Version:        23.1.5
Release:        1%{?dist}
Summary:        Intel oneVPL GPU Runtime
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/oneapi-src/%{name}/archive/refs/tags/intel-onevpl-%{version}.tar.gz
Patch0:         %{name}-fix-build.patch

# Every other component has the 2022.x.x format:
Requires:       oneVPL%{?_isa}

BuildRequires:  cmake3
BuildRequires:  devtoolset-9-gcc-c++
BuildRequires:  oneVPL-devel
BuildRequires:  pkgconfig(libdrm) >= 2.4
# Should be 1.9 but fails with libva < 2.12 (VAProcFilterCap3DLUT):
# https://github.com/oneapi-src/oneVPL-intel-gpu/issues/198
BuildRequires:  pkgconfig(libva) >= 1.12

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
%autosetup -p1 -n %{name}-intel-onevpl-%{version}

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

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_docdir}

%{?ldconfig_scriptlets}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.2
%{_libdir}/libmfx-gen.so.1.2.8
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
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
