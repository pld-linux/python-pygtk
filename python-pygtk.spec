%define module pygtk
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	GTK+ interface for Python language
Summary(pl):	Interfejs GTK+ dla j�zyka Python
Name:		python-%{module}
Version:	0.6.8
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Source0:	http://freshmeat.net/redir/pygtk/8536/url_tgz/%{module}-%{version}.tar.gz
Requires:	python >= 1.5, gtk+ >= 1.2.6, imlib >= 1.8
BuildRequires:	python-devel >= 1.5, gtk+-devel >= 1.2.6
Provides:	pygtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This archive contains modules that allow you to use gtk+ in Python
programs.

%description -l pl
Pakiet ten zawiera modu�y dla j�zyka Python umo�liwiaj�ce tworzenie
program�w z u�yciem biblioteki GTK+.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pyexecdir=%{python_sitepkgsdir}/%{module} \
	pthondir=%{python_sitepkgsdir}/%{module}
	
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
mv -f examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

mv -f $RPM_BUILD_ROOT%{python_sitepkgsdir}/*.py* \
	$RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}

echo %{module} > $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}.pth
echo pyglade > $RPM_BUILD_ROOT%{python_sitepkgsdir}/pyglade.pth

gzip -9nf COPYING ChangeLog README MAPPING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,MAPPING}.gz
%{python_sitepkgsdir}/%{module}.pth
%{python_sitepkgsdir}/%{module}
%{python_sitepkgsdir}/pyglade.pth
%{python_sitepkgsdir}/pyglade
%{_includedir}/%{module}/
%attr(-,root,root) %{_examplesdir}/%{name}
