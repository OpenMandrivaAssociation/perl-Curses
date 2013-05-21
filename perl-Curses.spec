%define	modname	Curses
%define	modver	1.28

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	13

Summary:	Perl module for character screen handling and windowing
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GI/GIRAFFED/%{modname}-%{modver}.tgz

BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	perl-devel

%description
Curses is the interface between Perl and your system's curses(3) library. 

%prep
%setup -q -n %{modname}-%{modver}
find -type f | xargs chmod o+r

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Artistic README
%{perl_vendorarch}/auto/Curses
%{perl_vendorarch}/Curses*
%{_mandir}/*/*

%changelog
* Wed Dec 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.280.0-11
- rebuild for new perl-5.16.2
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.280.0-8mdv2012.0
+ Revision: 765140
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.280.0-7
+ Revision: 763654
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.280.0-6
+ Revision: 763236
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.280.0-5
+ Revision: 667064
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 1.280.0-4
+ Revision: 650064
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.280.0-3mdv2011.0
+ Revision: 564393
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.280.0-2mdv2011.0
+ Revision: 555270
- rebuild

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.1
+ Revision: 497005
- update to 1.28

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.27-1mdv2010.0
+ Revision: 374655
- update to new version 1.27

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.1
+ Revision: 292069
- update to new version 1.24

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.23-2mdv2009.0
+ Revision: 265344
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.0
+ Revision: 194842
- update to new version 1.23
- update to new version 1.23

* Mon Feb 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2008.1
+ Revision: 170104
- update to new version 1.21

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.20-2mdv2008.1
+ Revision: 151253
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.1
+ Revision: 133603
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Oct 26 2006 Pixel <pixel@mandriva.com> 1.15-2mdv2007.0
+ Revision: 72681
- no need explictly requiring ncurses
- we now need to BuildRequires libncursesw-devel
- increase release
- use ncursesw (to handle wide-chars, and so utf8)

* Sat Oct 21 2006 Pixel <pixel@mandriva.com> 1.15-1mdv2007.1
+ Revision: 71567
- new version
- add "make test"
- Import perl-Curses

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdk
- New release 1.13
- spec cleanup
- %%mkrel

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- 1.12 
- rpmbuildupdate aware

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.07-1mdk
- New version 1.07
- Drop patch 0

* Wed Apr 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.06-8mdk
- rebuild for new perl

