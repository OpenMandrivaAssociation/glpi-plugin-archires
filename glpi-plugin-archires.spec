%define name glpi-plugin-archires
%define version 1.7.3
%define release %mkrel 2

Summary: Network reporting plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/archires
Source0: https://forge.indepnet.net/attachments/download/478/glpi-archires-%{version}.tar.gz
Source1: pack.mg_dvl.tar.bz2
Requires: graphviz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin allow you to generate automatically a graphical representation of
the network architecture.

%prep
%setup -q -n archires
%setup -q -T -D -a 1 -n archires
find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/archires
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/archires

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/glpi/plugins/archires
