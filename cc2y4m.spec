Summary:	Translates broken PAL signals to YUV4MPEG2
Summary(pl.UTF-8):	Tłumaczenie zepsutych sygnałów PAL na YUV4MPEG2
Name:		cc2y4m
Version:	0.0.12
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://cube.dyndns.org/~rsnel/cc2y4m/%{name}-%{version}.tar.gz
# Source0-md5:	8e15d4baa67cb31340267bbe44f5970a
URL:		http://cube.dyndns.org/~rsnel/cc2y4m/
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some channels broadcast a TV signal which is not standards compliant.
It usually lacks sync pulses, gets inverted at random times and even
may include disinformation. Those signals can't be comfortably viewed
on a normal television set. The Brooktree 87[89](A) chip has a special
mode in which it doesn't get confused because of missing sync signals.
This program enables this mode, very much alike cabletv, and takes
special measures to keep the image stable and adjust for the
inversion. The output of this program appears on standard output in
YUV4MPEG2 format, and can, for example, be fed to MPlayer.

%description -l pl.UTF-8
Niektóre kanały dostarczają sygnał telewizyjny niezgodny ze
standardami. Zwykle brakuje mu sygnałów synchronizacji, jest odwracany
w losowych chwilach, czasem nawet zawiera dezinformację. Sygnały te
nie mogą być wygodnie oglądane w normalnym telewizorze. Układ Booktree
87[89](A) ma specjalny tryb, w którym nie daje się oszukać z powodu
brakujących sygnałów synchronizacji. Niniejszy program włącza ten tryb
podobnie jak cabletv i czynui specjalne zabiegi, aby utrzymywać
stabilny obraz i dostosowywać się do odwracania sygnału. Program
podaje sygnał wyjściowy na standardowe wyjście w formacie YUV4MPEG2,
który może być następnie przekazany np. do MPlayera.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DVERSION=\"$(VERSION)\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS FAQ README TECH *.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
