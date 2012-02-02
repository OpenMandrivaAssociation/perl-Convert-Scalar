%define	module	Convert-Scalar
%define	upstream_version 1.04

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert-Scalar module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{module}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel

%description
This module exports various internal perl methods that change the internal
representation or state of a perl scalar. All of these work in-place, that is,
they modify their scalar argument. No functions are exported by default.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes COPYING README
%{perl_vendorarch}/Convert/Scalar.pm
%{perl_vendorarch}/auto/Convert/Scalar
%{_mandir}/*/*
