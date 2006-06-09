Summary:	Applet that displays the network status in a GNOME panel
Summary(pl):	Aplet wyświetlający stan połączeń sieciowych na panelu GNOME
Name:		gnome-netstatus
Version:	2.12.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	a5f23731a3bf232969e82afef8792a36
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.6.0
BuildRequires:	gnome-panel-devel >= 2.14.1
BuildRequires:	gtk+2-devel >= 2:2.9.2
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.15.1
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2:2.9.2
Requires(post,postun):	scrollkeeper
Requires:	libgnomeui >= 2.15.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applet that displays the network status in a GNOME panel.

%description -l pl
Aplet wyświetlający stan połączeń sieciowych na panelu GNOME.

%prep
%setup -q

%build
gnome-doc-prepare --copy --force
%{__gnome_doc_common}
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install netstatus.schemas
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%preun
%gconf_schema_uninstall netstatus.schemas

%postun
%scrollkeeper_update_postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/%{name}-applet
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/netstatus.schemas
