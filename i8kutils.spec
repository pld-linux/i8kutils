Summary:	User-space programs for Dell Inspiron and Latitude laptops
Summary(pl):	Programy przestrzeni u¿ytkownika dla laptopów Dell Inspiron i Latitude
Name:		i8kutils
Version:	1.25
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://people.debian.org/~dz/i8k/%{name}_%{version}.tar.gz
# Source0-md5:	50c03dde689c5709406118a7c6c120db
Source1:	%{name}.init
Source2:	i8kbuttons.aumix
Source3:	i8kbuttons.conf
URL:		http://people.debian.org/~dz/i8k/
Requires:	aumix
Requires:	tcl 
Requires:	tk 
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a user-space programs for accessing the SMM BIOS
of Dell Inspiron and Latitude laptops. The SMM BIOS is used on many
recent laptops to implement APM functionalities and to access custom
hardware, for example the cooling fans and volume buttons.

%description -l pl
Ten pakiet zawiera programy dzia³aj±ce w przestrzeni u¿ytkownika
s³u¿±ce do dostêpu do SMM BIOS-u laptopów Dell Inspiron i Latitude.
SMM BIOS w nowych laptopach s³u¿y do implementowania funkcjonalno¶ci
APM i dostêpu do specyficznego sprzêtu, na przyk³ad wiatraczków
ch³odz±cych i przycisków g³o¶no¶ci.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install i8kmon.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}
install i8kbuttons.1 i8kctl.1 i8kmon.1 $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "Now modprobe i8k module."
echo
echo "Since than you'll be able to control fans and buttons."
echo

%files
%defattr(644,root,root,755)
%doc README.i8kutils examples
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.conf
%attr(754,root,root) /etc/rc.d/init.d/i8kutils
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
