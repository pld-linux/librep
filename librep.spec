Summary:	Embeddable Lisp environment
Name:		librep
Version:	0.12.4
Release:	1
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/librep/%{name}-%{version}.tar.gz
Patch0:		librep-info.patch
URL:		http://www.dcs.warwick.ac.uk/~john/sw/librep.html
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a lightweight LISP environment for UNIX. It contains a LISP
interpreter, byte-code compiler and virtual machine. Applications may
use the LISP interpreter as an extension language, or it may be used
for standalone scripts.

Originally inspired by Emacs Lisp, the language dialect combines many
of the elisp features while trying to remove some of the main
deficiencies, with features from Common Lisp.

%package jl
Summary:	*.jl Lisp source files
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description jl
Lisp source files.

%package devel
Summary:	librep include files and link libraries
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description devel
Link libraries and C header files for librep development.

%package static
Summary:	librep static libraries
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	%{name}-devel = %{version}

%description static
Librep static libraries.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libexecdir}/rep/%{version}/%{_host}/*.so

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/librep* \
	NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rep
%attr(755,root,root) %{_bindir}/rep-remote
%attr(755,root,root) %{_bindir}/rep-xgettext
%attr(755,root,root) %{_bindir}/repdoc
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/rep
%dir %{_datadir}/rep/%{version}
%dir %{_datadir}/rep/%{version}/lisp
%{_datadir}/rep/%{version}/lisp/*.jlc
%dir %{_libexecdir}/rep
%dir %{_libexecdir}/rep/%{version}
%dir %{_libexecdir}/rep/%{version}/%{_host}
%{_libexecdir}/rep/%{version}/%{_host}/DOC
%attr(755,root,root) %{_libexecdir}/rep/%{version}/%{_host}/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{version}/%{_host}/*.la

%files jl
%defattr(644,root,root,755)
%{_datadir}/rep/%{version}/lisp/*.jl

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rep-config
%attr(755,root,root) %{_bindir}/repdoc
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/rep.h
%{_includedir}/rep_*.h
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/libtool
%{_libexecdir}/rep/%{_host}/rules.mk
%{_aclocaldir}/rep.m4
%{_infodir}/librep*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libexecdir}/rep/%{version}/%{_host}/*.a
