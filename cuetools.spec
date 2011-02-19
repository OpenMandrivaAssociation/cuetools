%define name cuetools
%define version 1.3.1
%define release %mkrel 8

Summary: Utilities to works with cue and TOC files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: cuetag.sh
License: GPL
Group: Archiving/Cd burning
Url: http://cuetools.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Cuetools is a set of utilities for working with cue files and TOC files.
It includes programs for conversion between the formats, file renaming based
on cue/TOC information, and track breakpoint printing. 

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README TODO
%_bindir/*
%_mandir/man1/*
