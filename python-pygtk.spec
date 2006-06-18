#
# Conditional build:
%bcond_without	numpy	# without numpy features
#
# todo: extensions?

%define		module	pygtk

Summary:	Python bindings for GTK+ 2.x libraries
Summary(pl):	Wi±zania Pythona do bibliotek GTK+ 2.x
Name:		python-%{module}
Version:	2.9.2
Release:	1
Epoch:		2
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/gnome/sources/pygtk/2.9/%{module}-%{version}.tar.bz2
# Source0-md5:	2625ddd1aba04869eb2f9e4d4cc5552b
Source1:	%{name}-python.m4
Source2:	%{name}-jhflags.m4
Patch0:		%{name}-pyc.patch
URL:		http://www.pygtk.org/
BuildRequires:	atk-devel >= 1:1.11.4
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.9.3
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.13.2
BuildRequires:	python-devel >= 1:2.3.2
%{?with_numpy:BuildRequires:	python-numpy-devel}
BuildRequires:	python-pycairo-devel >= 1.1.6
BuildRequires:	python-pygobject-devel >= 2.10.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GTK+ 2.x libraries. This package contains
documentation and examples.

%description -l pl
Wi±zania Pythona do bibliotek GTK+ 2.x. Pakiet zawiera dokumentacjê
oraz przyk³ady.

%package devel
Summary:	Python bindings for GTK+ 2.x libraries - development files
Summary(pl):	Wi±zania Pythona do bibliotek GTK+ 2.x - czê¶æ rozwojowa
Group:		Development/Languages/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-glade = %{epoch}:%{version}-%{release}
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.9.3
Requires:	python-devel >= 1:2.3.2
Requires:	python-pygobject-devel >= 2.10.1
Obsoletes:	python-pygtk < 1:1.0

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with Python bindings.

%description devel -l pl
Pakiet zawiera pliki wymagane do zbudowania funkcji do bibliotek GTK+,
tak by mog³y te biblioteki kooperowaæ z wi±zaniami Pythona.

%package examples
Summary:	Example programs for pygtk
Summary(pl):	Programy przyk³adowe do pygtk
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	python-pygtk

%description examples
This package contains example programs for pygtk.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy dla pygtk.

%package gtk
Summary:	Python bindings for GTK+ library
Summary(pl):	Wi±zania Pythona do biblioteki GTK+
Group:		Libraries/Python
Requires:	%{name}-atk = %{epoch}:%{version}-%{release}
Requires:	%{name}-pango = %{epoch}:%{version}-%{release}
Requires:	gtk+2 >= 2:2.9.2
Requires:	python-pycairo >= 1.1.6
Conflicts:	python-pygtk < 1:1.0
Obsoletes:	python-pygtk-glarea

%description gtk
Python bindings for GTK+ library.

%description gtk -l pl
Wi±zania Pythona do biblioteki GTK+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl):	Wi±zania Pythona do biblioteki ATK
Group:		Libraries/Python
Requires:	python-pygobject >= 2.10.1
Requires:	atk >= 1:1.11.4

%description atk
Python bindings for ATK library.

%description atk -l pl
Wi±zania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl):	Wi±zania Pythona do biblioteki Pango
Group:		Libraries/Python
Requires:	pango >= 1:1.13.1
Requires:	python-pycairo >= 1.1.6
Requires:	python-pygobject >= 2.10.1

%description pango
Python bindings for Pango library.

%description pango -l pl
Wi±zania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl):	Wi±zania Pythona do biblioteki Glade
Group:		Libraries/Python
Requires:	%{name}-gtk = %{epoch}:%{version}-%{release}
Requires:	libglade2 >= 1:2.5.1
Obsoletes:	python-pygtk-libglade < 1:1.0

%description glade
Python bindings for Glade library.

%description glade -l pl
Wi±zania Pythona do biblioteki Glade.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

# don't remove it
mkdir m4
cp %{SOURCE1} m4/python.m4
cp %{SOURCE2} m4/jhflags.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/{*.la,*/*.la}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/{*.py,*/*.py,*/*/*.py}
rm -f $RPM_BUILD_ROOT%{_datadir}/pygtk/2.0/codegen/*.py
rm -rf $RPM_BUILD_ROOT%{_libdir}/pygtk/2.0/{demos,pygtk-demo*}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{module}
%dir %{_datadir}/%{module}/2.0
%dir %{_datadir}/%{module}/2.0/codegen
%{_datadir}/%{module}/2.0/codegen/*.py[co]
%{_datadir}/%{module}/2.0/defs
%{_includedir}/pygtk-2.0
%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/gtk
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/_gtk*.so
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/unixprint.so
%{py_sitedir}/gtk-2.0/gtk/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atk*.so

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pango*.so

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/glade*.so
