
#
# todo:
# 1. descriptions and summaries
# 2. numpy? extensions?
#

%include /usr/lib/rpm/macros.python
%define module pygtk

Summary:	P
Summary(pl):	P
Name:		python-%{module}
Version:	1.99.7
Release:	0.2
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.gtk.org/pub/gtk/python/v1.3/%{module}-%{version}.tar.gz
URL:		http://daa.com.au/~james/pygtk
%requires_eq    python-modules
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 1.99.9
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
N/A

%description -l pl
N/A

%package gobject
Summary:	GObject
Summary(pl):	GObject
Group:		Development/Languages/Python

%description gobject
N/A

%description gobject -l pl
N/A

%package gtk
Summary:	GTK
Summary(pl):	GTK
Group:		Development/Languages/Python
Requires:	%{name}-gobject = %{version}

%description gtk
N/A

%description gtk -l pl
N/A

%package atk
Summary:	atk
Summary(pl):	atk
Group:		Development/Languages/Python
Requires:	%{name}-gobject = %{version}

%description atk
N/A

%description atk -l pl
N/A

%package pango
Summary:	pango
Summary(pl):	pango
Group:		Development/Languages/Python
Requires:	%{name}-gobject = %{version}

%description pango
N/A

%description pango -l pl
N/A

%package glade
Summary:	glade
Summary(pl):	glade
Group:		Development/Languages/Python
Requires:	%{name}-gtk = %{version}

%description glade
N/A

%description glade -l pl
N/A

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
