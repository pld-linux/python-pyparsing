
%define 	module	pyparsing

Summary:	pyparsing - a Python module for creating executing simple grammars
Summary(pl):	pyparsing - modu³ Pythona umo¿liwiaj±cy tworzenie i parsowanie prostych gramatyk
Name:		python-%{module}
Version:	1.2.2
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyparsing/%{module}-%{version}.tar.gz
# Source0-md5:	700967c4c78e171783fae1073f74ea8d
URL:		http://pyparsing.sourceforge.net/
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-modules
Requires:	python >= 2.3.2
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The parsing module is an alternative approach to creating and
executing simple grammars, vs. the traditional lex/yacc approach, or
the use of regular expressions. The parsing module provides a library
of classes that client code uses to construct the grammar directly in
Python code.

%description -l pl
Modu³ pyparsing umo¿liwia tworzenie i parsowanie prostych gramatyk w
sposób odmienny od podej¶cia tradycyjnego, jakim jest zwykle u¿ycie
pary lex/yacc lub wyra¿eñ regularnych. Modu³ ten udostêpnia bibliotekê
klas, przy pomocy których gramatyka tworzona jest wprost w kodzie
Pythona.

%package doc
Summary:	Documentation for pyparsing module
Summary(pl):	Dokumentacja do modu³u pyparsing
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for pyparsing Python module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona pyparsing.

%package examples
Summary:	Examples for pyparsing module
Summary(pl):	Przyk³ady do modu³u pyparsing
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for pyparsing Python module.

%description examples -l pl
Pakiet zawieraj±cy przyk³adowe skrypty dla modu³u Pythona pyparsing.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitescriptdir}/pyparsing.py[oc]

%files doc
%defattr(644,root,root,755)
%doc HowToUsePyparsing.html htmldoc pyparsingClassDiagram.{JPG,PNG}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
