# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	Ispell
Summary:	Lingua::Ispell Perl module
Summary(pl):	Modu³ Perla Lingua::Ispell
Name:		perl-Lingua-Ispell
Version:	0.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
Requires:	ispell >= 3.1.20-35
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::Ispell - Perl module encapsulating access to the Ispell
program.

%description -l pl
Lingua::Ispell - modu³ Perla obudowuj±cy dostêp do programu Ispell.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Lingua/Ispell.pm
%{_mandir}/man3/*
