Summary:	A file compression and packaging utility compatible with PKZIP
Name:		zip
Version:	3.0
Release:	2
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://ftp.info-zip.org/pub/infozip/src/%{name}30.tgz
# Source0-md5:	7b74551e63f8ee6aab6fbc86676c0d37
Patch0:		%{name}-zmem.patch
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zip program is a compression and file packaging utility. Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%prep
%setup -qn %{name}30
%patch0 -p1

%build
%{__make} -f unix/Makefile generic	\
	prefix=%{_prefix}		\
	CC="%{__cc}"			\
	CPP="%{__cpp}"			\
	CFLAGS_NOOPT="%{rpmcflags} -I. -DUNIX -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -f unix/Makefile install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTALL=install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHERE proginfo/*.txt proginfo/3rdparty.bug
%doc TODO proginfo/infozip.who CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

