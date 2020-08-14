Summary: lua-openssl package
Name: lua-openssl
Version: %{version}
Release: %{release}
License: GPLv2

BuildRequires: gcc gcc-c++
BuildRequires: make automake cmake3 autoconf zlib-devel zlib
BuildRequires: openssl-devel openssl
BuildRequires: luajit-devel luajit

Requires: luajit openssl zlib


%description
Openssl module for luajit

%build
cmake3 -Bbuild -H. -DOPENSSL_ROOT_DIR=/usr/lib64/ && cd build && make

%install
cd build && make DESTDIR="/usr/local/lib/lua/5.1/" install
ls -lah %{buildroot}
pwd
ls -lah

%files
/usr/local/lib/lua/5.1/openssl.so
/usr/local/lib/lua/5.1/openssl.so.1
/usr/local/lib/lua/5.1/openssl.so.0.7.8.0
