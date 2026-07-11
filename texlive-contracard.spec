%global tl_name contracard
%global tl_revision 79287

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.0
Release:	%{tl_revision}.1
Summary:	Generate calling cards for dances
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/contracard
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/contracard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/contracard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/contracard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package and a class used to typeset traditional country dances, such
as contra and square dances, and to create calling cards for the same.

