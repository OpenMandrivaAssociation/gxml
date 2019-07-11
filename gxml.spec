%define api 0.18

%define libname	%mklibname gxml %{api}
%define girname	%mklibname gxml-gir
%define devname %mklibname -d gxml

Name: gxml
Version: 0.18.1
Release: 1

Summary: GXml provides a GObject API for manipulating XML
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/GXml

Source0: https://download.gnome.org/sources/gxml/%{api}/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(vapigen)
BuildRequires: pkgconfig(gobject-introspection-1.0) 
BuildRequires: typelib(Gee)
BuildRequires: intltool 
BuildRequires: gtk-doc
BuildRequires: vala-tools
BuildRequires: yelp-tools 
BuildRequires: graphviz
BuildRequires: meson

%description
GXml provides a GObject API for manipulating XML. Most functionality
is provided through libxml2. Currently, GXml provides the DOM Level 1
Core API.

%package -n %{libname}
Group:		System/Libraries
Summary:	GXml library
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
This is a library for GXml.


%package -n %{devname}
Summary: Development files for GXml
Group: Development/C
Requires: %name = %version-%release
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files needed for
development using GXml.

%package -n %{girname}
Summary: GObject introspection data for the GXml library
Group: System/Libraries
Requires: %name = %version-%release

%description -n %{girname}
GObject introspection data for the GXml library

%package devel-doc
Summary: Development documentation for GXml
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for GXml library.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang --output=%_name.lang %_name GXml

%files -f %_name.lang
%doc AUTHORS NEWS README

%files -n %{libname}
%_libdir/%name-%api_ver.so.*

%files -n %{devname}
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi
%_girdir/GXml-%api_ver.gir

%files -n %{girname}
%_typelibdir/GXml-%api_ver.typelib

%files devel-doc
#%_datadir/gtk-doc/html/%_name/
%_datadir/devhelp/books/GXml-%api_ver/
