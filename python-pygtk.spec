%define pp_subname pygtk

Summary:       GTK+ interface for Python language
Summary(pl):   Interfejs GTK+ dla j�zyka Python
Name:          python-%{pp_subname}
Version:       0.6.5
Release:       1
Copyright:     GPL
Group:         Development/Languages/Python
Group(pl):     Programowanie/J�zyki/Python
Source:        pygtk-%{version}.tar.gz 
#Icon:          linux-python-paint-icon.gif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:      python >= 1.5, gtk+ >= 1.2.1, imlib >= 1.8
BuildRequires: python-devel >= 1.5

%description
This archive contains modules that allow you to use gtk+ in Python
programs. 

%description -l pl
Pakiet ten zawiera modu�y dla j�zyka Python umo�liwiaj�ce tworzenie
program�w z u�yciem biblioteki GTK+.

%prep
%setup -n pygtk-%{version}

%build
%configure
%{__make} OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}
echo %{pp_subname} > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
%{__make} pyexecdir=$RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname} \
	pythondir=$RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{pp_subname} \
	includedir=$RPM_BUILD_ROOT%{_includedir} install
	
# examples
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
mv examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

gzip -9nf COPYING ChangeLog README MAPPING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc {COPYING,ChangeLog,README,MAPPING}.gz
%{_libdir}/python1.5/site-packages/%{pp_subname}.pth
%{_libdir}/python1.5/site-packages/%{pp_subname}
%{_includedir}/%{pp_subname}/
/usr/src/examples/%{name}
