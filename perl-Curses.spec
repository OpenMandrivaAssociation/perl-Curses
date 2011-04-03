%define upstream_name	 Curses
%define upstream_version 1.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl module for character screen handling and windowing
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GI/GIRAFFED/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	libncursesw-devel
BuildRequires:	perl-devel

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Curses is the interface between Perl and your system's curses(3) library. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"
chmod 644 Artistic Copying INSTALL README

%check
%make test

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
