Summary: Utilities to works with cue and TOC files
Name: cuetools
Version: 1.3.1
Release:	1
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


%changelog
* Sat Feb 19 2011 Александр Казанцев <kazancas@mandriva.org> 1.3.1-8mdv2011.0
+ Revision: 638690
- add script cuetag.sh

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-7mdv2011.0
+ Revision: 617458
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-6mdv2010.0
+ Revision: 425436
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3.1-5mdv2009.0
+ Revision: 243803
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.3.1-3mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3.1-3mdv2008.0
+ Revision: 68429
- rebuild


* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 00:07:09 (53155)
- rebuild

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 00:05:35 (53154)
Import cuetools

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 1.3.1-1mdk
- 1.3.1

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 1.3-2mdk
- rebuild

* Tue Mar 22 2005 Olivier Thauvin <nanardon@mandrake.org> 1.3-1mdk
- 1.3
- %%mkrel

* Fri May 07 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.6-1mdk
- 1st spec file

