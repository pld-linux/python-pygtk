#
# todo:
# 1. numpy? extensions?
# 2. gtkgl module

%include	/usr/lib/rpm/macros.python

%define		module	pygtk

Summary:	Python bindings for Gtk+ 2.x libraries
Summary(pl):	Wi±zania Pythona do bibliotek Gtk+ 2.x
Name:		python-%{module}
Version:	1.99.13
Release:	3
License:	LGPL
Group:		Libraries/Python
Source0:	ftp://ftp.gtk.org/pub/gtk/python/v2.0/%{module}-%{version}.tar.gz
Patch0:		%{name}-pyc.patch
URL:		http://daa.com.au/~james/pygtk
%pyrequires_eq	python-modules
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Gtk+ 2.x libraries. This package contains documentation
and examples.

%description -l pl
Wi±zania Pythona do bibliotek Gtk+ 2.x. Ten pakiet zawiera dokumentacjê
oraz przyk³ady.

%package devel
Summary:	Python bindings for Gtk+ 2.x libraries - development files
Summary(pl):	Wi±zania Pythona do bibliotek Gtk+ 2.x - czê¶æ rozwojowa
Group:		Development/Languages/Python
Requires:	%{name}-atk = %{version}
Requires:	%{name}-glade = %{version}
Requires:	%{name}-gobject = %{version}
Requires:	%{name}-gtk = %{version}
Requires:	%{name}-pango = %{version}

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

%description gobject
Python bindings for GObject library.

%description gobject -l pl
Wi±zania Pythona do biblioteki GObject.

%package gtk
Summary:	Python bindings for Gtk+ library
Summary(pl):	Wi±zania Pythona do biblioteki Gtk+
Group:		Libraries/Python
Requires:	%{name}-gobject = %{version}
Conflicts:	%{name} < 1.0

%description gtk
Python bindings for Gtk+ library.

%description gtk -l pl
Wi±zania Pythona do biblioteki Gtk+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl):	Wi±zania Pythona do biblioteki ATK
Group:		Libraries/Python
Requires:	%{name}-gobject = %{version}

%description atk
Python bindings for ATK library.

%description atk -l pl
Wi±zania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl):	Wi±zania Pythona do biblioteki Pango
Group:		Libraries/Python
Requires:	%{name}-gobject = %{version}

%description pango
Python bindings for Pango library.

%description pango -l pl
Wi±zania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl):	Wi±zania Pythona do biblioteki Glade
Group:		Libraries/Python
Requires:	%{name}-gtk = %{version}

%description glade
Python bindings for Glade library.

%description glade -l pl
Wi±zania Pythona do biblioteki Glade.

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS MAPPING TODO THREADS AUTHORS
%{_examplesdir}/%{name}

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
%{py_sitedir}/pygtk.pth
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gobject*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gobject*.la

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/*.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk*.la
%{py_sitedir}/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk*.la

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango*.la

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade*.la
