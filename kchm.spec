# TODO:
# - separate libs/devel/static packages
Summary:	A CHM file viewer for KDE
Summary(pl):	Przegl±darka plików CHM dla KDE
Name:		kchm
Version:	0.6.5
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/kchmnew/%{name}-%{version}.tar.bz2
# Source0-md5:	c11189726ed59563d95d9677ae8555c0
URL:		http://sourceforge.net/projects/kchmnew/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A CHM file viewer + corresponding kpart and kio slave for

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post  -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/service*/*.*
