
#
# todo:
# 1. numpy? extensions?
# 2. main package description - blah... blah... extensions and so on, read
#    README in .tar.gz
#

%include /usr/lib/rpm/macros.python
%define module pygtk

Summary:	Python bindings for Gtk+ libraries - development files
Summary(pl):	Wi±zania Pythona do bibliotek Gtk+ - czê¶æ rozwojowa
Name:		python-%{module}
Version:	1.99.7
Release:	0.2
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.gtk.org/pub/gtk/python/v1.3/%{module}-%{version}.tar.gz
URL:		http://daa.com.au/~james/pygtk
Requires:	%{name}-atk
Requires:	%{name}-glade
Requires:	%{name}-gobject
Requires:	%{name}-gtk
Requires:	%{name}-pango
%requires_eq    python-modules
BuildRequires:	libglade2-devel >= 1.99.9
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
N/A

%description -l pl
N/A

%package gobject
Summary:	Python bindings for GObject library
Summary(pl):	Wi±zania Pythona do biblioteki GObject
Group:		Development/Languages/Python

%description gobject
Python bindings for GObject library.

%description gobject -l pl
Wi±zania Pythona do biblioteki GObject.

%package gtk
Summary:	Python bindings for Gtk+ library
Summary(pl):	Wi±zania Pythona do biblioteki Gtk+
Group:		Development/Languages/Python
Requires:	%{name}-gobject = %{version}

%description gtk
Python bindings for Gtk+ library.

%description gtk -l pl
Wi±zania Pythona do biblioteki Gtk+.

%package atk
Summary:	Python bindings for ATK library
Summary(pl):	Wi±zania Pythona do biblioteki ATK
Group:		Development/Languages/Python
Requires:	%{name}-gobject = %{version}

%description atk
Python bindings for ATK library.

%description atk -l pl
Wi±zania Pythona do biblioteki ATK.

%package pango
Summary:	Python bindings for Pango library
Summary(pl):	Wi±zania Pythona do biblioteki Pango
Group:		Development/Languages/Python
Requires:	%{name}-gobject = %{version}

%description pango
Python bindings for Pango library.

%description pango -l pl
Wi±zania Pythona do biblioteki Pango.

%package glade
Summary:	Python bindings for Glade library
Summary(pl):	Wi±zania Pythona do biblioteki Glade
Group:		Development/Languages/Python
Requires:	%{name}-gtk = %{version}

%description glade
Python bindings for Glade library.

%description glade -l pl
Wi±zania Pythona do biblioteki Glade.

%prep
%setup  -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf README ChangeLog NEWS MAPPING TODO THREADS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_includedir}/pygtk-2.0

%dir %{_datadir}/%{module}
%dir %{_datadir}/%{module}/2.0
%dir %{_datadir}/%{module}/2.0/codegen
%{_datadir}/%{module}/2.0/codegen/*.py[co]

%{_datadir}/%{module}/2.0/defs

%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gobject*.so
%attr(755,root,root) %{py_sitedir}/gobject*.la

%files gtk
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk
%attr(755,root,root) %{py_sitedir}/gtk/_gtk*.so
%attr(755,root,root) %{py_sitedir}/gtk/_gtk*.la
%{py_sitedir}/gtk/*.py[co]

%files atk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/atk*.so
%attr(755,root,root) %{py_sitedir}/atk*.la

%files pango
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pango*.so
%attr(755,root,root) %{py_sitedir}/pango*.la

%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk/glade*.so
%attr(755,root,root) %{py_sitedir}/gtk/glade*.la
