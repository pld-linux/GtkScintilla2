Summary:	GtkScintilla2 - A GTK+2 wrapper for Scintilla editing component
Summary(pl):	GtkScintilla2 - wrapper GTK+2 do komponentu edycyjnego Scintilla
Name:		GtkScintilla2
Version:	0.0.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.gphpedit.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	e275b450c59575adef18175c099df79d
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	scintilla-devel >= 1.53
Requires:	scintilla >= 1.53
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GtkScintilla2, a GTK+2 wrapper for the Scintilla
(http://www.scintilla.org/) editing component which adds some facility
to this powerful component written by Neil Hodgson (and many others).

%description -l pl
To jest GtkScintilla2 - wrapper GTK+2 do komponentu edycyjnego
Scintilla (http://www.scintilla.org/) dodaj�cy nieco udogodnie� do
tego pot�nego komponentu napisanego przez Neila Hodgsona (i wielu
innych).

%package devel
Summary:	Header files for GtkScintilla2 library
Summary(pl):	Pliki nag��wkowe biblioteki GtkScintilla2
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel >= 2.0.0
Requires:	scintilla-devel >= 1.53

%description devel
Headers files needed for compiling other programs against
GtkScintilla2.

%description devel -l pl
Pliki nag��wkowe potrzebne do kompilacji innych program�w u�ywaj�cych
biblioteki GtkScintilla2.

%package static
Summary:	Static GtkScintilla2 library
Summary(pl):	Statyczna biblioteka GtkScintilla2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static GtkScintilla2 library.

%description static -l pl
Statyczna biblioteka GtkScintilla2.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cxx}" \
	CFLAGS="%{rpmcflags} -fPIC `pkg-config --cflags gtk+-2.0` -Wall -DGTK -DSCI_LEXER" \
	LIB_DIR=%{_libdir} \
	PKG_CONFIG_DIR=%{_pkgconfigdir} \
	SCINTILLA_LIB= \
	SCINTILLA_INCLUDE=/usr/include/scintilla \
	SCINTILLA_IFACE=scintilla/include/Scintilla.iface \
	LDFLAGS_POST="-lscintilla -Wl,-soname=libgtkscintilla2.so.0"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	SCINTILLA_LIB= \
	LIB_DIR=%{_libdir} \
	PKG_CONFIG_DIR=%{_pkgconfigdir} \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gtkscintilla2
%{_pkgconfigdir}/GtkScintilla-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
