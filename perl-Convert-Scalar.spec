%define real_name Convert-Scalar

Summary:	Convert-Scalar module for perl 
Name:		perl-%{real_name}
Version:	1.03
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module exports various internal perl methods that change the internal
representation or state of a perl scalar. All of these work in-place, that is,
they modify their scalar argument. No functions are exported by default.

%prep
%setup -q -n %{real_name}-%{version} 

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

