Summary: A compact getty program for virtual consoles only
Name: mingetty
Version: 1.08
License: GPLv2+
Release: 4.1%{?dist}
Group: System Environment/Base
URL: http://sourceforge.net/projects/mingetty/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch: mingetty-1.00-opt.patch
BuildRoot: %{_tmppath}/%{name}-root

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program in that case).

%prep
%setup -q
%patch -p1

%build
make "RPM_OPTS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,%{_mandir}/man8}

install -m 0755 mingetty $RPM_BUILD_ROOT/sbin/
install -m 0644 mingetty.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/sbin/mingetty
%{_mandir}/man8/mingetty.*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.08-4.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.08-2
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Florian La Roche <laroche@redhat.com> - 1.08-1
- change Source: tag
- Bernardo Innocenti bernie at codewiz.org: add LDFLAGS to opt patch
  to enable cross building on 64bit host
- release 1.08 with loginpause option from Bernardo Innocenti bernie at codewiz.org

* Tue Jan 08 2008 Florian La Roche <laroche@redhat.com> - 1.07-8
- add sf.net project url
- add dist macro to release

* Sun Jan 06 2008 Florian La Roche <laroche@redhat.com> - 1.07-7
- add rpmlint changes to .spec file from Jon Ciesla limb at jcomserv.net

* Tue Aug 21 2007 Florian La Roche <laroche@redhat.com> - 1.07-6
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.07-5.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.07-5.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.07-5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 1.07-5
- build with gcc-4

* Wed Feb 09 2005 Karsten Hopp <karsten@redhat.de> 1.07-4
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jan 03 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.07

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat May 24 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.06

* Sat Apr 12 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.05

* Sun Mar 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.04

* Sat Feb 08 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- small source cleanups

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar 04 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- re-release as 1.00

* Thu Jul 05 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Apr 11 2001 Bill Nottingham <notting@redhat.com>
- rebuild (missing ia64 packages)

* Fri Apr 06 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix man-page bug #34991
- fix syslog() call to be more secure #17349

* Thu Jan 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- set TERM=dumb for s390 console

* Mon Nov 13 2000 Oliver Paukstadt <oliver.paukstadt@millenux.com>
- fgetc returns int not char

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- use %%{_mandir} for man pages

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed build problems on intel and alpha for manhattan

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
~- built against glibc
