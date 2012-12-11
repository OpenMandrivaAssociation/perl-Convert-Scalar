%define	module	Convert-Scalar
%define	upstream_version 1.1

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert-Scalar module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{module}-%{upstream_version}.tar.gz

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


%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.100.0-4
+ Revision: 770599
- new version
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.40.0-3
+ Revision: 680847
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 555703
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 406921
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.04-3mdv2009.0
+ Revision: 256138
- rebuild

* Sun Mar 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2008.1
+ Revision: 183108
- update to new version 1.04

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 1.03-4mdv2008.1
+ Revision: 151884
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-3mdv2008.0
+ Revision: 86231
- rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:02:55 (58443)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:57:21 (58436)
Import perl-Convert-Scalar

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.03-1mdk
- 1.03
- use perl_vendorarch macro

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.01-1mdk
- initial Mandriva package

