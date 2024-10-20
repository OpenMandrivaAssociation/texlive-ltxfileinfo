Name:		texlive-ltxfileinfo
Version:	38663
Release:	2
Summary:	Print version info for latex class or style file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ltxfileinfo
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxfileinfo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxfileinfo.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/ltxfileinfo/ltxfileinfo ltxfileinfo
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
