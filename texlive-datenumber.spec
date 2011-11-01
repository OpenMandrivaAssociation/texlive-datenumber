Name:		texlive-datenumber
Version:	0.02
Release:	1
Summary:	Convert a date into a number and vice versa
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datenumber
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides commands to convert a date into a number
and vice versa. Additionally there are commands for
incrementing and decrementing a date. Leap years and the
Gregorian calendar reform are considered.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/datenumber/datenumber.sty
%{_texmfdistdir}/tex/latex/datenumber/datenumberUSenglish.ldf
%{_texmfdistdir}/tex/latex/datenumber/datenumberdummy.ldf
%{_texmfdistdir}/tex/latex/datenumber/datenumberenglish.ldf
%{_texmfdistdir}/tex/latex/datenumber/datenumberfrench.ldf
%{_texmfdistdir}/tex/latex/datenumber/datenumbergerman.ldf
%{_texmfdistdir}/tex/latex/datenumber/datenumberspanish.ldf
%doc %{_texmfdistdir}/doc/latex/datenumber/README.txt
%doc %{_texmfdistdir}/doc/latex/datenumber/doc.pdf
%doc %{_texmfdistdir}/doc/latex/datenumber/doc.tex
%doc %{_texmfdistdir}/doc/latex/datenumber/docgerman.pdf
%doc %{_texmfdistdir}/doc/latex/datenumber/docgerman.tex
#- source
%doc %{_texmfdistdir}/source/latex/datenumber/datenumber.dtx
%doc %{_texmfdistdir}/source/latex/datenumber/datenumber.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
