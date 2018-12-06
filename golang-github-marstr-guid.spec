# Run tests in check section
# Tests do not work
%bcond_with check

%global goipath         github.com/marstr/guid
Version:                1.1.0

%global common_description %{expand:
This rather bizarre program will scour a Go package for all publicly exported 
entities then create a package that merely delegates the work to the original 
package.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Generates a Go package that acts as a ghost of another
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- First package for Fedora

