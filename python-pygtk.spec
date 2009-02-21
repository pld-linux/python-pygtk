#
# Conditional build:
%bcond_without	numpy	# without numpy features
#
# todo: extensions?

%define		module	pygtk

Summary:	Python bindings for GTK+ 2.x libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek GTK+ 2.x
Name:		python-%{module}
Version:	2.14.0
Release:	1
Epoch:		2
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.14/%{module}-%{version}.tar.bz2
# Source0-md5:	b5fec3a9493a394d0ba2b8d2b337c4c5
Source1:	%{name}-python.m4
Source2:	%{name}-jhflags.m4
URL:		http://www.pygtk.org/
BuildRequires:	atk-devel >= 1:1.20.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtk+2-devel >= 2:2.13.0
BuildRequires:	libglade2-devel >= 1:2.6.0-4
BuildRequires:	libtool
BuildRequires:	pkgconfig
%{?with_numpy:BuildRequires:	python-Numeric-devel}
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	python-pycairo-devel >= 1.2.6
BuildRequires:	python-pygobject-devel >= 2.16.0
# needs /usr/share/doc/gtk-doc/html/pygobject/style.css
BuildRequires:	python-pygobject-apidocs
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GTK+ 2.x libraries. This package contains
documentation and examples.

%description -l pl.UTF-8
Wiązania Pythona do bibliotek GTK+ 2.x. Pakiet zawiera dokumentację
oraz przykłady.

%package devel
Summary:	Python bindings for GTK+ 2.x libraries - development files
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek GTK+ 2.x - część rozwojowa
Group:		Development/Languages/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-glade = %{epoch}:%{version}-%{release}
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	python-devel >= 1:2.3.2
Requires:	python-pygobject-devel >= 2.14.1
Obsoletes:	python-pygtk < 2:2.12.1-2

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with Python bindings.

%description devel -l pl.UTF-8
Pakiet zawiera pliki wymagane do zbudowania funkcji do bibliotek GTK+,
tak by mogły te biblioteki kooperować z wiązaniami Pythona.

%package examples
Summary:	Example programs for pygtk
Summary(pl.UTF-8):	Programy przykładowe do pygtk
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
This package contains example programs for pygtk.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla pygtk.

%package gtk
Summary:	Python bindings for GTK+ library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GTK+
Group:		Libraries/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	gtk+2 >= 2:2.12.0
Requires:	python-pycairo >= 1.2.3
Obsoletes:	python-pygtk-glarea
Conflicts:	python-pygtk < 1:1.0

%description gtk
Python bindings for GTK+ library.

%description gtk -l pl.UTF-8
Wiązania Pythona do biblioteki GTK+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki ATK
Group:		Libraries/Python
Requires:	atk >= 1:1.20.0
Requires:	python-pygobject >= 2.14.1

%description atk
Python bindings for ATK library.

%description atk -l pl.UTF-8
Wiązania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Pango
Group:		Libraries/Python
Requires:	pango >= 1:1.18.1
Requires:	python-pycairo >= 1.2.2
Requires:	python-pygobject >= 2.14.1

%description pango
Python bindings for Pango library.

%description pango -l pl.UTF-8
Wiązania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Glade
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	libglade2 >= 1:2.6.2
Obsoletes:	python-pygtk-libglade < 1:1.0

%description glade
Python bindings for Glade library.

%description glade -l pl.UTF-8
Wiązania Pythona do biblioteki Glade.

%package apidocs
Summary:	pygtk API documentation
Summary(pl.UTF-8):	Dokumentacja API pygtk
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygtk API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API pygtk.

%prep
%setup -q -n %{module}-%{version}

# don't remove it
#mkdir m4
#cp %{SOURCE1} m4/python.m4
#cp %{SOURCE2} m4/jhflags.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-thread \
	%{!?with_numpy:--disable-numeric}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	TARGET_DIR='%{_gtkdocdir}/%{name}'

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/{*.la,*/*.la}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/{*.py,*/*.py,*/*/*.py}
rm -f $RPM_BUILD_ROOT%{_datadir}/pygtk/2.0/codegen/*.py
rm -rf $RPM_BUILD_ROOT%{_libdir}/pygtk/2.0/{demos,pygtk-demo*}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pygtk-codegen-2.0
%attr(755,root,root) %{_bindir}/pygtk-demo
%dir %{_datadir}/pygtk
%dir %{_datadir}/pygtk/2.0
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_datadir}/pygtk/2.0/defs/*.override
%{_includedir}/pygtk-2.0
%{_pkgconfigdir}/pygtk-2.0.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gtk
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtkunixprint.so
%{py_sitedir}/gtk-2.0/gtk/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk.so

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pangocairo.so

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade.so

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
