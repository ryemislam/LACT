Name:           lact-headless
Version:        0.5.6
Release:        1
Summary:        AMDGPU control utility
License:        MIT
URL:            https://github.com/ilya-zlobintsev/LACT
Source0:        https://github.com/ilya-zlobintsev/LACT/archive/refs/tags/v0.5.6.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  rust cargo gcc libdrm-devel dbus curl make clang git
Requires:       libdrm hwdata

%description
AMDGPU control utility

%prep
%setup -q -n LACT-%{version}

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install PREFIX=/usr DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
/usr/bin/lact-headless
/usr/lib/systemd/system/lact-headlessd.service
/usr/share/applications/io.github.lact-headless-linux.desktop
/usr/share/icons/hicolor/scalable/apps/io.github.lact-headless-linux.svg
/usr/share/pixmaps/io.github.lact-headless-linux.png

%changelog
* Thu Nov 14 2024 - ilya-zlobintsev -  - 
- Autogenerated from CI, please see  for detailed changelog.
