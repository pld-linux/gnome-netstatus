Name:		gnome-netstatus
Summary:	Applet that displays the network status in a GNOME panel
Summary(pl):	Aplet pokazuj±cy stan po³±czeñ sieciowych na panelu GNOME
Version:	0.14
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/0.14/%{name}-%{version}.tar.bz2
# Source0-md5:	9308555ffba2269a0a26b9d402e891c8
URL:		http://www.gnome.org/
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2.3.1
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.4.0
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applet that displays the network status in a GNOME panel.

%description -l pl
Aplet pokazuj±cy stan po³±czeñ sieciowych na panelu GNOME.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/%{name}-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_iconsdir}/%{name}
%{_pixmapsdir}/*

%{_sysconfdir}/gconf/schemas/*
