%global tl_name datenumber
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Convert a date into a number and vice versa
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datenumber
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands to convert a date into a number and vice
versa. Additionally there are commands for incrementing and decrementing
a date. Leap years and the Gregorian calendar reform are considered.

