%global tl_name lambdax
%global tl_revision 60278

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Use Lambda expression within LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lambdax
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lambdax.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lambdax.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lambdax.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides Lambda expressions. It is an interface to specify
the parameters and replacement code of a document-command, and then to
evaluate it with compatible arguments. Optionally, it can be used
recursively.

