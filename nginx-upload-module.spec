#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nginx-upload-module
Version  : 2.3.0
Release  : 21
URL      : https://github.com/fdintino/nginx-upload-module/archive/2.3.0.tar.gz
Source0  : https://github.com/fdintino/nginx-upload-module/archive/2.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nginx-upload-module-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev

%description
# nginx-upload-module
[![Build Status](https://travis-ci.org/fdintino/nginx-upload-module.svg?branch=master)](https://travis-ci.org/fdintino/nginx-upload-module)

%package lib
Summary: lib components for the nginx-upload-module package.
Group: Libraries

%description lib
lib components for the nginx-upload-module package.


%prep
%setup -q -n nginx-upload-module-2.3.0
cd %{_builddir}/nginx-upload-module-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_upload_module.so
