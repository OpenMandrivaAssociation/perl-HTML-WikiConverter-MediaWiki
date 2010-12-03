
%define realname   HTML-WikiConverter-MediaWiki
%define version    0.59
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Convert HTML to MediaWiki markup
Source:     http://www.cpan.org/modules/by-module/HTML/%{realname}-%{version}.tar.xz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(HTML::WikiConverter)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)

BuildArch: noarch

%description
This module contains rules for converting HTML into MediaWiki markup. See
the HTML::WikiConverter manpage for additional usage details.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


