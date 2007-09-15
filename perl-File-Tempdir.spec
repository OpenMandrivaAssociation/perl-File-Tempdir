%define module	File-Tempdir
%define name	perl-%{module}
%define version	0.02
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A module to make easier temporary directories deletion
License:	GPL
Group:		Development/Perl
Source:		%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/module/RPM4
Buildroot:	%{_tmppath}/%{name}-root
BuildRequires: perl-devel >= 5.8.0
Requires:	perl
BuildArch: noarch

%description
A module to make easier temporary directories deletion

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/*/*

