Name:           facter
Version:        3.1.4
Release:        1%{?dist}
Summary:        Command and ruby library for gathering system information

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://puppetlabs.com/%{name}
Source0:        https://downloads.puppetlabs.com/%{name}/%{name}-%{version}.tar.gz
Source1:        https://downloads.puppetlabs.com/%{name}/%{name}-%{version}.tar.gz.asc
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  boost-devel
BuildRequires:  openssl-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  libblkid-devel
BuildRequires:  libcurl-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  wget
BuildRequires:  tar
BuildRequires:  cmake

%description
Facter is a lightweight program that gathers basic node information about the
hardware and operating system. Facter is especially useful for retrieving
things like operating system names, hardware characteristics, IP addresses, MAC
addresses, and SSH keys.

Facter is extensible and allows gathering of node information that may be
custom or site specific. It is easy to extend by including your own custom
facts. Facter can also be used to create conditional expressions in Puppet that
key off the values returned by facts.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}



%install
make install DESTDIR=%{buildroot}

%postun
# Work around issues where puppet fails to run after a facter update
# https://bugzilla.redhat.com/806370
# http://projects.puppetlabs.com/issues/12879
if [ "$1" -ge 1 ]; then
  /sbin/service puppet condrestart >/dev/null 2>&1 || :
fi


%clean
rm -rf %{buildroot}


%check
ctest -V %{?_smp_mflags}

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%{facter_libdir}/%{name}*
%{_mandir}/man8/%{name}*


%changelog
* Fri Feb 02 2016 Julien Pivotto <roidelapluie@inuits.eu> - 3.1.4-1
- Update to 3.1.4

* Fri Feb 02 2016 Julien Pivotto <roidelapluie@inuits.eu> - 2.4.6-1
- Update to 2.4.6

* Fri Feb 02 2016 Julien Pivotto <roidelapluie@inuits.eu> - 2.4.4-3
- Fix el7 build

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
- Update to 2.4.4

* Thu Apr 2 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-1
- Update to 2.4.3

* Fri Feb 13 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.1-1
- Update to 2.4.1

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Tue Jan 06 2015 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-1
- Update to 2.3.0

