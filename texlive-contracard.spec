Name:		texlive-contracard
Version:	1.1.0
Release:	1
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
%{_texmfdistdir}/tex/latex/contracard
%doc %{_texmfdistdir}/doc/latex/contracard
#- source
%doc %{_texmfdistdir}/source/latex/contracard

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
