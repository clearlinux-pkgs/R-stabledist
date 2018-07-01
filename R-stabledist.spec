#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-stabledist
Version  : 0.7.1
Release  : 11
URL      : https://cran.r-project.org/src/contrib/stabledist_0.7-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stabledist_0.7-1.tar.gz
Summary  : Stable Distribution Functions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-FMStable
Requires: R-fBasics
BuildRequires : R-FMStable
BuildRequires : R-fBasics
BuildRequires : clr-R-helpers

%description
generation for (skew) stable distributions, using the parametrizations of
  Nolan.

%prep
%setup -q -c -n stabledist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530426001

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530426001
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stabledist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stabledist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stabledist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library stabledist|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/stabledist/DESCRIPTION
/usr/lib64/R/library/stabledist/INDEX
/usr/lib64/R/library/stabledist/Meta/Rd.rds
/usr/lib64/R/library/stabledist/Meta/features.rds
/usr/lib64/R/library/stabledist/Meta/hsearch.rds
/usr/lib64/R/library/stabledist/Meta/links.rds
/usr/lib64/R/library/stabledist/Meta/nsInfo.rds
/usr/lib64/R/library/stabledist/Meta/package.rds
/usr/lib64/R/library/stabledist/NAMESPACE
/usr/lib64/R/library/stabledist/R/stabledist
/usr/lib64/R/library/stabledist/R/stabledist.rdb
/usr/lib64/R/library/stabledist/R/stabledist.rdx
/usr/lib64/R/library/stabledist/help/AnIndex
/usr/lib64/R/library/stabledist/help/aliases.rds
/usr/lib64/R/library/stabledist/help/paths.rds
/usr/lib64/R/library/stabledist/help/stabledist.rdb
/usr/lib64/R/library/stabledist/help/stabledist.rdx
/usr/lib64/R/library/stabledist/html/00Index.html
/usr/lib64/R/library/stabledist/html/R.css
/usr/lib64/R/library/stabledist/unitTests/Makefile
/usr/lib64/R/library/stabledist/unitTests/runTests.R
/usr/lib64/R/library/stabledist/unitTests/runit.StableDistribution.R
/usr/lib64/R/library/stabledist/xtraR/Levy.R
