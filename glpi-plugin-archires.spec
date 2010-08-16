%define name glpi-plugin-archires
%define version 1.7.3
%define release %mkrel 1

Summary: Network reporting plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/archires
Source0: https://forge.indepnet.net/attachments/download/478/glpi-archires-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin allow you to generate automatically a graphical representation of
the network architecture.

%prep
%setup -q -n archires

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/archires
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/archires

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/glpi/plugins/archires