#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-power-tweaks
Version  : 203
Release  : 132
URL      : https://github.com/clearlinux/clr-power-tweaks/archive/203/clr-power-tweaks-203.tar.gz
Source0  : https://github.com/clearlinux/clr-power-tweaks/archive/203/clr-power-tweaks-203.tar.gz
Summary  : Power Tweaks -- adjusts runtime kernel options for optimal power and performance
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-power-tweaks-autostart = %{version}-%{release}
Requires: clr-power-tweaks-bin = %{version}-%{release}
Requires: clr-power-tweaks-license = %{version}-%{release}
Requires: clr-power-tweaks-services = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake-dev
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkgconfig(systemd)

%description
# clr-power-tweaks
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


%package services
Summary: services components for the clr-power-tweaks package.
Group: Systemd services

%description services
services components for the clr-power-tweaks package.


%prep
%setup -q -n clr-power-tweaks-203

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566485658
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1566485658
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-power-tweaks
cp COPYING %{buildroot}/usr/share/package-licenses/clr-power-tweaks/COPYING
%make_install
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s ../clr-power.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/clr-power.timer
mkdir %{buildroot}/usr/lib/systemd/system/sysinit.target.wants
ln -s ../clr-power-rfkill.service %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
/usr/lib/systemd/system/timers.target.wants/clr-power.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/clr_power

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-power-tweaks/COPYING

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sysinit.target.wants/clr-power-rfkill.service
%exclude /usr/lib/systemd/system/timers.target.wants/clr-power.timer
/usr/lib/systemd/system/clr-power-rfkill.service
/usr/lib/systemd/system/clr-power.service
/usr/lib/systemd/system/clr-power.timer
