
#
# todo:
# 1. libglade subpackage (needs libglade2)
# 2. descriptions and summaries
# 3. review subpackages content and dependencies (does gtk require atk
#    and pango modules? more?)
# 4. numpy?
#

%include /usr/lib/rpm/macros.python
%define module pygtk

Summary:	P
Summary(pl):	P
Name:		python-%{module}
Version:	1.99.7
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	%{module}-%{version}.tar.gz
URL:		http://daa.com.au/~james/pygtk
%requires_eq    python-modules
BuildRequires:	gtk+-devel
BuildRequires:	atk-devel
BuildRequires:	pango-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel
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
%dir %{_datadir}/%{module}/2.0/defs
%{_datadir}/%{module}/2.0/codegen/*.py[co]

%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gobject*.so
%attr(755,root,root) %{py_sitedir}/gobject*.la

%files gtk
%defattr(644,root,root,755)
%{_datadir}/%{module}/2.0/defs/gtk*
%{_datadir}/%{module}/2.0/defs/gdk*
%dir %{py_sitedir}/gtk
%attr(755,root,root) %{py_sitedir}/gtk/*.so
%attr(755,root,root) %{py_sitedir}/gtk/*.la
%{py_sitedir}/gtk/*.py[co]

%files atk
%defattr(644,root,root,755)
%{_datadir}/%{module}/2.0/defs/atk*
%attr(755,root,root) %{py_sitedir}/atk*.so
%attr(755,root,root) %{py_sitedir}/atk*.la

%files pango
%defattr(644,root,root,755)
%{_datadir}/%{module}/2.0/defs/pango*
%attr(755,root,root) %{py_sitedir}/pango*.so
%attr(755,root,root) %{py_sitedir}/pango*.la
