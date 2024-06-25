%global debug_package %{nil}

Name:           diskus
Version:        0.7.0
Release:        1%{?dist}
Summary:        A minimal, fast alternative to du -sh
Group:          Applications/System
License:        MIT
URL:            https://github.com/sharkdp/%{name}
Source:         https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake, openssl-devel
%{?el7:BuildRequires: cargo, rust}

%description
diskus is a very simple program that computes the total size of the current directory. It is a
parallelized version of du -sh. On my 8-core laptop, it is about ten times faster than du with
a cold disk cache and more than three times faster with a warm disk cache.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/diskus %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/diskus

%changelog
* Mon Nov 15 2021 Jamie Curnow <jc@jc21.com> - 0.7.0-1
- v0.7.0

* Tue Sep 24 2019 Jamie Curnow <jc@jc21.com> - 0.6.0-1
- v0.6.0

* Thu Feb 14 2018 Jamie Curnow <jc@jc21.com> - 0.5.0-1
- Initial spec <3

