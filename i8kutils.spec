Summary:	Kernel driver and user-space programs for Dell Inspiron and Latitude laptops.
Name:		i8kutils
Version:	1.25
Release:	1
License:	GPL
Group:		Applications/System/Configuration/Hardware
######		Unknown group!
Source0:	http://people.debian.org/~dz/i8k/%{name}_%{version}.tar.gz
# Source0-md5:	50c03dde689c5709406118a7c6c120db
Source1:	i8kutils
URL:		http://people.debian.org/~dz/i8k/
Requires:	aumix ld-linux.so.2 libc.so.6
Provides:	%{name}-%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#BuildRequires:

%description
This package contains a user-space programs for accessing the SMM BIOS 
of Dell Inspiron and Latitude laptops. The SMM BIOS is used on many 
recent laptops to implement APM functionalities and to access custom
hardware, for example the cooling fans and volume buttons.

%prep
rm -rf %buildroot
%setup -q

%build
%make
mkdir -p $RPM_BUILD_ROOT/usr/bin
make DESTDIR=$RPM_BUILD_ROOT install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp i8kmon.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d
chmod a+x $RPM_BUILD_ROOT/etc/rc.d/init.d/*
cp i8kbuttons.1 i8kctl.1 i8kmon.1 $RPM_BUILD_ROOT%{_mandir}/man1
%makeinstall

%post
echo
echo "Now modprobe i8k module."
echo
echo "Since than you'll be able to control fans and buttons."
echo

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%doc COPYING README.i8kutils ./examples
%config(noreplace) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
## /etc/rc.d/initd/
