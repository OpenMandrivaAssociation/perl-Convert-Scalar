%define upstream_name    Convert-Scalar
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert-Scalar module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module exports various internal perl methods that change the internal
representation or state of a perl scalar. All of these work in-place, that is,
they modify their scalar argument. No functions are exported by default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes COPYING README
%{perl_vendorarch}/Convert/Scalar.pm
%{perl_vendorarch}/auto/Convert/Scalar
%{_mandir}/*/*
