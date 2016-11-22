Summary:	User-space programs for Dell Inspiron and Latitude laptops
Summary(pl.UTF-8):	Programy przestrzeni użytkownika dla laptopów Dell Inspiron i Latitude
Name:		i8kutils
Version:	1.42
Release:	1
License:	GPL
Group:		Applications/System
Source0:	https://launchpad.net/i8kutils/trunk/%{version}/+download/%{name}_%{version}.tar.xz
# Source0-md5:	7470b2908b39a41e3f26b8b3398e189d
Patch0:		%{name}-build.patch
Source1:	%{name}.init
Source2:	i8kbuttons.aumix
Source3:	i8kbuttons.conf
URL:		https://launchpad.net/i8kutils
Requires:	aumix
Requires:	tcl
Requires:	tk
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a user-space programs for accessing the SMM BIOS
of Dell Inspiron and Latitude laptops. The SMM BIOS is used on many
recent laptops to implement APM functionalities and to access custom
hardware, for example the cooling fans and volume buttons.

%description -l pl.UTF-8
Ten pakiet zawiera programy działające w przestrzeni użytkownika
służące do dostępu do SMM BIOS-u laptopów Dell Inspiron i Latitude.
SMM BIOS w nowych laptopach służy do implementowania funkcjonalności
APM i dostępu do specyficznego sprzętu, na przykład wiatraczków
chłodzących i przycisków głośności.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cp -p i8kmon.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}
cp -p i8kctl.1 i8kmon.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -p i8kctl i8kfan i8kmon probe_i8k_calls_time \
	$RPM_BUILD_ROOT%{_bindir}

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
%doc README.i8kutils TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i8kbuttons.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/i8kmon.conf
%attr(754,root,root) /etc/rc.d/init.d/i8kutils
%attr(755,root,root) %{_bindir}/i8kbuttons.aumix
%attr(755,root,root) %{_bindir}/i8kctl
%attr(755,root,root) %{_bindir}/i8kfan
%attr(755,root,root) %{_bindir}/i8kmon
%attr(755,root,root) %{_bindir}/probe_i8k_calls_time
%{_mandir}/man1/i8kctl.1*
%{_mandir}/man1/i8kmon.1*

