%define module pygtk
%define pver 1.6

Summary:	GTK+ interface for Python language
Summary(pl):	Interfejs GTK+ dla jêzyka Python
Name:		python-%{module}
Version:	0.6.6
Release:	3
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

install -d $RPM_BUILD_ROOT%{_libdir}/python%{pver}/site-packages/%{module}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pyexecdir=%{_libdir}/python%{pver}/site-packages/%{module} \
	pthondir=%{_libdir}/python%{pver}/site-packages/%{module}
	
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}
mv examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

mv $RPM_BUILD_ROOT%{_libdir}/python%{pver}/site-packages/*.py* \
	$RPM_BUILD_ROOT%{_libdir}/python%{pver}/site-packages/%{module}

echo %{module} > $RPM_BUILD_ROOT%{_libdir}/python%{pver}/site-packages/%{module}.pth
echo pyglade > $RPM_BUILD_ROOT%{_libdir}/python%{pver}/site-packages/pyglade.pth

gzip -9nf COPYING ChangeLog README MAPPING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,MAPPING}.gz
%{_libdir}/python%{pver}/site-packages/%{module}.pth
%{_libdir}/python%{pver}/site-packages/%{module}
%{_libdir}/python%{pver}/site-packages/pyglade.pth
%{_libdir}/python%{pver}/site-packages/pyglade
%{_includedir}/%{module}/
%attr(-,root,root) %{_prefix}/src/examples/%{name}
