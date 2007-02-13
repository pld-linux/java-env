Summary:	Java environment scripts
Summary(pl.UTF-8):	Skrypty środowiskowe dla Javy
Name:		java-env
Version:	0.1
Release:	1
License:	GPL
Group:		Applications
Source0:	%{name}.tgz
# Source0-md5:	1ec5435d5d9e420a612cba6d722156a0
#URL:		http://www.pld.org.pl/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		classdir	%{_datadir}/java

%description
Java environment scripts.

%description -l pl.UTF-8
Skrypty środowiskowe dla Javy.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_libdir}/%{name} \
	$RPM_BUILD_ROOT/etc/sysconfig/java \
	$RPM_BUILD_ROOT/etc/profile.d \
	$RPM_BUILD_ROOT%{classdir}

install usr/bin/* $RPM_BUILD_ROOT%{_bindir}
install usr/lib/%{name}/* $RPM_BUILD_ROOT%{_libdir}/%{name}
install etc/profile.d/* $RPM_BUILD_ROOT/etc/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /etc/profile.d/*
%dir /etc/sysconfig/java
%{_libdir}/%{name}
