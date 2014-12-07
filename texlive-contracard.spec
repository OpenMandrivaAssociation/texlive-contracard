# revision 31745
# category Package
# catalog-ctan /macros/latex/contrib/contracard
# catalog-date 2013-09-17 14:49:30 +0200
# catalog-license lppl1.3
# catalog-version 1.0.0
Name:		texlive-contracard
Version:	1.0.0
Release:	8
Summary:	Generate calling cards for dances
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/contracard
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contracard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contracard.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contracard.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class may be used to create calling cards for traditional
country dances, such as contra and square dances.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/contracard/contracard.cls
%doc %{_texmfdistdir}/doc/latex/contracard/LICENSE
%doc %{_texmfdistdir}/doc/latex/contracard/Makefile
%doc %{_texmfdistdir}/doc/latex/contracard/README
%doc %{_texmfdistdir}/doc/latex/contracard/README.md
%doc %{_texmfdistdir}/doc/latex/contracard/contracard.lod
%doc %{_texmfdistdir}/doc/latex/contracard/contracard.pdf
%doc %{_texmfdistdir}/doc/latex/contracard/contracard.sty
#- source
%doc %{_texmfdistdir}/source/latex/contracard/contracard.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
