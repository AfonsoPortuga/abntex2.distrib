%define texdir /usr/share/texmf-dist

Summary:	LaTeX macros for writing documents following the ABNT norms
Name:		abntex2
Version:	1.6
Release:	%mkrel 1
License:	LPPL
Group:		Publishing
URL:		http://code.google.com/p/abntex2/
Source0:	http://abntex2.googlecode.com/files/abntex2.tds-%{version}.zip
Requires:	texlive
BuildArch:	noarch

%description
abnTeX2 able to write LaTeX documents which conform to several norms from ABNT
(Brazilian Association for Technical Norms).

%prep
%setup -cn abntex2-%{version}

%install
install -m 755 -d %{buildroot}/%{texdir}
cp -rf %{_builddir}/%{name}-%{version}/* %{buildroot}/%{texdir}

%post
texhash

%postun
texhash

%files
%{texdir}/bibtex/bib/abntex2/
%{texdir}/bibtex/bst/abntex2/
%{texdir}/doc/latex/abntex2/
%{texdir}/tex/latex/abntex2/
