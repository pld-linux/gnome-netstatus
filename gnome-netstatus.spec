Summary:	Applet that displays the network status in a GNOME panel
Summary(pl):	Aplet wy¶wietlaj±cy stan po³±czeñ sieciowych na panelu GNOME
Name:		gnome-netstatus
Version:	2.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	8a0e9831ad6b2aa48c6f4c2b6516ab6e
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gnome-panel-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	perl-base
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applet that displays the network status in a GNOME panel.

%description -l pl
Aplet wy¶wietlaj±cy stan po³±czeñ sieciowych na panelu GNOME.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
gnome-doc-common --copy
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/%{name}-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*
%{_iconsdir}/*/*/*/*.png
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
%{_omf_dest_dir}/%{name}
