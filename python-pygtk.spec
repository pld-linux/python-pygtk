#
# todo:
# 1. numpy? extensions?

%include	/usr/lib/rpm/macros.python

%define		module	pygtk

Summary:	Python bindings for Gtk+ 2.x libraries
Summary(pl):	Wi±zania Pythona do bibliotek Gtk+ 2.x
Name:		python-%{module}
Version:	1.99.17
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{module}/1.99/%{module}-%{version}.tar.bz2
# Source0-md5:	80c18a6153a16c4845b55beb34a452e0
Patch0:		%{name}-pyc.patch
URL:		http://www.daa.com.au/~james/software/pygtk/
%pyrequires_eq	python-modules
BuildRequires:	gtkglarea-devel >= 1.99.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Gtk+ 2.x libraries. This package contains
documentation and examples.

%description -l pl
Wi±zania Pythona do bibliotek Gtk+ 2.x. Pakiet zawiera dokumentacjê
oraz przyk³ady.

%package devel
Summary:	Python bindings for Gtk+ 2.x libraries - development files
Summary(pl):	Wi±zania Pythona do bibliotek Gtk+ 2.x - czê¶æ rozwojowa
Group:		Development/Languages/Python
Requires:	%{name}-atk = %{epoch}:%{version}
Requires:	%{name}-glade = %{epoch}:%{version}
Requires:	%{name}-gobject = %{epoch}:%{version}
Requires:	%{name}-gtk = %{epoch}:%{version}
Requires:	%{name}-pango = %{epoch}:%{version}
Obsoletes:	python-pygtk < 1:1.0

%description devel
This package contains files required to build wrappers for Gtk+ addon
libraries so that they interoperate with Python bindings.

%description devel -l pl
Pakiet zawiera pliki wymagane do zbudowania funkcji do bibliotek Gtk+,
tak by mog³y te biblioteki kooperowaæ z wi±zaniami Pythona.

%package gobject
Summary:	Python bindings for GObject library
Summary(pl):	Wi±zania Pythona do biblioteki GObject
Group:		Libraries/Python
%pyrequires_eq	python-modules
Conflicts:	python-pygtk < 1:1.0

%description gobject
Python bindings for GObject library.

%description gobject -l pl
Wi±zania Pythona do biblioteki GObject.

%package gtk
Summary:	Python bindings for Gtk+ library
Summary(pl):	Wi±zania Pythona do biblioteki Gtk+
Group:		Libraries/Python
Requires:	%{name}-atk = %{epoch}:%{version}
Requires:	%{name}-pango = %{epoch}:%{version}
Conflicts:	python-pygtk < 1:1.0

%description gtk
Python bindings for Gtk+ library.

%description gtk -l pl
Wi±zania Pythona do biblioteki Gtk+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl):	Wi±zania Pythona do biblioteki ATK
Group:		Libraries/Python
Requires:	%{name}-gobject = %{epoch}:%{version}

%description atk
Python bindings for ATK library.

%description atk -l pl
Wi±zania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl):	Wi±zania Pythona do biblioteki Pango
Group:		Libraries/Python
Requires:	%{name}-gobject = %{epoch}:%{version}

%description pango
Python bindings for Pango library.

%description pango -l pl
Wi±zania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl):	Wi±zania Pythona do biblioteki Glade
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}
Obsoletes:	python-pygtk-libglade < 1:1.0

%description glade
Python bindings for Glade library.

%description glade -l pl
Wi±zania Pythona do biblioteki Glade.

%package glarea
Summary:	Python bindings for GtkGLArea library
Summary(pl):	Wi±zania Pythona do biblioteki GtkGLArea
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}

%description glarea
Python bindings for GtkGLArea library.

%description glarea -l pl
Wi±zania Pythona do biblioteki GtkGLArea.

%prep
%setup  -q -n %{module}-%{version}
%patch0 -p1

%build
%configure \
	--enable-thread
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/{*.la,*/*.la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS MAPPING TODO THREADS AUTHORS
%{_examplesdir}/%{name}-%{version}

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

%files gobject
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0
%{py_sitedir}/pygtk.pth
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gobject*.so

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gtk
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk*.so
%{py_sitedir}/gtk-2.0/gtk/*.py[co]
%{py_sitedir}/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk*.so

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango*.so

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade*.so

%files glarea
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/gl.so
