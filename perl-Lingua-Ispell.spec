#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	Ispell
Summary:	Lingua::Ispell Perl module
Summary(pl):	Modu³ Perla Lingua::Ispell
Name:		perl-Lingua-Ispell
Version:	0.07
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f6a364daccf28a5c208fa1a3df83daa
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Lingua/Ispell.pm
%{_mandir}/man3/*
