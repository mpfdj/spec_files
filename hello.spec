# https://www.redhat.com/en/blog/create-rpm-package

Name:           hello
Version:        0.0.1
Release:        1%{?dist}
Summary:        A simple hello world script
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
A demo RPM build


%prep
#----------------------------------------------------------------------------------------------------------------------
# The prep section, short for prepare, defines the commands necessary to prepare for the build.
# If you are starting with a compressed tar archive (a tarball) of the sources, the prep section needs to extract the sources.
#
# This section describes how to build packages with source code tarballs using different variants of the setup macro.
# The -q option limits the verbosity of the setup macro. Only tar -xof is executed instead of tar -xvvof. Use this option as the first option.

# The setup macro is used to unpack the original sources, in preparation for the
# build. In its simplest form, the macro is used with no options and gets the name
# of the source archive from the source tag specified earlier in the spec file.
#----------------------------------------------------------------------------------------------------------------------
%setup -q


%build
# Not applicable


# -------------------------------------------------------------------------------------
# The install section doesn't run when .rpm is installed. It runs during build of RPM. It's a phase of the build rather.
# In there you have commands which install files to the $RPM_BUILD_ROOT which is more or a less a temporary directory where you install the files during build.
#-------------------------------------------------------------------------------------
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
cp %{name}.sh %{buildroot}/%{_bindir}


%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------------------------------
# Subsequently, you have the files section where you list the files to be packaged into the actual .rpm.
# Those files are the ones installed to the RPM build root in the install phase.
#-------------------------------------------------------------------------------------------------------
%files
%{_bindir}/%{name}.sh


%post
chmod a+x %{_bindir}/%{name}.sh


%changelog
* Fri Jan 24 2025 Miel de Jaeger <mpf.dejaeger@gmail.com> - 0.0.1
- First version being packaged
