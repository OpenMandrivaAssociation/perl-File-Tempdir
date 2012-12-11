%define upstream_name	 File-Tempdir
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A module to make easier temporary directories deletion
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
A module to make easier temporary directories deletion

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/*/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 654964
- rebuild for updated spec-helper

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 407749
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-6mdv2009.0
+ Revision: 257035
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.02-4mdv2008.1
+ Revision: 152082
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2008.0
+ Revision: 86403
- rebuild


* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/10/06 20:16:33 (55501)
- 0.02

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 15:57:30 (54837)
- really add patch0

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 15:56:47 (54836)
- add upstream patch0

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 13:32:17 (54725)
- initial mdv package

