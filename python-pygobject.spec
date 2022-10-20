# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pygobject
Epoch: 100
Version: 3.40.1
Release: 1%{?dist}
Summary: Python bindings for GObject Introspection
License: LGPL-2.1-or-later
URL: https://github.com/GNOME/pygobject/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cairo-gobject-devel
BuildRequires: fdupes
BuildRequires: glib2-devel >= 2.56.0
BuildRequires: gobject-introspection-devel >= 1.56.0
BuildRequires: libffi-devel >= 3.0
BuildRequires: python-rpm-macros
BuildRequires: python3-cairo >= 1.16.0
BuildRequires: python3-cairo-devel >= 1.16.0
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
PyGObject is a Python package which provides bindings for GObject based
libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
export CFLAGS="%{optflags}"
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-gobject
Summary: Python bindings for GObject Introspection
Requires: python3
Provides: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gobject
PyGObject is a Python package which provides bindings for GObject based
libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more.

%package -n python%{python3_version_nodots}-gobject-Gdk
Summary: Python bindings for GObject/Gdk
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3-gobject-Gdk = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-Gdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-Gdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-Gdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-Gdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-Gdk) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gobject-Gdk
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

%package -n python%{python3_version_nodots}-gobject-cairo
Summary: Python bindings for GObject/Cairo
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3-gobject-cairo = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-cairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-cairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-cairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-cairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-cairo) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gobject-cairo
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

%package -n python%{python3_version_nodots}-gobject-devel
Summary: Metapackage to pull in all of python-gobject's packages
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Requires: python3-gobject-Gdk = %{epoch}:%{version}-%{release}
Requires: python3-gobject-cairo = %{epoch}:%{version}-%{release}
Requires: python3-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python3-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-devel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gobject-devel
This package contains files required to build wrappers for gobject
addon libraries such as pygtk.

%package -n python%{python3_version_nodots}-gobject-common-devel
Summary: Shared development files for GObject's Python bindings
Requires: python3
Provides: python3-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-common-devel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gobject-common-devel
This package contains common files required to build wrappers for gobject
addon libraries such as pygtk in both Python2 and Python3.

