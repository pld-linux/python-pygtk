Summary: Python -> GTK interface 
Name: python-pygtk
Version: 0.5.9
Release: 1
Copyright: distributable
Packager: Oliver Andrich <oli@andrich.net>
Group: Development/Languages/Python
Source0: pygtk-0.5.9.tar.gz 
Source1: PyGTK.pth
Icon: linux-python-paint-icon.gif
BuildRoot:	/tmp/%{name}-%{version}-root
Requires: python >= 1.5, gtk+ >= 1.1.9, imlib >= 1.8

%changelog

* Sun Dec 27 1998 Oliver Andrich <oli@andrich.net>

- updated package to version 0.5.9 which requires the recent developer version
	of gtk

* Sun Oct 04 1998 Oliver Andrich <oli@andrich.net>

- updated package to version 0.5.3 which requires the recent developer version
	of gtk

* Sun Aug 09 1998 Oliver Andrich <oli@andrich.net>

- created the package 

%description
This archive contains modules that allow you to use gtk in Python
programs.  At present, it is a fairly complete set of bindings.
Despite the low version number, this peice of software is quite
useful, and is usable to write moderately complex programs.  (see the
examples directory for some examples of the simpler programs you could
write).

						
%prep
%setup -n pygtk-0.5.9

%build
./configure %{_target}
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK
install -m 644 $RPM_SOURCE_DIR/PyGTK.pth $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages
make pyexecdir=$RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK \
	pythondir=$RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/PyGTK install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING Changelog README examples
%{_libdir}/python1.5/site-packages/PyGTK.pth
%{_libdir}/python1.5/site-packages/PyGTK
