#
# TODO:
# - add desc and pl desc.
Summary:	World of Padman - the biggest Q3A-Funmod project
Summary(pl.UTF-8):	World of Padman - największa modyfikacja projektu Q3A
Name:		worldofpadman-data
Version:	1.2
Release:	0.5
License:	GPL v2
Group:		X11/Applications/Games
Source0:	ftp://ftp.snt.utwente.nl/pub/games/worldofpadman/linux/worldofpadman.run
# Source0-md5:	c7650414d7865ddac26ada6b3f7b8cc9
Source1:	ftp://ftp.snt.utwente.nl/pub/games/worldofpadman/linux/wop_patch_1_2.run
# Source1-md5:	3468fc91889795471bc68e35ea334614
URL:		http://www.worldofpadman.com
BuildRequires:	/bin/sh
BuildRequires:	tar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.

#% description -l pl.UTF-8

%prep
%setup -q -T -c -n worldofpadman
sh %{SOURCE0} --noexec --target .
sh %{SOURCE1} --noexec --target .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/worldofpadman/wop,%{_desktopdir},%{_pixmapsdir}}

tar xf wop-data.tar -C $RPM_BUILD_ROOT%{_datadir}/worldofpadman/wop
tar xf wop-data-1.2.tar -C $RPM_BUILD_ROOT%{_datadir}/worldofpadman/wop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/worldofpadman/wop
