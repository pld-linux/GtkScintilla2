Summary:	GtkScintilla2 - A GTK+2 wrapper for Scintilla editing component
Name:		GtkScintilla2
Version:	0.0.8
Release:	0.1
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.gphpedit.org/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	libgtkscintilla2.so

%description
This is GtkScintilla2, a GTK+2 wrapper for the Scintilla
(www.scintilla.org) editing component wich adds some facility to this
powerful component written by Neil Hodgson (and may others).

%package devel
Summary:	GtkScintilla2 - Library header files and static libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers files and static libraries needed for compiling other programs
against gtkscintilla2.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%preun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%doc scintilla/doc/
%{_libdir}/pkgconfig/GtkScintilla-2.0.pc
%{_includedir}/gtkscintilla2
%{_libdir}/*.a
