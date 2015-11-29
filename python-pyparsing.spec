#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pyparsing
Summary:	pyparsing - a Python module for creating executing simple grammars
Summary(pl.UTF-8):	pyparsing - moduł Pythona umożliwiający tworzenie i parsowanie prostych gramatyk
Name:		python-%{module}
Version:	2.0.1
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyparsing/%{module}-%{version}.tar.gz
# Source0-md5:	37adec94104b98591507218bc82e7c31
URL:		http://pyparsing.sourceforge.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-distribute
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The parsing module is an alternative approach to creating and
executing simple grammars, vs. the traditional lex/yacc approach, or
the use of regular expressions. The parsing module provides a library
of classes that client code uses to construct the grammar directly in
Python code.

%description -l pl.UTF-8
Moduł pyparsing umożliwia tworzenie i parsowanie prostych gramatyk w
sposób odmienny od podejścia tradycyjnego, jakim jest zwykle użycie
pary lex/yacc lub wyrażeń regularnych. Moduł ten udostępnia bibliotekę
klas, przy pomocy których gramatyka tworzona jest wprost w kodzie
Pythona.

%package -n python3-%{module}
Summary:	pyparsing - a Python3 module for creating executing simple grammars
Summary(pl.UTF-8):	pyparsing - moduł Pythona3 umożliwiający tworzenie i parsowanie prostych gramatyk
Group:		Libraries/Python

%description -n python3-%{module}
The parsing module is an alternative approach to creating and
executing simple grammars, vs. the traditional lex/yacc approach, or
the use of regular expressions. The parsing module provides a library
of classes that client code uses to construct the grammar directly in
Python code.

%description -n python3-%{module} -l pl.UTF-8
Moduł pyparsing umożliwia tworzenie i parsowanie prostych gramatyk w
sposób odmienny od podejścia tradycyjnego, jakim jest zwykle użycie
pary lex/yacc lub wyrażeń regularnych. Moduł ten udostępnia bibliotekę
klas, przy pomocy których gramatyka tworzona jest wprost w kodzie
Pythona.

%package doc
Summary:	Documentation for pyparsing module
Summary(pl.UTF-8):	Dokumentacja do modułu pyparsing
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for pyparsing Python module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona pyparsing.

%package examples
Summary:	Examples for pyparsing module
Summary(pl.UTF-8):	Przykłady do modułu pyparsing
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for pyparsing Python module.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe skrypty dla modułu Pythona pyparsing.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitescriptdir}/pyparsing.py[co]
%{py_sitescriptdir}/pyparsing-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES README
%{py3_sitescriptdir}/pyparsing.py
%{py3_sitescriptdir}/__pycache__/pyparsing*.py[co]
%{py3_sitescriptdir}/pyparsing-*.egg-info
%endif

%files doc
%defattr(644,root,root,755)
%doc HowToUsePyparsing.html htmldoc pyparsingClassDiagram.{JPG,PNG}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
