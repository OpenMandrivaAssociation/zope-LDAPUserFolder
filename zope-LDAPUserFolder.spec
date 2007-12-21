%define Product	LDAPUserFolder
%define product	ldapuserfolder
%define name    zope-%{Product}
%define version 2.8
%define release %mkrel 1

%define zope_minver	2.7.1
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	User folder replacement for Zope that authenticates Zope users against LDAP
License:	GPL
Group:		System/Servers
URL:		http://www.dataflake.org/software/ldapuserfolder/
Source:		http://www.dataflake.org/software/ldapuserfolder/ldapuserfolder_%{version}/LDAPUserFolder-%{version}.tgz
Requires:	zope >= %{zope_minver}
Requires:	python2.4-ldap
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This product is a replacement for a Zope user folder. It 
does not store its own user objects but builds them on the 
fly after authenticating a user against the LDAP database.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
