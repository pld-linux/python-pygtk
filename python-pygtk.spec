Summary:       GTK+ interface for Python language
Summary(pl):   Interfejs GTK+ dla jêzyka Python
Name:          python-pygtk
Version:       0.6.1
Release:       1
Copyright:     GPL
Group:         Development/Languages/Python
Group(pl):     Programowanie/Jêzyki/Python
Source:        pygtk-%{version}.tar.gz 
#Icon:          linux-python-paint-icon.gif
BuildRoot:	   /tmp/%{name}-%{version}-root
Requires:      python >= 1.5, gtk+ >= 1.2.1, imlib >= 1.8
#BuildRequires: python-devel >= 1.5

%description
This archive contains modules that allow you to use gtk+ in Python
programs. 

%description -l pl
Pakiet ten zawiera modu³y dla jêzyka Python umo¿liwiaj±ce tworzenie
programów z u¿yciem biblioteki GTK+.

%prep
%setup -n pygtk-%{version}

%build
./configure %{_target_platform}
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK
echo %{_libdir}/python1.5/site-packages/PyGTK \
	> $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK.pth
make pyexecdir=$RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK \
	pythondir=$RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK install
	
	
gzip -9nf COPYING ChangeLog README
tar czf examples.tar.gz examples

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc {COPYING,ChangeLog,README,examples.tar}.gz
%{_libdir}/python1.5/site-packages/PyGTK.pth
%{_libdir}/python1.5/site-packages/PyGTK
