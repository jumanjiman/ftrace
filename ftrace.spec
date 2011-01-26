Name:		ftrace
Version:	0.1
Release:	1%{?dist}
Summary:	Script to dynamically enable/disable kernel ftrace

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/jumanjiman/ftrace
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	initscripts
Requires:	chkconfig
Requires:	util-linux
Requires:	grep

%description
Provides a SysV-style init script to enable or disable
the kernel's ftrace feature dynamically and apply settings
based on a config file.


%prep
%setup -q


%build
# nothing to build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/rc.d/init.d
%{__install} -pm 755 src/ftrace %{buildroot}/%{_sysconfdir}/rc.d/init.d
%{__install} -pm 644 src/ftrace.conf %{buildroot}/%{_sysconfdir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.GPLv3
%doc README
%config(noreplace) %{_sysconfdir}/ftrace.conf
%{_sysconfdir}/rc.d/init.d/ftrace


%preun
if [ $1 -eq 0 ]; then
  service ftrace stop
  chkconfig --del ftrace
fi


%changelog
* Wed Jan 26 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- initial packaging


