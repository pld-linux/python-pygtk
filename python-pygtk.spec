#
# Conditional build:
%bcond_without	numpy	# without numpy features
#
# todo: extensions?

%define		module	pygtk

Summary:	Python bindings for GTK+ 2.x libraries
Summary(pl):	Wi�zania Pythona do bibliotek GTK+ 2.x
Name:		python-%{module}
Version:	2.3.96
Release:	1
Epoch:		2
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{module}/2.3/%{module}-%{version}.tar.bz2
# Source0-md5:	f5fcace74a398a5fac12f76592c405bb
Patch0:		%{name}-pyc.patch
URL:		http://www.pygtk.org/
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	python-devel >= 1:2.3.2
%{?with_numpy:BuildRequires:	python-numpy-devel}
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GTK+ 2.x libraries. This package contains
documentation and examples.

%description -l pl
Wi�zania Pythona do bibliotek GTK+ 2.x. Pakiet zawiera dokumentacj�
oraz przyk�ady.

%package devel
Summary:	Python bindings for GTK+ 2.x libraries - development files
Summary(pl):	Wi�zania Pythona do bibliotek GTK+ 2.x - cz�� rozwojowa
Group:		Development/Languages/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-glade = %{epoch}:%{version}-%{release}
Requires:	%{name}-gobject = %{epoch}:%{version}-%{release}
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	python-devel >= 1:2.3.2
Obsoletes:	python-pygtk < 1:1.0

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with Python bindings.

%description devel -l pl
Pakiet zawiera pliki wymagane do zbudowania funkcji do bibliotek GTK+,
tak by mog�y te biblioteki kooperowa� z wi�zaniami Pythona.

%package examples
Summary:	Example programs for pygtk
Summary(pl):	Programy przyk�adowe do pygtk
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	python-pygtk < 1:1.0

%description examples
This package contains example programs for pygtk.

%description examples -l pl
Ten pakiet zawiera przyk�adowe programy dla pygtk.

%package gobject
Summary:	Python bindings for GObject library
Summary(pl):	Wi�zania Pythona do biblioteki GObject
Group:		Libraries/Python
%pyrequires_eq	python-modules
Requires:	glib2 >= 1:2.4.4
Conflicts:	python-pygtk < 1:1.0
Obsoletes:	python-pygtk-glarea

%description gobject
Python bindings for GObject library.

%description gobject -l pl
Wi�zania Pythona do biblioteki GObject.

%package gtk
Summary:	Python bindings for GTK+ library
Summary(pl):	Wi�zania Pythona do biblioteki GTK+
Group:		Libraries/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	gtk+2 >= 2:2.4.4
Conflicts:	python-pygtk < 1:1.0
Obsoletes:	python-pygtk-glarea

%description gtk
Python bindings for GTK+ library.

%description gtk -l pl
Wi�zania Pythona do biblioteki GTK+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl):	Wi�zania Pythona do biblioteki ATK
Group:		Libraries/Python
Requires:	%{name}-gobject = %{epoch}:%{version}-%{release}
Requires:	atk >= 1.0.0

%description atk
Python bindings for ATK library.

%description atk -l pl
Wi�zania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl):	Wi�zania Pythona do biblioteki Pango
Group:		Libraries/Python
Requires:	%{name}-gobject = %{epoch}:%{version}-%{release}
Requires:	pango >= 1.0.0

%description pango
Python bindings for Pango library.

%description pango -l pl
Wi�zania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl):	Wi�zania Pythona do biblioteki Glade
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	libglade2 >= 1:2.4.0
Obsoletes:	python-pygtk-libglade < 1:1.0

%description glade
Python bindings for Glade library.

%description glade -l pl
Wi�zania Pythona do biblioteki Glade.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--enable-thread \
	%{!?with_numpy:--disable-numpy}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# handle the py_sitescriptdir/py_sitedir package split
cp $RPM_BUILD_ROOT%{py_sitedir}/pygtk.pth $RPM_BUILD_ROOT%{py_sitescriptdir}
touch $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/__init__.py
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/
rm $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/__init__.py

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/{*.la,*/*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/pygtk-2.0

%dir %{_datadir}/%{module}
%dir %{_datadir}/%{module}/2.0
%dir %{_datadir}/%{module}/2.0/codegen
%{_datadir}/%{module}/2.0/codegen/*.py[co]

%{_datadir}/%{module}/2.0/defs

%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files gobject
%defattr(644,root,root,755)
%doc README ChangeLog NEWS MAPPING TODO THREADS AUTHORS
%dir %{py_sitedir}/gtk-2.0
%{py_sitescriptdir}/pygtk.pth
%{py_sitedir}/pygtk.pth
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gobject*.so

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gtk
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk*.so
%{py_sitedir}/gtk-2.0/gtk/*.py[co]
%{py_sitescriptdir}/gtk-2.0/gtk/*.py[co]
%{py_sitescriptdir}/gtk-2.0/*.py[co]
%{py_sitescriptdir}/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk*.so

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango*.so

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade*.so
