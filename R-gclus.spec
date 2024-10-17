%global packname  gclus
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.3.1
Release:          3
Summary:          Clustering Graphics
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-cluster 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-cluster

%description
Orders panels in scatterplot matrices and parallel coordinate displays by
some merit index. Package contains various indices of merit, ordering
functions, and enhanced versions of pairs and parcoord which color panels
according to their merit level.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 775926
- Import R-gclus
- Import R-gclus

