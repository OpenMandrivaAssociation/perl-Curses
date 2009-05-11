%define module	Curses
%define name	perl-%{module}
%define version 1.27
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module for character screen handling and windowing
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/G/GI/GIRAFFED/%{module}-%{version}.tgz
BuildRequires:	perl-devel
BuildRequires:	libncursesw-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Curses is the interface between Perl and your system's curses(3) library. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"
chmod 644 Artistic Copying INSTALL README

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Artistic Copying INSTALL README
%{perl_vendorarch}/auto/Curses
%{perl_vendorarch}/Curses*
%{_mandir}/*/*


