# revision 33670
# category Package
# catalog-ctan /support/ltxfileinfo
# catalog-date 2014-04-24 15:36:27 +0200
# catalog-license gpl
# catalog-version 2.01
Name:		texlive-ltxfileinfo
Version:	2.01
Release:	4
Summary:	Print version info for latex class or style file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/ltxfileinfo
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxfileinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxfileinfo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ltxfileinfo.bin = %{EVRD}

%description
The bash script ltxfileinfo prints information about a LaTeX
class, style and other files to standard output. The script is
based on Uwe Luck's readprov, so it prints information only for
files that contain a \ProvidesFile, \ProvidesClass or
\ProvidesPackage statement. The script tries to correct errors
in these \Provides... statements and it has options, useful for
developers, to make errors in those statements visible.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ltxfileinfo
%{_texmfdistdir}/scripts/ltxfileinfo/ltxfileinfo
%doc %{_texmfdistdir}/doc/support/ltxfileinfo/README
%doc %{_texmfdistdir}/doc/support/ltxfileinfo/ltxfileinfo.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ltxfileinfo/ltxfileinfo ltxfileinfo
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
