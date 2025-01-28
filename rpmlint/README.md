# rpmlint sources
https://src.fedoraproject.org/rpms/rpmlint
https://github.com/rpm-software-management/rpmlint/releases


# Enable rockylinux repos
cp rockylinux.repo /etc/yum.repos.d
yum clean all
yum repolist all


# Packages which are required for the Python build
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install rpmdevtools
yum install python3-devel
yum install libappstream-glib
yum install desktop-file-utils
yum install pyproject-rpm-macros
python3.12 -m pip install --target /usr/lib/python3.12/site-packages wheel


# Initialize rpmbuild folder
cd ~
rm -rf rpmbuild
rpmdev-setuptree

cp /tmp/ansible/builds/rpmlint-2.6.1/rpmlint.spec ~/rpmbuild/SPECS
cp /tmp/ansible/builds/rpmlint-2.6.1/rpmlint-2.6.1.tar.gz /tmp/ansible/builds/rpmlint-2.6.1/*.toml ~/rpmbuild/SOURCES


# Make sure we use unix format
dos2unix ~/rpmbuild/SPECS/rpmlint.spec


# Build the rpm
rpmbuild -ba --noprep --noclean --target noarch --nocheck -vv rpmlint.spec


# Install rpm
cd /root/rpmbuild/RPMS/noarch
yum localinstall *.rpm


# Install missing pip modules
python3.12 -m pip install --target /usr/lib/python3.12/site-packages file-magic packaging pyenchant pyxdg rpm zstandard tomli-w


# Run rpmlint
cd /root/rpmbuild/SPECS
rpmlint rpmlint.spec