* Fri Oct 10 2014 Michael Stahnke <stahnma@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 as per bz#1108041

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.0.1-2
- Fix el7 conditionals as suggested by Orion Poplawski (BZ #1087946)

* Tue Apr 29 2014 Sam Kottler <skottler@fedoraproject.org> - 2.0.1-1
- Update to to 2.0.1

* Tue Jan 28 2014 Todd Zullinger <tmz@pobox.com> - 1.7.4-1
- Update to 1.7.4
- Create /etc/facter/facts.d for external facts
- Send dmiddecode errors to /dev/null in the virtual fact (FACT-86)

* Tue Oct 8 2013 Sam Kottler <skottler@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3 (BZ #1016817)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Sam Kottler <skottler@fedoraproject.org> 1.6.18-4
- Apply upstream patch to ensure the first non-127.0.0.1 interface

* Wed Apr 03 2013 Todd Zullinger <tmz@pobox.com> - 1.6.18-3
- Avoid warnings when virt-what produces no output

* Tue Apr 02 2013 Todd Zullinger <tmz@pobox.com> - 1.6.18-2
- Apply upstream patch to filter virt-what warnings from virtual fact

* Mon Mar 18 2013 Todd Zullinger <tmz@pobox.com> - 1.6.18-1
- Update to 1.6.18
- Restart puppet in %%postun (#806370)
- Require virt-what for improved KVM detection (#905592)
- Ensure man page is installed on EL < 7

* Tue Mar 12 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.17-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 25 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.6.17-1
- New upstream version, fixes rhbz #892734

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.16-1
- Update to 1.6.16

* Wed Nov 28 2012 Michael Stahnke <stahnma@puppetlabs.com> -  1.6.15-1
- Rebase to 1.6.15
- Put asc file back as Source1

* Fri Nov 09 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.13-2
- Add patch for ec2 fix
- Rebase to 1.6.14 via bz 871211

* Mon Oct 29 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.13-1
- Rebase to 1.6.13

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Todd Zullinger <tmz@pobox.com> - 1.6.6-1
- Update to 1.6.6

* Sun Feb 19 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-5
- Disable useless debuginfo generation (#795106, thanks to Ville Skyttä)
- Update summary and description
- Remove INSTALL from %%doc

* Wed Feb 15 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-4
- Only run rspec checks on Fedora >= 17

* Mon Feb 13 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-3
- Make spec file work for EPEL and Fedora
- Drop BuildArch: noarch and make dmidecode/pciutils deps arch-specific
- Make ec2 facts work on CentOS again (#790849, thanks to Jeremy Katz)
- Preserve timestamps when installing files

* Thu Feb 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.5-2
- Rebuilt for Ruby 1.9.3.

* Thu Jan 26 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-1
- Update to 1.6.5
- Require net-tools and pciutils, thanks to Dominic Cleal (#783749)

* Thu Jan 05 2012 Todd Zullinger <tmz@pobox.com> - 1.6.4-1
- Update to 1.6.4
- Require dmidecode (upstream #11041)

* Sat Oct 15 2011 Todd Zullinger <tmz@pobox.com> - 1.6.2-1
- Update to 1.6.2
- Update source URL

* Thu Sep 29 2011 Todd Zullinger <tmz@pobox.com> - 1.6.1-1
- Update to 1.6.1
- Minor spec file reformatting

* Wed Jul 27 2011 Todd Zullinger <tmz@pobox.com> - 1.6.0-2
- Update license tag, GPLv2+ -> ASL 2.0

* Thu Jul 14 2011 Todd Zullinger <tmz@pobox.com> - 1.6.0-1
- Update to 1.6.0

* Thu May 26 2011 Todd Zullinger <tmz@pobox.com> - 1.5.9-1
- Update to 1.5.9
- Improve Scientific Linux support, courtesy of Orion Poplawski (upstream #7682)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Todd Zullinger <tmz@pobox.com> - 1.5.8-1
- Update to 1.5.8

* Fri Sep 25 2009 Todd Zullinger <tmz@pobox.com> - 1.5.7-1
- Update to 1.5.7
- Update #508037 patch from upstream ticket

* Wed Aug 12 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.5.5-3
- Fix #508037 or upstream #2355

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Todd Zullinger <tmz@pobox.com> - 1.5.5-1
- Update to 1.5.5
- Drop upstreamed libperms patch

* Sat Feb 28 2009 Todd Zullinger <tmz@pobox.com> - 1.5.4-1
- New version
- Use upstream install script

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Todd Zullinger <tmz@pobox.com> - 1.5.2-1
- New version
- Simplify spec file checking for Fedora and RHEL versions

* Mon Sep  8 2008 David Lutterkort <dlutter@redhat.com> - 1.5.1-1
- New version

* Thu Jul 17 2008 David Lutterkort <dlutter@redhat.com> - 1.5.0-3
- Change 'mkdir' in install to 'mkdir -p'

* Thu Jul 17 2008 David Lutterkort <dlutter@redhat.com> - 1.5.0-2
- Remove files that were listed twice in files section

* Mon May 19 2008 James Turnbull <james@lovedthanlosty.net> - 1.5.0-1
- New version
- Added util and plist files

* Mon Sep 24 2007 David Lutterkort <dlutter@redhat.com> - 1.3.8-1
- Update license tag
- Copy all of lib/ into ruby_sitelibdir

* Thu Mar 29 2007 David Lutterkort <dlutter@redhat.com> - 1.3.7-1
- New version

* Fri Jan 19 2007 David Lutterkort <dlutter@redhat.com> - 1.3.6-1
- New version

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 1.3.5-3
- require which; facter is very unhappy without it

* Mon Nov 20 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-2
- Make require ruby(abi) and buildarch: noarch conditional for fedora 5 or
  later to allow building on older fedora releases

* Tue Oct 10 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-1
- New version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 1.3.4-1
- New version

* Wed Sep 13 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-2
- Rebuilt for FC6

* Wed Jun 28 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-1
- Rebuilt

* Fri Jun 19 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Fixed spec file to work again with the extra memory and processor files.
- Require ruby(abi). Build as noarch

* Fri Jun 9 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Added memory.rb and processor.rb

* Mon Apr 17 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-4
- Rebuilt with changed upstream tarball

* Tue Mar 21 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-3
- Do not rely on install.rb, it will be deleted upstream

* Mon Mar 13 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-2
- Commented out noarch; requires fix for bz184199

* Mon Mar  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-1
- Removed unused macros

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-2
- Fix BuildRoot. Add dist to release tag

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-1
- Initial build.
