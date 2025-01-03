#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : clr-power-tweaks
Version  : 236
Release  : 169
URL      : https://github.com/clearlinux/clr-power-tweaks/archive/refs/tags/236.tar.gz
Source0  : https://github.com/clearlinux/clr-power-tweaks/archive/refs/tags/236.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-power-tweaks-autostart = %{version}-%{release}
Requires: clr-power-tweaks-bin = %{version}-%{release}
Requires: clr-power-tweaks-license = %{version}-%{release}
Requires: clr-power-tweaks-man = %{version}-%{release}
Requires: clr-power-tweaks-services = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake-dev
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkgconfig(systemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## clr-power-tweaks
This is a utility, authored for the purposes of Clear Linux, that sets
reasonable power management defaults for platform devices. This is to improve
energy efficiency while platform is idle.

%package autostart
Summary: autostart components for the clr-power-tweaks package.
Group: Default

%description autostart
autostart components for the clr-power-tweaks package.


%package bin
Summary: bin components for the clr-power-tweaks package.
Group: Binaries
Requires: clr-power-tweaks-license = %{version}-%{release}
Requires: clr-power-tweaks-services = %{version}-%{release}

%description bin
bin components for the clr-power-tweaks package.


%package license
Summary: license components for the clr-power-tweaks package.
Group: Default

%description license
license components for the clr-power-tweaks package.


%package man
Summary: man components for the clr-power-tweaks package.
Group: Default

%description man
man components for the clr-power-tweaks package.


%package services
Summary: services components for the clr-power-tweaks package.
Group: Systemd services
Requires: systemd

%description services
services components for the clr-power-tweaks package.


%prep
%setup -q -n clr-power-tweaks-236
cd %{_builddir}/clr-power-tweaks-236
pushd ..
cp -a clr-power-tweaks-236 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735920351
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735920351
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-power-tweaks
cp %{_builddir}/clr-power-tweaks-%{version}/COPYING %{buildroot}/usr/share/package-licenses/clr-power-tweaks/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s ../clr-power.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/clr-power.timer
mkdir %{buildroot}/usr/lib/systemd/system/sysinit.target.wants
ln -s ../clr-power-rfkill.service %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
/usr/lib/systemd/system/timers.target.wants/clr-power.timer

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/clr_power
/usr/bin/clr_power

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-power-tweaks/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clr_power.1
/usr/share/man/man5/clr-power-tweaks.conf.5

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
%exclude /usr/lib/systemd/system/timers.target.wants/clr-power.timer
/usr/lib/systemd/system/clr-power-rfkill.service
/usr/lib/systemd/system/clr-power.service
/usr/lib/systemd/system/clr-power.timer
