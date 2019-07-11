Name: gxml
Version: 0.18.1
Release: 1

Summary: GXml provides a GObject API for manipulating XML
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/GXml

Source0: https://download.gnome.org/sources/gxml/0.18/%{name}-%{version}.tar.xz

BuildRequires: libgio-devel
BuildRequires: libgee0.8-devel
BuildRequires: libxml2-devel
BuildRequires: libvala-devel 
BuildRequires: gobject-introspection-devel 
BuildRequires: libgee0.8-gir-devel
BuildRequires: intltool 
BuildRequires: gtk-doc
BuildRequires: valadoc 
BuildRequires: yelp-tools 
BuildRequires: graphviz

%description
GXml provides a GObject API for manipulating XML. Most functionality
is provided through libxml2. Currently, GXml provides the DOM Level 1
Core API.

%package devel
Summary: Development files for GXml
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using GXml.

%package gir
Summary: GObject introspection data for the GXml library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GXml library

%package gir-devel
Summary: GObject introspection devel data for the GXml library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GXml library.

%package devel-doc
Summary: Development documentation for GXml
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for GXml library.

%prep
%setup -n %_name-%version
# to avoid "/usr/lib/rpm/debugedit: canonicalization unexpectedly shrank by one character" bug
find ./ -type f -print0| xargs -r0 subst 's|gxml//xlibxml.h|gxml/xlibxml.h|' --

%build
%autoreconf
%configure --disable-static \
	%{subst_enable docs}
%make_build

%install
%makeinstall_std

%check
%make check

%find_lang --output=%_name.lang %_name GXml

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%files gir
%_typelibdir/GXml-%api_ver.typelib

%files gir-devel
%_girdir/GXml-%api_ver.gir

%if_enabled docs
%files devel-doc
#%_datadir/gtk-doc/html/%_name/
%_datadir/devhelp/books/GXml-%api_ver/
%endif
