Summary:	Embeddable Lisp environment
Summary(es):	Ambiente LISP que se puede incluir
Summary(pl):	╕rodowisko do zagnie©d©ania Lispa
Summary(pt_BR):	Ambiente LISP embutМvel
Summary(ru):	Встраиваемая среда LISP
Summary(uk):	Вбудовуване середовище LISP
Name:		librep
Version:	0.17
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ad4ad851ff9f82a5d61024cd96bc2998
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_version.patch
Patch2:		%{name}-longdouble.patch
Patch3:		%{name}-config.patch
Patch4:		%{name}-am18.patch
URL:		http://librep.sourceforge.net/
BuildRequires:	autoconf >= 2.3-12
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel >= 4.1-3
BuildRequires:	libffi-devel
BuildRequires:	readline-devel >= 5.0
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

%description -l es
Este es un ambiente LISP (sencillo, ocupa poca memoria y rАpido) para
UNIX. Este paquete contiene un interpretador LISP, compilador de
byte-code y una mАquinavirtual. Las aplicaciones pueden usar el
interpretador LISP como un lenguaje deextensiСn, o el interpretador
puede usarse para scripts separados.

Instalado originalmente en Emacs LISP, este dialecto combina muchos de
los recursos de elisp al mismo tiempo en que intenta eliminar algunas
de sus deficiencias, con recursos de Common LISP.

%description -l pl
To jest niewielkie ╤rodowisko LISP dla Uniksa. Zawiera interpreter
LISP-a, kompilator bytecodu i maszynЙ wirtualn╠. Aplikacje mog╠ u©ywaФ
interpretera LISP-a jako rozszerzenia jЙzyka lub w oddzielnych
skryptach.

Oryginalnie zainspirowany przez Emacs Lisp, ten dialekt jЙzyka Ё╠czy
wiele cech elispa, prСbuj╠c usun╠Ф niektСre z gЁСwnych utrudnieЯ, z
cechami Common Lispa.

%description -l pt_BR
Esse И um ambiente LISP leve para UNIX. Esse pacote contИm um
interpretador LISP, compilador de byte-code e uma mАquina virtual.
AplicaГУes podem usar o interpretador LISP como uma linguagem de
extensЦo, ou o interpretador pode ser usado para scripts isolados.

Originalmente inspirado pelo Emacs LISP, esse dialeto combina muitos
dos recursos do elisp ao mesmo tempo em que tenta remover algumas de
suas deficiЙncias, com recursos do Common LISP.

%description -l ru
Librep - это диалект языка LISP для использования встроенным в другие
приложения или отдельно. Librep в большой степени (хотя и не
полностью) совместим с Emacs LISP. Librep содержит интерпретатор LISP,
байт-кодовый компилятор и виртуальную машину. Приложения могут
использвать интерпретатор LISP как язык расширения или для запуска
самостоятельных сценариев.

%description -l uk
Librep - це д╕алект мови LISP для використання вбудованим в ╕нш╕
прикладн╕ програми чи окремо. Librep великою м╕рою (хоча й не
повн╕стю) сум╕сний з Emacs LISP. Librep м╕стить ╕нтерпретатор LISP,
байт-кодовий комп╕лятор та в╕ртуальну машину. Програми можуть
використовувати ╕нтерпретатор LISP як мову розширення чи для запуску
в╕докремлених сценар╕╖в.

%package devel
Summary:	librep include files and link libraries
Summary(es):	Archivos de cabezamiento y bibliotecas para librep
Summary(pl):	Pliki nagЁСwkowe do librep
Summary(pt_BR):	Arquivos de cabeГalho e bibliotecas para o librep
Summary(ru):	Файлы для разработки программ, использующих librep
Summary(uk):	Файли для розробки програм з використанням librep
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gmp-devel >= 4.1-3
Obsoletes:	librep-jl

%description devel
Link libraries and C header and Lisp source files for librep
development.

%description devel -l es
Bibliotecas para enlace y archivos de encabezamiento para desarrollo
con librep.

%description devel -l pl
Pliki nagЁСwkowe i ╪rСdЁa Lispa do tworzenia programСw z u©yciem
librep.

%description devel -l pt_BR
Bibliotecas para ligaГЦo e arquivos de cabeГalho para desenvolvimento
com librep.

%description devel -l ru
Файлы для разработки программ с использованием librep. Librep - это
встраиваемый диалект LISP.

%description devel -l uk
Файли для розробки програм з використанням librep. Librep - це
вбудовуваний д╕алект LISP.

%package static
Summary:	librep static libraries
Summary(pl):	Biblioteki statyczne librep
Summary(ru):	Статические библиотеки librep
Summary(uk):	Статичн╕ б╕бл╕отеки librep
Group:		Development/Languages
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Librep static libraries.

%description static -l pl
Biblioteki statyczne librep.

%description static -l ru
Статические библиотеки для разработки программ с использованием
librep. Librep - это встраиваемый диалект LISP.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки програм з використанням librep.
Librep - це вбудовуваний д╕алект LISP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-static
%{__make} \
	host_type=%{_host}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir} \
	host_type=%{_host}

# remove useless static plugins
# *.la can be used to load plugins and may contain additional information
rm -f $RPM_BUILD_ROOT%{_libexecdir}/rep/%{_host}/rep{,/*,/*/*}/*.a

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
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/rep
%attr(755,root,root) %{_bindir}/rep-remote
%attr(755,root,root) %{_bindir}/rep-xgettext
%attr(755,root,root) %{_bindir}/repdoc
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/rep
%{_datadir}/rep/lisp
%exclude %{_datadir}/rep/lisp/*.jl
%exclude %{_datadir}/rep/lisp/*/*.jl
%exclude %{_datadir}/rep/lisp/*/*/*.jl
%exclude %{_datadir}/rep/lisp/*/*/*/*.jl
%exclude %{_datadir}/rep/lisp/*/*/*/*/*.jl
%dir %{_libexecdir}/rep
%dir %{_libexecdir}/rep/%{_host}
%{_libexecdir}/rep/%{_host}/doc-strings
%{_libexecdir}/rep/%{_host}/*.la
%dir %{_libexecdir}/rep/%{_host}/rep
%dir %{_libexecdir}/rep/%{_host}/rep/data
%dir %{_libexecdir}/rep/%{_host}/rep/i18n
%dir %{_libexecdir}/rep/%{_host}/rep/io
%dir %{_libexecdir}/rep/%{_host}/rep/io/db
%dir %{_libexecdir}/rep/%{_host}/rep/lang
%dir %{_libexecdir}/rep/%{_host}/rep/util
%dir %{_libexecdir}/rep/%{_host}/rep/vm
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*.so
%{_libexecdir}/rep/%{_host}/rep/*.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*/*.so
%{_libexecdir}/rep/%{_host}/rep/*/*.la
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/rep/*/*/*.so
%{_libexecdir}/rep/%{_host}/rep/*/*/*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rep-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_libexecdir}/rep/%{_host}/rep_config.h
%attr(755,root,root) %{_libexecdir}/rep/%{_host}/emulate-gnu-tar
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
