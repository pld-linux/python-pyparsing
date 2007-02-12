
%define 	module	pyparsing

Summary:	pyparsing - a Python module for creating executing simple grammars
Summary(pl.UTF-8):   pyparsing - moduł Pythona umożliwiający tworzenie i parsowanie prostych gramatyk
Name:		python-%{module}
Version:	1.4.5
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyparsing/%{module}-%{version}.tar.gz
# Source0-md5:	d4a9108e7a4e4aacda28f055d8cb4f89
URL:		http://pyparsing.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
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

%package doc
Summary:	Documentation for pyparsing module
Summary(pl.UTF-8):   Dokumentacja do modułu pyparsing
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for pyparsing Python module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona pyparsing.

%package examples
Summary:	Examples for pyparsing module
Summary(pl.UTF-8):   Przykłady do modułu pyparsing
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for pyparsing Python module.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe skrypty dla modułu Pythona pyparsing.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitescriptdir}/pyparsing.py[co]
%{py_sitescriptdir}/pyparsing-*.egg-info

%files doc
%defattr(644,root,root,755)
%doc HowToUsePyparsing.html htmldoc pyparsingClassDiagram.{JPG,PNG}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
