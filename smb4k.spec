Name:		smb4k
Version:	0.10.7
Release:	1%{?dist}
Summary:	The SMB/CIFS Share Browser for KDE

Group:		Applications/Internet
License:	GPLv2+
URL:		http://smb4k.berlios.de/
Source0:	http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
Patch0:		smb4k-0.10.4-sudo.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake >= 2.6.0
BuildRequires:	kdelibs-devel >= 4.1.0
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
Requires:	samba-client
Requires:	%{_bindir}/kdesu

%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the libraries, include files and other resources
needed to develop applications using %{name}.

%prep
%setup -q
# Fix pt translation
pushd po/pt/
mv -f pt.po smb4k.po
popd
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications/kde4 \
	--add-category Network \
	--add-category FileTransfer \
	--add-category FileManager \
	%{buildroot}%{_datadir}/applications/kde4/smb4k.desktop

# Make symlink relative
pushd $RPM_BUILD_ROOT%{_docdir}/HTML/en/smb4k/
ln -sf ../common
popd

%find_lang %{name} --with-kde

%post
/sbin/ldconfig

xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-icon-resource forceupdate --theme oxygen 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :

%postun
/sbin/ldconfig

xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-icon-resource forceupdate --theme oxygen 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog COPYING FAQ README TODO
%{_kde4_bindir}/*
%{_kde4_libdir}/kde4/libsmb4k*.*
%{_kde4_libdir}/libsmb4k*.so.*
%{_kde4_libdir}/libsmb4kdialogs.so
%{_kde4_datadir}/applications/kde4/smb4k.desktop
%{_kde4_datadir}/config.kcfg/smb4k.kcfg
%{_kde4_iconsdir}/hicolor/*/apps/smb4k.png
%{_kde4_iconsdir}/oxygen/*/apps/smb4k.png
%{_kde4_datadir}/kde4/apps/kconf_update/*
%{_kde4_datadir}/kde4/apps/smb4k/

%files devel
%defattr(-,root,root,-)
# %{_kde4_includedir}/smb4k*.h
%{_libdir}/libsmb4kc*.so

%changelog
* Mon Jun 21 2010 Marcin Garski <mgarski[AT]post.pl> 0.10.7-1
- Update to 0.10.7 (fix #574904)

* Sat Oct 24 2009 Marcin Garski <mgarski[AT]post.pl> 0.10.4-1
- Update to 0.10.4
- Proper update of sudoers (#527401)
- Add kdesu to Requires (#499720)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Marcin Garski <mgarski[AT]post.pl> 0.10.2-1
- Update to 0.10.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Marcin Garski <mgarski[AT]post.pl> 0.10.1-1
- Update to 0.10.1

* Thu Sep 04 2008 Marcin Garski <mgarski[AT]post.pl> 0.10.0-2
- Update to 0.10.0

* Wed Jul 30 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.6-1
- Update to 0.9.6

* Mon Jun 02 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.5-1
- Update to 0.9.5

* Tue Apr 29 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.4-1
- Update to 0.9.4

* Sat Mar 01 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.3-2
- Include .la files (bug #435149)

* Tue Feb 26 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.3-1
- Update to 0.9.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.2-4
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Marcin Garski <mgarski[AT]post.pl> 0.9.2-3
- Update to 0.9.2
- Don't compile Konqueror plugin

* Sat Dec 08 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.7-3
- Fix BR's to compile on rawhide

* Sun Dec 02 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.7-2
- Add qt-devel to BR

* Sun Dec 02 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.7-1
- Update to 0.8.7

* Sun Nov 11 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.6-1
- Update to 0.8.6

* Thu Sep 27 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.5-1
- Update to 0.8.5

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.4-2
- Fix license tag

* Fri Aug 03 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.4-1
- Update to 0.8.4
- Preserve upstream .desktop vendor

* Thu May 03 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.3-1
- Updated to version 0.8.3

* Tue May 01 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.2-1
- Updated to version 0.8.2
- Spec file cleanup

* Tue Apr 10 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.1-1
- Updated to version 0.8.1

* Mon Jan 01 2007 Marcin Garski <mgarski[AT]post.pl> 0.8.0-1
- Updated to version 0.8.0

* Tue Nov 28 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.5-1
- Updated to version 0.7.5

* Tue Nov 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.4-1
- Updated to version 0.7.4

* Wed Sep 27 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.3-1
- Updated to version 0.7.3

* Fri Sep 01 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.2-2
- Rebuild for Fedora Core 6
- Spec tweak

* Fri Aug 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.2-1
- Updated to version 0.7.2

* Mon Jun 19 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.1-1
- Updated to version 0.7.1
- Drop smb4k-0.6.5-desktop.patch (merged upstream)

* Tue Apr 25 2006 Marcin Garski <mgarski[AT]post.pl> 0.7.0-1
- Updated to version 0.7.0, comment --enable-final

* Tue Apr 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.10-1
- Updated to version 0.6.10

* Fri Mar 24 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.9-1
- Updated to version 0.6.9

* Fri Feb 24 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.8-1
- Updated to version 0.6.8

* Fri Feb 17 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-4
- Updated smb4k-0.6.8-mount.patch

* Fri Feb 17 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-3
- Add support of mount.cifs/umount.cifs (bug #181638)
- Remove smb4k-0.6.5-buff.patch

* Tue Feb 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-2
- Rebuild

* Wed Feb 08 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.7-1
- Updated to version 0.6.7

* Wed Feb 01 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-5
- Fix GCC warnings
- Don't own KDE directories

* Wed Jan 18 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-4
- Remove libxml2 from BR
- Add workaround for broken libtool archive (made by Dawid Gajownik)

* Sun Jan 15 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-3
- Get rid of desktop-file-utils
- Add --disable-dependency-tracking & --enable-final

* Thu Jan 12 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-2
- Add kdebase-devel to BuildRequires

* Wed Jan 11 2006 Marcin Garski <mgarski[AT]post.pl> 0.6.5-1
- Updated to version 0.6.5 && spec cleanup for FE

* Sun Sep 05 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.1a-1.fc2
- Updated to version 0.4.1a

* Thu Aug 31 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.1-1.fc2
- Updated to version 0.4.1

* Wed Jun 02 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.0-3.fc2
- Rebuild for Fedora Core 2

* Thu May 06 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.0-2
- Convert pl.po to UTF-8

* Thu May 06 2004 Marcin Garski <mgarski[AT]post.pl> 0.4.0-1
- Update to 0.4.0

* Wed Jan 21 2004 Marcin Garski <mgarski[AT]post.pl> 0.3.2-1
- Rebuild for Fedora Core 1

* Thu Dec 18 2003 Marcin Garski <mgarski[AT]post.pl> 0.3.1-3
- Cleanup specfile

* Fri Nov 27 2003 Marcin Garski <mgarski[AT]post.pl> 0.3.1-2
- Initial specfile based on specfile by Ian Geiser <geiseri[AT]msoe.edu>
