%define upstream_name       HTML-WikiConverter-MediaWiki
%define upstream_version    0.59

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Convert HTML to MediaWiki markup
Url:		https://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::WikiConverter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
This module contains rules for converting HTML into MediaWiki markup. See
the HTML::WikiConverter manpage for additional usage details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.590.0-2mdv2011.0
+ Revision: 654349
- rebuild for updated spec-helper

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.590.0-1mdv2011.0
+ Revision: 612364
- normalize perl version

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.59-1mdv2011.0
+ Revision: 606981
- import perl-HTML-WikiConverter-MediaWiki

