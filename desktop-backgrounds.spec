Summary: Desktop backgrounds.
Name: desktop-backgrounds
Version: 2.0
Release: 9
License: LGPL
Group: Applications/Multimedia
Source: redhat-backgrounds.tar.gz
Source2: Propaganda-1.0.0.tar.gz
Source3: README.Propaganda
## Source4: beta-placeholder.png
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArchitectures: noarch

%description
The desktop-backgrounds package contains artwork intended 
to be used as desktop wallpaper.

%package basic

Summary: Desktop background base set.
Group: Applications/Multimedia

Provides: desktop-backgrounds
Obsoletes: desktop-backgrounds

%description basic
The desktop-backgrounds-basic package contains a good basic set of 
images to use for your desktop background.

%package extra

Summary: Desktop background images.
Group: Applications/Multimedia

%description extra
The desktop-backgrounds-extra package contains a larger set of images
to use for your desktop background. It builds on
desktop-backgrounds-basic.

%prep
%setup -n redhat-backgrounds

# move things where %doc can find them
cp %{SOURCE3} .
mv images/space/*.ps .
mv images/space/README* .

# add propaganda
(cd tiles && tar zxf %{SOURCE2})

## put in placeholder for the beta
## cp -f %{SOURCE4} images/default.png

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/backgrounds
cd $RPM_BUILD_ROOT%{_prefix}/share/backgrounds

cp -a $RPM_BUILD_DIR/redhat-backgrounds/images .
cp -a $RPM_BUILD_DIR/redhat-backgrounds/tiles .

%clean
rm -rf $RPM_BUILD_ROOT

# basic contains some reasonable sane basic tiles
%files basic
%defattr(-, root, root)
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/tiles
%dir %{_datadir}/backgrounds/images
%{_datadir}/backgrounds/tiles/*.png
%{_datadir}/backgrounds/tiles/*jpg
%{_datadir}/backgrounds/images/default.png

# extra contains big images, plus Propaganda tiles
%files extra
%defattr(-, root, root)
%doc README.space PHOTO_FAQ.ps README.Propaganda
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/images
%dir %{_datadir}/backgrounds/tiles
%{_datadir}/backgrounds/tiles/Propaganda
%{_datadir}/backgrounds/images/*
## we'll see if rpm likes this
%exclude %{_datadir}/backgrounds/images/default.png

%changelog
* Tue Aug 27 2002 Than Ngo <than@redhat.com> 2.0-9
- add missing kdebase desktop backgrounds (bug #72508)

* Wed Aug 21 2002 Havoc Pennington <hp@redhat.com>
- drop the beta placeholder in favor of final background

* Tue Aug 13 2002 Havoc Pennington <hp@redhat.com>
- new redhat-backgrounds with wallpapers moved to tiles
- overwrite default.png with a placeholder

* Fri Aug  9 2002 Havoc Pennington <hp@redhat.com>
- new redhat-backgrounds with default.png

* Mon Jul 22 2002 Havoc Pennington <hp@redhat.com>
- new redhat-backgrounds from CVS with default.jpg

* Tue Jul 16 2002 Havoc Pennington <hp@redhat.com>
- new images from Garrett added to -extra

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- redo it, now it includes the tile/image collection
  redhat-backgrounds from CVS, plus propaganda
- move things to datadir/share/backgrounds/images 
  and datadir/share/backgrounds/wallpapers
- split into a small basic package and an extra package, 
  so we can have packages require the basic package
  without sucking in huge images
- move space images into devserv CVS
- move nautilus and kdebase tiles into devserv CVS

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

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
