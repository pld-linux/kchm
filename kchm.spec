# TODO:
# - separate libs package? (does sth other use libchmmix???)
Summary:	A CHM file viewer for KDE
Summary(pl):	Przegl±darka plików CHM dla KDE
Name:		kchm
Version:	0.6.5
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/kchmnew/%{name}-%{version}.tar.bz2
# Source0-md5:	c11189726ed59563d95d9677ae8555c0
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://sourceforge.net/projects/kchmnew/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A CHM file viewer + corresponding kpart and kio slave for.

%description -l pl
Przegl±darka plików CHM dla KDE oraz odpowiednie modu³y kpart i kio
slave.

%package devel
Summary:	Header files for chmmix library
Summary(pl):	Pliki nag³ówkowe biblioteki chmmix
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for chmmix library.

%description devel -l pl
Pliki nag³ówkowe biblioteki chmmix.

%prep
%setup -q

%build
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# conflicts with chmlib-devel
rm -f $RPM_BUILD_ROOT%{_includedir}/chm_lib.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libchmmix.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/chmnew
%{_datadir}/apps/chmnewpart
%{_datadir}/apps/kchm
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/service*/*.*
%{_desktopdir}/kde/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchmmix.so
%{_libdir}/libchmmix.la
%{_includedir}/chmxx.h
%{_includedir}/lzx.h
