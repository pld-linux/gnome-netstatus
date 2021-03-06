Summary:	Applet that displays the network status in a GNOME panel
Summary(pl.UTF-8):	Aplet wyświetlający stan połączeń sieciowych na panelu GNOME
Name:		gnome-netstatus
Version:	2.28.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	9ce64074ed64e2c94a9ea4499749508c
#from http://hasbox.com/gnome-netstatus-notification.diff.txt
#Patch0: %{name}-notification.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-panel-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.24.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applet that displays the network status in a GNOME panel.

%description -l pl.UTF-8
Aplet wyświetlający stan połączeń sieciowych na panelu GNOME.

%prep
%setup -q
#%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install netstatus.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall netstatus.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/%{name}-applet
%{_datadir}/gnome-2.0/ui/GNOME_NetstatusApplet.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_libdir}/bonobo/servers/GNOME_NetstatusApplet_Factory.server
%{_sysconfdir}/gconf/schemas/netstatus.schemas
