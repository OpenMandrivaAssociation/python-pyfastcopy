Name:           python-pyfastcopy
Version:        1.0.3
Release:        3
Summary:        simple Python module that monkey patches the shutil.copyfile function of Python standard library to internally use the sendfile system call
License:        GPL
URL:            https://pypi.org/project/pyfastcopy/
Source:         https://files.pythonhosted.org/packages/43/80/535d6b3de415e26d0a1cb774c6895dd07aa5986d2f8bde200393bd916790/pyfastcopy-%{version}.tar.gz

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)

BuildArch:      noarch

%description
pyfastcopy is a simple Python module that monkey patches the shutil.copyfile function of Python standard library to internally use the sendfile system call.
It can provide important performance improvements for large file copy (typically 30-40%). See the performance section for some numbers.

%prep
%setup -q -n pyfastcopy-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/*
