Summary:	Embeddable Lisp environment
Name:		librep
Version:	0.14
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	http://download.sourceforge.net/librep/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_version.patch
URL:		http://librep.sourceforge.net/
BuildRequires:	autoconf >= 2.3-12
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
This is a lightweight LISP environment for UNIX. It contains a LISP
interpreter, byte-code compiler and virtual machine. Applications may
use the LISP interpreter as an extension language, or it may be used
for standalone scripts.

Originally inspired by Emacs Lisp, the language dialect combines many
of the elisp features while trying to remove some of the main
deficiencies, with features from Common Lisp.

%package devel
Summary:	librep include files and link libraries
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}
Obsoletes:	librep-jl

%description devel
Link libraries and C header and Lisp source files for librep
development.

%package static
Summary:	librep static libraries
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name}-devel = %{version}

%description static
Librep static libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

install src/rep_config.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf NEWS README TODO

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
%dir %{_datadir}/rep/lisp
%dir %{_datadir}/rep/lisp/scheme
%dir %{_datadir}/rep/lisp/unscheme
%dir %{_datadir}/rep/lisp/rep/data
%dir %{_datadir}/rep/lisp/rep/i18n
%dir %{_datadir}/rep/lisp/rep/io
%dir %{_datadir}/rep/lisp/rep/io/file-handlers
%dir %{_datadir}/rep/lisp/rep/lang
%dir %{_datadir}/rep/lisp/rep/mail
%dir %{_datadir}/rep/lisp/rep/net
%dir %{_datadir}/rep/lisp/rep/system
%dir %{_datadir}/rep/lisp/rep/threads
%dir %{_datadir}/rep/lisp/rep/util
%dir %{_datadir}/rep/lisp/rep/vm
%dir %{_datadir}/rep/lisp/rep/vm/compiler
%dir %{_datadir}/rep/lisp/rep/www
%{_datadir}/rep/lisp/*.jlc
%{_datadir}/rep/lisp/*/*.jlc
%{_datadir}/rep/lisp/*/*/*.jlc
%{_datadir}/rep/lisp/*/*/*/*.jlc
%{_datadir}/rep/lisp/*/*/*/*/*.jlc
%dir %{_libexecdir}/rep
%dir %{_libexecdir}/rep/%{_host}
%dir %{_libexecdir}/rep/%{_host}/rep
%dir %{_libexecdir}/rep/%{_host}/rep/*
%{_libexecdir}/rep/%{_host}/DOC
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*/*.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*/*/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*/*/*.la

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rep-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/libtool
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/install-aliases
%{_libexecdir}/rep/%{_host}/rules.mk
%{_aclocaldir}/rep.m4
%{_infodir}/librep*
%{_datadir}/rep/lisp/*.jl
%{_datadir}/rep/lisp/*/*.jl
%{_datadir}/rep/lisp/*/*/*.jl
%{_datadir}/rep/lisp/*/*/*/*.jl
%{_datadir}/rep/lisp/*/*/*/*/*.jl

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libexecdir}/rep/%{_host}/rep/*/*.a
