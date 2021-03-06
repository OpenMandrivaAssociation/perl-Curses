%define	modname	Curses
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
%setup -qn %{modname}-%{modver}
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
%{_mandir}/man3/*
