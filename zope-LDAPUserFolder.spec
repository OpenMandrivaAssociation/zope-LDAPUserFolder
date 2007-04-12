%define product		LDAPUserFolder
%define version		2.7
%define release		1

%define zope_minver	2.7.1

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python
%define mVersion	%(echo '%{version}' | sed -e 's/\\./_/g')

Summary:	User folder replacement for Zope that authenticates Zope users against LDAP
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://www.dataflake.org/software/ldapuserfolder/ldapuserfolder_%{version}/LDAPUserFolder-%{mVersion}.tar.bz2
URL:		http://www.dataflake.org/software/ldapuserfolder/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver} python-ldap

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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*



