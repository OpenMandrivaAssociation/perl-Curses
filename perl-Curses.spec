# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define module Curses

Summary:	Perl module for character screen handling and windowing
Name:		perl-%{module}
Version:	1.41
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Curses/Curses-%{version}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	perl-devel

%description
Curses is the interface between Perl and your system's curses(3) library. 

%files
%doc Artistic README
%{perl_vendorarch}/auto/Curses
%{perl_vendorarch}/Curses*
%doc %{_mandir}/man3/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}
#find -type f | xargs chmod o+r

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install


