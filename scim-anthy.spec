Summary:	SCIM IMEngine for anthy for Japanese input
Summary(pl.UTF-8):	Silnik IM SCIM dla metody wprowadzania znaków japońskich Anthy
Name:		scim-anthy
Version:	1.2.7
Release:	1
License:	GPL v2+
Group:		Libraries
# note: there is also scim-anthy-ss subproject (with 1.3.1 release - snapshot/development version)
#Source0Download: https://osdn.jp/projects/scim-imengine/releases/p3104
Source0:	http://dl.osdn.jp/scim-imengine/37309/%{name}-%{version}.tar.gz
# Source0-md5:	8d06bfd46839c771401b9f176be8818f
Patch0:		%{name}-no-rpath.patch
Patch1:		%{name}-gtk3.patch
URL:		https://osdn.jp/projects/scim-imengine/
BuildRequires:	anthy-devel >= 6700b-1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.2.0
Requires:	scim >= 1.2.0
Requires:	kasumi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scim-anthy is a SCIM IMEngine module for anthy to support Japanese
input.

%description -l pl.UTF-8
Scim-anthy to moduł silnika IM SCIM umożliwiający wprowadzanie znaków
japońskich poprzez system Anthy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/scim-1.0/*/Helper/anthy-imengine-helper.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/anthy.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/anthy-imengine-setup.so
%{_datadir}/scim/Anthy
%{_datadir}/scim/icons/scim-anthy*.png
