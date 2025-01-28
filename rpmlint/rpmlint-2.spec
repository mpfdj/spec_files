%{!?python3: %global python3 %{__python3}}

Name:           rpmlint
Version:        2.6.1
Release:        0%{?dist}
Summary:        Tool for checking common errors in RPM packages

License:        GPLv2+
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  hunspell-en

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  glibc-langpack-en
%endif

Requires:       /bin/bash
Requires:       /usr/bin/appstream-util
Requires:       /usr/bin/bzip2
Requires:       /usr/bin/checkbashisms
Requires:       /usr/bin/cpio
Requires:       /usr/bin/desktop-file-validate
Requires:       /usr/bin/groff
Requires:       /usr/bin/gtbl
Requires:       /usr/bin/ldd
Requires:       /usr/bin/man
Requires:       /usr/bin/perl
Requires:       /usr/bin/readelf
Requires:       /usr/bin/xz
Requires:       /usr/bin/zstd

# Enable Python dependency generation
%{?python_enable_dependency_generator}

%description
rpmlint is a tool for checking common errors in RPM packages. Binary and source packages as well as spec files can be checked.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


%files
%license COPYING
%doc README*
%{_bindir}/rpmlint
%{_bindir}/rpmdiff
%{python3_sitelib}/rpmlint*


%changelog
