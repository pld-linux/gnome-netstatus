Name:		gnome-netstatus
Summary:	Applet that displays the network status in a gnome panel.
Version:	0.14
Release:	0.9
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/0.14/%{name}-%{version}.tar.bz2
# Source0-md5:	9308555ffba2269a0a26b9d402e891c8
URL:		http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applet that displays the network status in a gnome panel.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/%{name}-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}/*
%{_datadir}/gnome-2.0/ui/*
%{_iconsdir}/%{name}/*
%{_pixmapsdir}/*

%{_sysconfdir}/gconf/schemas/*
