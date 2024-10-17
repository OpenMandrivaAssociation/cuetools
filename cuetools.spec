Summary: Utilities to works with cue and TOC files
Name: cuetools
Version:	1.4.1
Release:	1
Source0: https://github.com/svend/cuetools/archive/%{version}.tar.gz
Source1: cuetag.sh
License: GPL
Group: Archiving/Cd burning
Url: https://cuetools.sourceforge.net
BuildRequires:	bison
BuildRequires:	flex

%description
Cuetools is a set of utilities for working with cue files and TOC files.
It includes programs for conversion between the formats, file renaming based
on cue/TOC information, and track breakpoint printing. 

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make

%install
%makeinstall_std

install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%files
%doc NEWS TODO
%_bindir/*
%_mandir/man1/*
