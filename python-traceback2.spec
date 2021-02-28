# NOTE: traceback is a part of standard library since 2.?/3.?
#       however, traceback2 supports unicode on python2
#       traceback2 1.4.0 is backport of traceback between 3.4.0/3.5.0
#       traceback from cpython>=3.5.0 is more robust
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# test target

Summary:	Backport of traceback to older supported Pythons
Summary(pl.UTF-8):	Backport modułu traceback do starszych wersji Pythona
Name:		python-traceback2
Version:	1.4.0
Release:	4
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/traceback2
Source0:	https://files.pythonhosted.org/packages/source/t/traceback2/traceback2-%{version}.tar.gz
# Source0-md5:	9e9723f4d70bfc6308fa992dd193c400
URL:		https://github.com/testing-cabal/traceback2
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%if %{with tests}
BuildRequires:	python-contextlib2
BuildRequires:	python-fixtures
BuildRequires:	python-linecache2
BuildRequires:	python-testtools
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%if %{with tests}
BuildRequires:	python3-contextlib2
BuildRequires:	python3-fixtures
BuildRequires:	python3-linecache2
BuildRequires:	python3-testtools
BuildRequires:	python3-unittest2
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
traceback2 is a backport of traceback to older supported Pythons.

traceback module is used to print or retrieve a stack traceback.

In Python 2.x, unlike traceback, traceback2 creates unicode output
(because it depends on the linecache2 module).

%description -l pl.UTF-8
traceback2 to backport modułu traceback do starszych wersji Pythona.

Moduł traceback służy do wypisywania i odtwarzania śladu wywołań ze
stosu.

W Pythonie 2.x, w przeciwieństwie do modułu traceback, moduł
traceback2 tworzy wyjście w unikodzie (ponieważ zależy od modułu
linecache2).

%package -n python3-traceback2
Summary:	Backport of traceback to older supported Pythons
Summary(pl.UTF-8):	Backport modułu traceback do starszych wersji Pythona
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-traceback2
traceback2 is a backport of traceback to older supported Pythons.

traceback module is used to print or retrieve a stack traceback.

%description -n python3-traceback2 -l pl.UTF-8
traceback2 to backport modułu traceback do starszych wersji Pythona.

Moduł traceback służy do wypisywania i odtwarzania śladu wywołań ze
stosu.

%prep
%setup -q -n traceback2-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/traceback2/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/traceback2/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%dir %{py_sitescriptdir}/traceback2
%{py_sitescriptdir}/traceback2/*.py[co]
%{py_sitescriptdir}/traceback2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-traceback2
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%dir %{py3_sitescriptdir}/traceback2
%{py3_sitescriptdir}/traceback2/*.py
%{py3_sitescriptdir}/traceback2/__pycache__
%{py3_sitescriptdir}/traceback2-%{version}-py*.egg-info
%endif
