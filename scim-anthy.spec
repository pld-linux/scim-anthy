Summary:	SCIM IMEngine for anthy for Japanese input
Name:		scim-anthy
Version:	1.2.7
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://osdn.dl.sourceforge.jp/scim-imengine/37309/%{name}-%{version}.tar.gz
# Source0-md5:	8d06bfd46839c771401b9f176be8818f
URL:		http://scim-imengine.sourceforge.jp/
BuildRequires:	anthy-devel >= 6700b-1
BuildRequires:	gtk+2-devel
BuildRequires:	scim-devel
Requires:	scim
Requires:	kasumi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scim-anthy is a SCIM IMEngine module for anthy to support Japanese
input.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

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
%{_datadir}/scim/icons/*.png
