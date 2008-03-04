%define up_name ocamlbdb
%define name	ocaml-bdb
%define version	4.3.21
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml interface to Berkeley-DB
Source: 	http://www.eecs.harvard.edu/~stein/%{up_name}-%{version}.tar.bz2
URL:		http://www.eecs.harvard.edu/~stein/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	db4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CamlGI is a library to enable you to write CGI and FastCGI in OCaml. It is
written 100% in OCaml so should run on many platforms. The library supports
multiple simultaneous connections and request multiplexing while presenting an
easy to use interface.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	db4-devel
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
make BDB_DIR=%{_prefix} CFLAGS="-I%{_libdir}/ocaml/"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/bdb 
install -m 644 bdb.cma bdb.cmi libcamlbdb.a %{buildroot}/%{ocaml_sitelib}/bdb

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CREDITS README
%dir %{ocaml_sitelib}/bdb
%{ocaml_sitelib}/bdb/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/bdb/*
%exclude %{ocaml_sitelib}/bdb/*.cmi
