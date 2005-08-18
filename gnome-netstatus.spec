Summary:	Applet that displays the network status in a GNOME panel
Summary(pl):	Aplet wy¶wietlaj±cy stan po³±czeñ sieciowych na panelu GNOME
Name:		gnome-netstatus
Version:	2.11.90
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/2.11/%{name}-%{version}.tar.bz2
# Source0-md5:	eea34fad7531398d68dc880fb343c296
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-panel-devel >= 2.10.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libglade2-devel >= 1:2.5.0
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applet that displays the network status in a GNOME panel.

%description -l pl
Aplet wy¶wietlaj±cy stan po³±czeñ sieciowych na panelu GNOME.

%prep
%setup -q

%build
%{__gnome_doc_common}
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

%preun
%gconf_schema_uninstall netstatus.schemas

%postun
%scrollkeeper_update_postun

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
%{_sysconfdir}/gconf/schemas/*
