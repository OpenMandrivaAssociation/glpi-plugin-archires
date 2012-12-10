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


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-2mdv2012.0
+ Revision: 771125
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-1
+ Revision: 771078
- 1.9.1

* Fri May 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.0-1
+ Revision: 680283
- new version

* Thu Sep 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.3-2mdv2011.0
+ Revision: 578863
- add missing icons
- add graphviz dependency

* Mon Aug 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.3-1mdv2011.0
+ Revision: 570527
- import glpi-plugin-archires