%files -n python%{python3_version_nodots}-gobject
%license COPYING
%{python3_sitearch}/*
%exclude %{python3_sitearch}/gi/_gi_cairo*.so
%exclude %{python3_sitearch}/gi/_gtktemplate.py
%exclude %{python3_sitearch}/gi/overrides/Gdk.*
%exclude %{python3_sitearch}/gi/overrides/GdkPixbuf.py
%exclude %{python3_sitearch}/gi/overrides/Gtk.*
%exclude %{python3_sitearch}/gi/overrides/keysyms.*
%exclude %{python3_sitearch}/gi/overrides/Pango.*

%files -n python%{python3_version_nodots}-gobject-Gdk
%{python3_sitearch}/gi/_gtktemplate.py
%{python3_sitearch}/gi/overrides/Gdk.*
%{python3_sitearch}/gi/overrides/GdkPixbuf.py
%{python3_sitearch}/gi/overrides/Gtk.*
%{python3_sitearch}/gi/overrides/keysyms.*
%{python3_sitearch}/gi/overrides/Pango.*

%files -n python%{python3_version_nodots}-gobject-cairo
%{python3_sitearch}/gi/_gi_cairo*.so

%files -n python%{python3_version_nodots}-gobject-devel
%doc README.rst

%files -n python%{python3_version_nodots}-gobject-common-devel
%{_includedir}/pygobject-3.0/
%{_libdir}/pkgconfig/pygobject-3.0.pc
%endif

%if 0%{?sle_version} > 150000
%package -n python3-gobject
Summary: Python bindings for GObject Introspection
Requires: python3
Provides: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject) = %{epoch}:%{version}-%{release}

%description -n python3-gobject
PyGObject is a Python package which provides bindings for GObject based
libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more.

%package -n python3-gobject-Gdk
Summary: Python bindings for GObject/Gdk
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3-gobject-Gdk = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-Gdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-Gdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-Gdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-Gdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-Gdk) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-Gdk
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

%package -n python3-gobject-cairo
Summary: Python bindings for GObject/Cairo
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3-gobject-cairo = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-cairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-cairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-cairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-cairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-cairo) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-cairo
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

%package -n python3-gobject-devel
Summary: Metapackage to pull in all of python-gobject's packages
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Requires: python3-gobject-Gdk = %{epoch}:%{version}-%{release}
Requires: python3-gobject-cairo = %{epoch}:%{version}-%{release}
Requires: python3-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python3-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-devel) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-devel
This package contains files required to build wrappers for gobject
addon libraries such as pygtk.

%package -n python3-gobject-common-devel
Summary: Shared development files for GObject's Python bindings
Requires: python3
Provides: python3-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-common-devel) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-common-devel
This package contains common files required to build wrappers for gobject
addon libraries such as pygtk in both Python2 and Python3.

%files -n python3-gobject
%license COPYING
%{python3_sitearch}/*
%exclude %{python3_sitearch}/gi/_gi_cairo*.so
%exclude %{python3_sitearch}/gi/_gtktemplate.py
%exclude %{python3_sitearch}/gi/overrides/Gdk.*
%exclude %{python3_sitearch}/gi/overrides/GdkPixbuf.py
%exclude %{python3_sitearch}/gi/overrides/Gtk.*
%exclude %{python3_sitearch}/gi/overrides/keysyms.*
%exclude %{python3_sitearch}/gi/overrides/Pango.*

%files -n python3-gobject-Gdk
%{python3_sitearch}/gi/_gtktemplate.py
%{python3_sitearch}/gi/overrides/Gdk.*
%{python3_sitearch}/gi/overrides/GdkPixbuf.py
%{python3_sitearch}/gi/overrides/Gtk.*
%{python3_sitearch}/gi/overrides/keysyms.*
%{python3_sitearch}/gi/overrides/Pango.*

%files -n python3-gobject-cairo
%{python3_sitearch}/gi/_gi_cairo*.so

%files -n python3-gobject-devel
%doc README.rst

%files -n python3-gobject-common-devel
%{_includedir}/pygobject-3.0/
%{_libdir}/pkgconfig/pygobject-3.0.pc
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-gobject
Summary: Python bindings for GObject Introspection
Requires: python3
Requires: python3-gobject-base = %{epoch}:%{version}-%{release}
Requires: python3-cairo >= 1.16.0
Provides: python3-gobject = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject) = %{epoch}:%{version}-%{release}

%description -n python3-gobject
PyGObject is a Python package which provides bindings for GObject based
libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more.

%package -n python3-gobject-base
Summary: Python bindings for GObject Introspection base package
Requires: python3
Requires: gobject-introspection >= 1.56.0
Requires: python3-gobject-base-noarch = %{epoch}:%{version}-%{release}
Provides: python3-gobject-base = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-base) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-base = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-base) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-base = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-base) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-base
This package provides the non-cairo specific bits of the GObject
Introspection library.

%package -n python3-gobject-base-noarch
Summary: Python bindings for GObject Introspection base package (not architecture dependent)
BuildArch: noarch
Requires: python3
Requires: gobject-introspection >= 1.56.0
Provides: python3-gobject-base-noarch = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-base-noarch) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-base-noarch = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-base-noarch) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-base-noarch = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-base-noarch) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-base-noarch
This package provides the non-cairo specific bits of the GObject
Introspection library that are not architecture specific.

%package -n python3-gobject-devel
Summary: Development files for embedding PyGObject introspection support
Requires: gobject-introspection-devel
Requires: python3
Requires: python3-gobject = %{epoch}:%{version}-%{release}
Requires: python3-gobject-devel-base = %{epoch}:%{version}-%{release}
Provides: python3-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(gobject-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gobject-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gobject-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gobject-devel) = %{epoch}:%{version}-%{release}

%description -n python3-gobject-devel
This package contains files required to embed PyGObject.

%files -n python3-gobject
%{python3_sitearch}/gi/_gi_cairo*.so

%files -n python3-gobject-base
%license COPYING
%{python3_sitearch}/*
%exclude %{python3_sitearch}/gi/_gi_cairo*.so
%exclude %{python3_sitearch}/gi/overrides
%exclude %{python3_sitearch}/gi/repository
%exclude %{python3_sitearch}/pygtkcompat

%files -n python3-gobject-base-noarch
%license COPYING
%dir %{python3_sitearch}/gi
%{python3_sitearch}/gi/overrides
%{python3_sitearch}/gi/repository
%{python3_sitearch}/pygtkcompat

%files -n python3-gobject-devel
%dir %{_includedir}/pygobject-3.0/
%{_includedir}/pygobject-3.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-3.0.pc
%endif

%changelog
