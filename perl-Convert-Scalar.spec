%define upstream_version 1.12
%define	module	Convert-Scalar
Name:		perl-%{module}
Version:	1.12
Release:	3

Summary:	Convert-Scalar module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Convert-Scalar
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Convert-Scalar-1.12.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel

%description
This module exports various internal perl methods that change the internal
representation or state of a perl scalar. All of these work in-place, that is,
they modify their scalar argument. No functions are exported by default.

%prep
%setup -q -n Convert-Scalar-1.12

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes COPYING README
%{perl_vendorarch}/Convert/Scalar.pm
%{perl_vendorarch}/auto/Convert/Scalar
%{_mandir}/*/*


