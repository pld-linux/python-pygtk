#
# Conditional build:
%bcond_without	numpy	# without numpy features
#
# todo: extensions?

%include	/usr/lib/rpm/macros.python

%define		module	pygtk

Summary:	Python bindings for Gtk+ 2.x libraries
Summary(pl):	Wi±zania Pythona do bibliotek Gtk+ 2.x
Name:		python-%{module}
Version:	2.2.0
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{module}/2.2/%{module}-%{version}.tar.bz2
# Source0-md5:	992122f8a61c266aeb1b7b35be9c4be1
Patch0:		%{name}-pyc.patch
URL:		http://www.daa.com.au/~james/software/pygtk/
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	python-devel >= 1:2.3.2
%{?with_numpy:BuildRequires:	python-numpy-devel}
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
%{?with_numpy:Requires:	python-numpy}
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
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-glade = %{epoch}:%{version}-%{release}
Requires:	%{name}-gobject = %{epoch}:%{version}-%{release}
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	python-devel >= 1:2.3.2
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
Obsoletes:	python-pygtk-glarea

%description gobject
Python bindings for GObject library.

%description gobject -l pl
Wi±zania Pythona do biblioteki GObject.

%package gtk
Summary:	Python bindings for Gtk+ library
Summary(pl):	Wi±zania Pythona do biblioteki Gtk+
Group:		Libraries/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Conflicts:	python-pygtk < 1:1.0

%description gtk
Python bindings for Gtk+ library.

%description gtk -l pl
Wi±zania Pythona do biblioteki Gtk+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl):	Wi±zania Pythona do biblioteki ATK
Group:		Libraries/Python
Requires:	%{name}-gobject = %{epoch}:%{version}-%{release}

%description atk
Python bindings for ATK library.

%description atk -l pl
Wi±zania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl):	Wi±zania Pythona do biblioteki Pango
Group:		Libraries/Python
Requires:	%{name}-gobject = %{epoch}:%{version}-%{release}

%description pango
Python bindings for Pango library.

%description pango -l pl
Wi±zania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl):	Wi±zania Pythona do biblioteki Glade
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Obsoletes:	python-pygtk-libglade < 1:1.0

%description glade
Python bindings for Glade library.

%description glade -l pl
Wi±zania Pythona do biblioteki Glade.

%prep
%setup  -q -n %{module}-%{version}
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-thread \
	%{!?with_numpy:--disable-numpy}

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
%{py_sitedir}/gtk-2.0/*.py[co]
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
