Name:		ftrace
Version:	0.5
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
  service ftrace stop || :
  chkconfig --del ftrace &> /dev/null || :
fi


%post
if [ $1 -gt 0 ]; then
  chkconfig --add ftrace &> /dev/null || :
fi


%changelog
* Mon Jan 31 2011 Paul Morgan <jumanjiman@gmail.com> 0.5-1
- add init script conventions per LSB 3.2
- exit code of init script complies with LSB 3.1.1
- by default, start as late as possible

* Fri Jan 28 2011 Mike Sciabica <msciabica@ise.com> 0.4-1
- change boot sequence to run after openibd (msciabica@ise.com)
- extend README with info from kernelnewbies.org (jumanjiman@gmail.com)
- bump release (jumanjiman@gmail.com)
- never fail on preun (jumanjiman@gmail.com)

* Wed Jan 26 2011 Paul Morgan <jumanjiman@gmail.com> 0.3-1
- gracefully handle failure on kernel-xen

* Wed Jan 26 2011 Paul Morgan <jumanjiman@gmail.com> 0.2-1
- alternate method to check if debugfs is mounted

* Wed Jan 26 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- initial packaging


