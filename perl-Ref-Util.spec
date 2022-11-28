#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Ref
%define		pnam	Util
Summary:	Ref::Util - Utility functions for checking references
Name:		perl-Ref-Util
Version:	0.204
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	add072ed1e481dc43ad6bb8bbe36ab99
URL:		http://search.cpan.org/dist/Ref-Util/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test2)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ref::Util introduces several functions to help identify references in
a smarter (and usually faster) way.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/%{pdir}
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
