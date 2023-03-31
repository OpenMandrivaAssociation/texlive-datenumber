Name:		texlive-datenumber
Version:	61761
Release:	2
Summary:	Convert a date into a number and vice versa
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datenumber
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands to convert a date into a number
and vice versa. Additionally there are commands for
incrementing and decrementing a date. Leap years and the
Gregorian calendar reform are considered.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/datenumber
%doc %{_texmfdistdir}/doc/latex/datenumber
#- source
%doc %{_texmfdistdir}/source/latex/datenumber

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
