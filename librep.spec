#%define	dsnap	2002-06-11
#%define	snap	%(echo %{dsnap} | sed -e "s#-##g")
Summary:	Embeddable Lisp environment
Summary(pl):	¦rodowisko do zagnie¿d¿ania Lispa
Name:		librep
Version:	0.16
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/librep/%{name}-%{version}.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_version.patch
URL:		http://librep.sourceforge.net/
BuildRequires:	autoconf >= 2.3-12
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
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

%description -l pl
To jest niewielkie ¶rodowisko LISP dla uniksa. Zawiera interpreter
LISP-a, kompilator bytecodu i maszynê wirtualn±. Aplikacje mog± u¿ywaæ
interpretera LISP-a jako rozszerzenia jêzyka lub w oddzielnych
skryptach.

Oryginalnie zainspirowany przez Emacs Lisp, ten dialekt jêzyka ³±czy
wiele cech elispa, próbuj±c usun±æ niektóre z g³ównych utrudnieñ, z
cechami Common Lispa.

%package devel
Summary:	librep include files and link libraries
Summary(pl):	Pliki nag³ówkowe do librep
Group:		Development/Languages
Requires:	%{name} = %{version}
Requires:	gmp-devel >= 3.1.1
Obsoletes:	librep-jl

%description devel
Link libraries and C header and Lisp source files for librep
development.

%description devel -l pl
Pliki nag³ówkowe i ¼ród³a Lispa do tworzenia programów z u¿yciem
librep.

%package static
Summary:	librep static libraries
Summary(pl):	Biblioteki statyczne librep
Group:		Development/Languages
Requires:	%{name}-devel = %{version}

%description static
Librep static libraries.

%description static -l pl
Biblioteki statyczne librep.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure \
	--with-readline \
	--enable-static
%{__make} host_type=%{_host}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir} \
	host_type=%{_host}

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
%{_libexecdir}/rep/%{_host}/DOC
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/emulate-gnu-tar
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/*.la
%dir %{_libexecdir}/rep/%{_host}/rep
%dir %{_libexecdir}/rep/%{_host}/rep/data
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/data/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/data/*.la
%dir %{_libexecdir}/rep/%{_host}/rep/i18n
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/i18n/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/i18n/*.la
%dir %{_libexecdir}/rep/%{_host}/rep/io
%dir %{_libexecdir}/rep/%{_host}/rep/io/db
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/io/db/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/io/db/*.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/io/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/io/*.la
%dir %{_libexecdir}/rep/%{_host}/rep/lang
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/lang/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/lang/*.la
%dir %{_libexecdir}/rep/%{_host}/rep/util
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/util/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/util/*.la
%dir %{_libexecdir}/rep/%{_host}/rep/vm
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/vm/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/vm/*.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/*.so
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/*.la

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
%{_libexecdir}/rep/%{_host}/rep_config.h
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
