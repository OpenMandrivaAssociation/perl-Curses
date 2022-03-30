# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname Curses
%define modver 1.32

Summary:	Perl module for character screen handling and windowing
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	29
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GI/GIRAFFED/%{modname}-%{modver}.tgz
BuildRequires:	perl(Test::More)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	perl-devel

%description
Curses is the interface between Perl and your system's curses(3) library. 

%prep
%autosetup -n %{modname}-%{modver} -p1
find -type f | xargs chmod o+r

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Artistic README
%{perl_vendorarch}/auto/Curses
%{perl_vendorarch}/Curses*
%doc %{_mandir}/man3/*
