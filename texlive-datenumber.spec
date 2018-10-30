# revision 18951
# category Package
# catalog-ctan /macros/latex/contrib/datenumber
# catalog-date 2006-11-16 11:36:05 +0100
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-datenumber
Version:	0.02
Release:	11
Summary:	Convert a date into a number and vice versa
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datenumber
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datenumber.source.tar.xz
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.02-2
+ Revision: 750840
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.02-1
+ Revision: 718205
- texlive-datenumber
- texlive-datenumber
- texlive-datenumber
- texlive-datenumber

