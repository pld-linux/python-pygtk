%define module pygtk
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	GTK+ interface for Python language
Summary(pl):	Interfejs GTK+ dla jêzyka Python
Name:		python-%{module}
Version:	0.6.6
Release:	4
License:	LGPL
Group:		Development/Languages/Python
Group(pl):	Programowanie/Jêzyki/Python
Source:		%{module}-%{version}.tar.gz
Requires:	python >= 1.5, gtk+ >= 1.2.6, imlib >= 1.8
BuildRequires:	python-devel >= 1.5, gtk+-devel >= 1.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This archive contains modules that allow you to use gtk+ in Python
programs.

%description -l pl
Pakiet ten zawiera modu³y dla jêzyka Python umo¿liwiaj±ce tworzenie
programów z u¿yciem biblioteki GTK+.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make} OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pyexecdir=%{python_sitepkgsdir}/%{module} \
	pthondir=%{python_sitepkgsdir}/%{module}
	
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
mv examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

mv $RPM_BUILD_ROOT%{python_sitepkgsdir}/*.py* \
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
%attr(-,root,root) %{_prefix}/src/examples/%{name}
