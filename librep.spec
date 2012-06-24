Summary:	Embeddable Lisp environment
Summary(es):	Ambiente LISP que se puede incluir
Summary(pl):	�rodowisko do zagnie�d�ania Lispa
Summary(pt_BR):	Ambiente LISP embut�vel
Summary(ru):	������������ ����� LISP
Summary(uk):	����������� ���������� LISP
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
Este es un ambiente LISP (sencillo, ocupa poca memoria y r�pido) para
UNIX. Este paquete contiene un interpretador LISP, compilador de
byte-code y una m�quinavirtual. Las aplicaciones pueden usar el
interpretador LISP como un lenguaje deextensi�n, o el interpretador
puede usarse para scripts separados.

Instalado originalmente en Emacs LISP, este dialecto combina muchos de
los recursos de elisp al mismo tiempo en que intenta eliminar algunas
de sus deficiencias, con recursos de Common LISP.

%description -l pl
To jest niewielkie �rodowisko LISP dla Uniksa. Zawiera interpreter
LISP-a, kompilator bytecodu i maszyn� wirtualn�. Aplikacje mog� u�ywa�
interpretera LISP-a jako rozszerzenia j�zyka lub w oddzielnych
skryptach.

Oryginalnie zainspirowany przez Emacs Lisp, ten dialekt j�zyka ��czy
wiele cech elispa, pr�buj�c usun�� niekt�re z g��wnych utrudnie�, z
cechami Common Lispa.

%description -l pt_BR
Esse � um ambiente LISP leve para UNIX. Esse pacote cont�m um
interpretador LISP, compilador de byte-code e uma m�quina virtual.
Aplica��es podem usar o interpretador LISP como uma linguagem de
extens�o, ou o interpretador pode ser usado para scripts isolados.

Originalmente inspirado pelo Emacs LISP, esse dialeto combina muitos
dos recursos do elisp ao mesmo tempo em que tenta remover algumas de
suas defici�ncias, com recursos do Common LISP.

%description -l ru
Librep - ��� ������� ����� LISP ��� ������������� ���������� � ������
���������� ��� ��������. Librep � ������� ������� (���� � ��
���������) ��������� � Emacs LISP. Librep �������� ������������� LISP,
����-������� ���������� � ����������� ������. ���������� �����
����������� ������������� LISP ��� ���� ���������� ��� ��� �������
��������������� ���������.

%description -l uk
Librep - �� Ħ����� ���� LISP ��� ������������ ���������� � ��ۦ
�������Φ �������� �� ������. Librep ������� ͦ��� (���� � ��
���Φ���) ��ͦ���� � Emacs LISP. Librep ͦ����� ������������� LISP,
����-������� ���Ц����� �� צ�������� ������. �������� ������
��������������� ������������� LISP �� ���� ���������� �� ��� �������
צ����������� �����Ҧ��.

%package devel
Summary:	librep include files and link libraries
Summary(es):	Archivos de cabezamiento y bibliotecas para librep
Summary(pl):	Pliki nag��wkowe do librep
Summary(pt_BR):	Arquivos de cabe�alho e bibliotecas para o librep
Summary(ru):	����� ��� ���������� ��������, ������������ librep
Summary(uk):	����� ��� �������� ������� � ������������� librep
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
Pliki nag��wkowe i �r�d�a Lispa do tworzenia program�w z u�yciem
librep.

%description devel -l pt_BR
Bibliotecas para liga��o e arquivos de cabe�alho para desenvolvimento
com librep.

%description devel -l ru
����� ��� ���������� �������� � �������������� librep. Librep - ���
������������ ������� LISP.

%description devel -l uk
����� ��� �������� ������� � ������������� librep. Librep - ��
������������ Ħ����� LISP.

%package static
Summary:	librep static libraries
Summary(pl):	Biblioteki statyczne librep
Summary(ru):	����������� ���������� librep
Summary(uk):	������Φ ¦�̦����� librep
Group:		Development/Languages
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Librep static libraries.

%description static -l pl
Biblioteki statyczne librep.

%description static -l ru
����������� ���������� ��� ���������� �������� � ��������������
librep. Librep - ��� ������������ ������� LISP.

%description static -l uk
������Φ ¦�̦����� ��� �������� ������� � ������������� librep.
Librep - �� ������������ Ħ����� LISP.

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
