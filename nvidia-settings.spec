Name:           nvidia-settings
Version:        375.26
Release:        1%{?dist}
Summary:        Configure the NVIDIA graphics driver

License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
Source0:        ftp://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.bz2
Patch0:         nvidia-settings-desktop.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  jansson-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXv-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  m4
BuildRequires:  mesa-libGL-devel

Requires:       libvdpau%{?_isa}


%description
NVIDIA's tool for dynamic configuration while the X server is running.


%prep
%setup -q
%patch0 -p1

find . -name "utils.mk" -exec sed -i \
    -e 's|LIBDIR = $(DESTDIR)$(PREFIX)/lib|LIBDIR = $(DESTDIR)$(PREFIX)/%{_lib}|g' \
    {} \;


%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} \
    NV_USE_BUNDLED_LIBJANSSON=0 \
    NV_VERBOSE=1 \
    STRIP_CMD="/bin/true" \
    X_LDFLAGS="-L%{_libdir}"


%install
rm -rf %{buildroot}
%make_install INSTALL="install -p" NV_USE_BUNDLED_LIBJANSSON=0 PREFIX=%{_prefix}

install -d %{buildroot}%{_datadir}/{applications,pixmaps}
install -p -m 0644 doc/%{name}.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir %{buildroot}%{_datadir}/applications/ doc/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc COPYING doc/FRAMELOCK.txt doc/NV-CONTROL-API.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/libnvidia-gtk*.so.%{version}
%{_mandir}/man1/%{name}.*


%changelog
* Fri Feb 17 2017 Jajauma's Packages <jajauma@yandex.ru> - 375.26-1
- Update to latest upstream release

* Sun Nov 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 375.20-1
- Update to latest upstream version

* Thu Oct 20 2016 Jajauma's Packages <jajauma@yandex.ru> - 367.57-1
- Update to latest upstream version

* Sun Oct 09 2016 Jajauma's Packages <jajauma@yandex.ru> - 367.44-2
- Public release
