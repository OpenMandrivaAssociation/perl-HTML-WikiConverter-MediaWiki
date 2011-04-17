%define upstream_name       HTML-WikiConverter-MediaWiki
%define upstream_version    0.59

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Convert HTML to MediaWiki markup
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(HTML::WikiConverter)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module contains rules for converting HTML into MediaWiki markup. See
the HTML::WikiConverter manpage for additional usage details.





%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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


