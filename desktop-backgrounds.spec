Summary: Desktop background images.
Name: desktop-backgrounds
Version: 1.1
Release: 4
Copyright: LGPL
Group: Applications/Multimedia
Source: space-1.0.0.tar.gz
Source1: gnome-tiles-1.0.0.tar.gz
Source2: Propaganda-1.0.0.tar.gz
Source3: README.Propaganda
Source4: README.space
Source5: PHOTO_FAQ.ps
BuildRoot: %{_tmppath}/%{name}-%{PACKAGE_VERSION}-root
Obsoletes: gnome-imglib
BuildArchitectures: noarch

%description
The desktop-backgrounds package contains a bunch of images for
sprucing up your desktop.

Install this package if you would like a variety of images for use as a
desktop background.

%prep
%setup -c desktop-backgrounds-%{version} -T -D

cp %{SOURCE3} $RPM_BUILD_DIR/desktop-backgrounds-%{version}
cp %{SOURCE4} $RPM_BUILD_DIR/desktop-backgrounds-%{version}
cp %{SOURCE5} $RPM_BUILD_DIR/desktop-backgrounds-%{version}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/pixmaps/backgrounds
cd $RPM_BUILD_ROOT%{_prefix}/share/pixmaps/backgrounds
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Dave Mason <dcm@redhat.com>
- updated spec file to RPM guidelines

* Thu Jun 29 2000 Than Ngo <than@redhat.de>
- FHS fixes

* Tue Feb 01 2000 Preston Brown <pbrown@redhat.com>
- new space backgrounds

* Fri Apr  2 1999 Jonathan Blandford <jrb@redhat.com>
- added propaganda tiles.  Spruced it up a bit
- moved README files out of tarball, and into docs dir.

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- First attempt

%files
%defattr(-, root, root)
%doc README.space README.Propaganda PHOTO_FAQ.ps
%{_prefix}/share/pixmaps/backgrounds/space
%{_prefix}/share/pixmaps/backgrounds/tiles
%{_prefix}/share/pixmaps/backgrounds/Propaganda
