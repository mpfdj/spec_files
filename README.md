# Some links on RPM Packaging
https://stackoverflow.com/questions/880227/what-is-the-minimum-i-have-to-do-to-create-an-rpm-file
https://opensource.com/article/18/9/how-build-rpm-packages
https://github.com/redhat-developer/rpm-packaging-guide/blob/master/source/hello-world.adoc

https://www.redhat.com/en/blog/create-rpm-package

https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/index
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/packaging-software_packaging-and-distributing-software#assembly_what-a-spec-file-is_packaging-software

https://docs.fedoraproject.org/en-US/docs/
https://docs.fedoraproject.org/en-US/packaging-guidelines/
https://docs.fedoraproject.org/en-US/packaging-guidelines/RPMMacros/

https://superuser.com/questions/1679368/beginner-rpm-about-install-and-rpmbuild-bb

https://koji.fedoraproject.org/


# Install packages
yum install rpmdevtools rpmbuild rpmlint

# Initialize rpmbuild environment
rpmdev-setuptree

# Create hello.sh and move to SOURCES
cat << EOF >> hello.sh
#!/bin/sh
echo "Hello world"
EOF

mkdir hello-0.0.1 && mv hello.sh hello-0.0.1
tar -zcf hello-0.0.1.tar.gz hello-0.0.1 && tar -ztvf hello-0.0.1.tar.gz
mv hello-0.0.1.tar.gz ~/rpmbuild/SOURCES

# Create an empty .spec file
rpmdev-newspec hello

# Lint .spec file
rpmlint hello.spec

# Evaluate a macro
rpm --eval %{_bindir}

# Build rpm
rpmbuild -ba ~/rpmbuild/SPECS/hello.spec

# List files
find ~/rpmbuild | sort

# Install package
yum localinstall ~/rpmbuild/RPMS/noarch/hello-0.0.1-1.el8.noarch.rpm

# Query package
rpm -qi hello
rpm -q hello --changelog
rpm -ql hello

# Run hello.sh
hello.sh



# https://github.com/rpm-software-management/rpmlint/issues/1162
# https://unix.stackexchange.com/questions/125120/why-is-dir-or-file-in-usr-local-an-error-rather-than-a-warning
# Customize rpmlint. Create below file and add filter
/root/.config/rpmlint
addFilter('invalid-url Source')
