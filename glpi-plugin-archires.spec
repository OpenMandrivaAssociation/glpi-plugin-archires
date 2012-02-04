%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
%endif

Summary: Network reporting plugin
Name: glpi-plugin-archires
Version: 1.9.1
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/archires
Source0: https://forge.indepnet.net/attachments/download/972/glpi-archires-%{version}.tar.gz
Source1: pack.mg_dvl.tar.bz2
Requires: graphviz
BuildArch: noarch

%description
This plugin allow you to generate automatically a graphical representation of
the network architecture.

%prep

%setup -q -n archires
%setup -q -T -D -a 1 -n archires

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/archires
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/archires

%files
%{_datadir}/glpi/plugins/archires
