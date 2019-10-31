#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtlocation
Version  : 5.13.2
Release  : 19
URL      : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtlocation-everywhere-src-5.13.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtlocation-everywhere-src-5.13.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 CC0-1.0 GFDL-1.3 GPL-2.0 GPL-3.0 ISC JSON LGPL-3.0 MIT NCSA OpenSSL Public-Domain Unlicense Zlib
Requires: qtlocation-lib = %{version}-%{release}
Requires: qtlocation-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5XmlPatterns)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
The scalable icons are from:
http://tango.freedesktop.org/Tango_Icon_Library
http://darkobra.deviantart.com/art/Tango-Weather-Icon-Pack-98024429

%package dev
Summary: dev components for the qtlocation package.
Group: Development
Requires: qtlocation-lib = %{version}-%{release}
Provides: qtlocation-devel = %{version}-%{release}
Requires: qtlocation = %{version}-%{release}

%description dev
dev components for the qtlocation package.


%package lib
Summary: lib components for the qtlocation package.
Group: Libraries
Requires: qtlocation-license = %{version}-%{release}

%description lib
lib components for the qtlocation package.


%package license
Summary: license components for the qtlocation package.
Group: Default

%description license
license components for the qtlocation package.


%prep
%setup -q -n qtlocation-everywhere-src-5.13.2
cd %{_builddir}/qtlocation-everywhere-src-5.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1572536472
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtlocation
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtlocation/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtlocation/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtlocation/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtlocation/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtlocation/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtlocation/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtlocation/d8b489a3c3d500a6601181e3db39bec6124b86fc
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/examples/location/geojson_viewer/data/10-countries_LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/6aa54cc12e002b5197172fe3796fb0ddd09ebc7c
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/clip2tri/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/69d5aab915ac11e2d4afbdbf664824e654b7ae93
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/clipper/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/4ed94404009026adb05e6da8bf8c857ca26760bb
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/earcut/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/1c92a2b8d0646e9c5e8696397c40b1407b46fddf
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/earcut/0.12.4/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/1c92a2b8d0646e9c5e8696397c40b1407b46fddf
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/kdbush/0.1.1-1/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/2402d654960118ffda4e8cd9db4d05531f5ceaae
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/polylabel/1.0.3/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/3a267029cb82d0e9c3188d47cdcbc3e8d939e7e2
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/shelf-pack/2.1.1/LICENSE.md %{buildroot}/usr/share/package-licenses/qtlocation/385f23556b74e358767dc3349fbe58201f95a634
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/supercluster/0.2.2/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/644a9caba03cab9194094c168962c125e7d6b8dc
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/tao_tuple/28626e99/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/42a688ebbcdf9cb6db783ade7cdfa2f922ab9715
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/deps/variant/1.1.4/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/ae3dbcee04c86fbc589fcf2547d4aaaeb41db3c2
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/mapbox-gl-native/vendor/nunicode/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/ea1ed91b37e5c99835b9ebf0861f96dfda2524cd
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/3rdparty/poly2tri/LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/3c4a0cf53278b001dd25ca8dea8d543fc0374181
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/src/plugins/geoservices/mapbox/maki-4.0.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtlocation/34b2b37ec594d86bd391137b4fb644eccb17bdbb
cp %{_builddir}/qtlocation-everywhere-src-5.13.2/tests/auto/qgeojson/10-countries_LICENSE %{buildroot}/usr/share/package-licenses/qtlocation/6aa54cc12e002b5197172fe3796fb0ddd09ebc7c
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/error_messages_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/locationvaluetypehelper_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qabstractgeotilecache_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qcache3q_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativecategory_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativecirclemapitem_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativecontactdetail_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeocodemodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomaneuver_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomap_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapcopyrightsnotice_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapitembase_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapitemgroup_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapitemtransitionmanager_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapitemview_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapparameter_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomapquickitem_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeomaptype_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeoroute_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeoroutemodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeoroutesegment_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativegeoserviceprovider_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativenavigator_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativenavigator_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeperiod_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplace_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplaceattribute_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplacecontentmodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplaceeditorialmodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplaceicon_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplaceimagemodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeplaceuser_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativepolygonmapitem_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativepolylinemapitem_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeratings_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativerectanglemapitem_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativereviewmodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativeroutemapitem_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativesearchmodelbase_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativesearchresultmodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativesearchsuggestionmodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativesupplier_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qdeclarativesupportedcategoriesmodel_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocameracapabilities_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocameradata_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocameratiles_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocameratiles_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocodereply_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocodingmanager_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeocodingmanagerengine_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeofiletilecache_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeojson_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomaneuver_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomap_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomap_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomapitemgeometry_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomapobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomapobject_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomapobjectqsgsupport_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomapparameter_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomappingmanager_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomappingmanager_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomappingmanagerengine_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomappingmanagerengine_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomaptype_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeomaptype_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoprojection_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoroute_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeorouteparser_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeorouteparser_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeorouteparserosrmv4_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeorouteparserosrmv5_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoroutereply_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeorouterequest_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoroutesegment_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoroutingmanager_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoroutingmanagerengine_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeoserviceprovider_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmap_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmap_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmaplabs_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmappingmanagerengine_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmappingmanagerengine_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmapreply_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmapreply_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmapscene_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotiledmapscene_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotilefetcher_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotilefetcher_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotilerequestmanager_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotilespec_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qgeotilespec_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qlocationglobal_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapcircleobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapcircleobject_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapcircleobjectqsg_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapiconobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapiconobject_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapiconobjectqsg_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapobjectview_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmapobjectview_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmappolygonobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmappolygonobject_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmappolygonobjectqsg_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmappolylineobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmappolylineobject_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmappolylineobjectqsg_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmaprouteobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmaprouteobject_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qmaprouteobjectqsg_p_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qnavigationmanager_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qnavigationmanagerengine_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qparameterizableobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplace_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceattribute_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacecategory_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacecontactdetail_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacecontent_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacecontentrequest_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceeditorial_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceicon_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceimage_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacemanagerengine_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceproposedsearchresult_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceratings_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacereply_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceresult_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacereview_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacesearchrequest_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacesearchresult_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplacesupplier_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qplaceuser_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qqsgmapobject_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qquickgeomapgesturearea_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/qtlocation-config_p.h
/usr/include/qt5/QtLocation/5.13.2/QtLocation/private/unsupportedreplies_p.h
/usr/include/qt5/QtLocation/QGeoCodeReply
/usr/include/qt5/QtLocation/QGeoCodingManager
/usr/include/qt5/QtLocation/QGeoCodingManagerEngine
/usr/include/qt5/QtLocation/QGeoManeuver
/usr/include/qt5/QtLocation/QGeoRoute
/usr/include/qt5/QtLocation/QGeoRouteLeg
/usr/include/qt5/QtLocation/QGeoRouteReply
/usr/include/qt5/QtLocation/QGeoRouteRequest
/usr/include/qt5/QtLocation/QGeoRouteSegment
/usr/include/qt5/QtLocation/QGeoRoutingManager
/usr/include/qt5/QtLocation/QGeoRoutingManagerEngine
/usr/include/qt5/QtLocation/QGeoServiceProvider
/usr/include/qt5/QtLocation/QGeoServiceProviderFactory
/usr/include/qt5/QtLocation/QLocation
/usr/include/qt5/QtLocation/QPlace
/usr/include/qt5/QtLocation/QPlaceAttribute
/usr/include/qt5/QtLocation/QPlaceCategory
/usr/include/qt5/QtLocation/QPlaceContactDetail
/usr/include/qt5/QtLocation/QPlaceContent
/usr/include/qt5/QtLocation/QPlaceContentReply
/usr/include/qt5/QtLocation/QPlaceContentRequest
/usr/include/qt5/QtLocation/QPlaceDetailsReply
/usr/include/qt5/QtLocation/QPlaceEditorial
/usr/include/qt5/QtLocation/QPlaceIcon
/usr/include/qt5/QtLocation/QPlaceIdReply
/usr/include/qt5/QtLocation/QPlaceImage
/usr/include/qt5/QtLocation/QPlaceManager
/usr/include/qt5/QtLocation/QPlaceManagerEngine
/usr/include/qt5/QtLocation/QPlaceMatchReply
/usr/include/qt5/QtLocation/QPlaceMatchRequest
/usr/include/qt5/QtLocation/QPlaceProposedSearchResult
/usr/include/qt5/QtLocation/QPlaceRatings
/usr/include/qt5/QtLocation/QPlaceReply
/usr/include/qt5/QtLocation/QPlaceResult
/usr/include/qt5/QtLocation/QPlaceReview
/usr/include/qt5/QtLocation/QPlaceSearchReply
/usr/include/qt5/QtLocation/QPlaceSearchRequest
/usr/include/qt5/QtLocation/QPlaceSearchResult
/usr/include/qt5/QtLocation/QPlaceSearchSuggestionReply
/usr/include/qt5/QtLocation/QPlaceSupplier
/usr/include/qt5/QtLocation/QPlaceUser
/usr/include/qt5/QtLocation/QtLocation
/usr/include/qt5/QtLocation/QtLocationDepends
/usr/include/qt5/QtLocation/QtLocationVersion
/usr/include/qt5/QtLocation/placemacro.h
/usr/include/qt5/QtLocation/qgeocodereply.h
/usr/include/qt5/QtLocation/qgeocodingmanager.h
/usr/include/qt5/QtLocation/qgeocodingmanagerengine.h
/usr/include/qt5/QtLocation/qgeomaneuver.h
/usr/include/qt5/QtLocation/qgeoroute.h
/usr/include/qt5/QtLocation/qgeoroutereply.h
/usr/include/qt5/QtLocation/qgeorouterequest.h
/usr/include/qt5/QtLocation/qgeoroutesegment.h
/usr/include/qt5/QtLocation/qgeoroutingmanager.h
/usr/include/qt5/QtLocation/qgeoroutingmanagerengine.h
/usr/include/qt5/QtLocation/qgeoserviceprovider.h
/usr/include/qt5/QtLocation/qgeoserviceproviderfactory.h
/usr/include/qt5/QtLocation/qlocation.h
/usr/include/qt5/QtLocation/qlocationglobal.h
/usr/include/qt5/QtLocation/qplace.h
/usr/include/qt5/QtLocation/qplaceattribute.h
/usr/include/qt5/QtLocation/qplacecategory.h
/usr/include/qt5/QtLocation/qplacecontactdetail.h
/usr/include/qt5/QtLocation/qplacecontent.h
/usr/include/qt5/QtLocation/qplacecontentreply.h
/usr/include/qt5/QtLocation/qplacecontentrequest.h
/usr/include/qt5/QtLocation/qplacedetailsreply.h
/usr/include/qt5/QtLocation/qplaceeditorial.h
/usr/include/qt5/QtLocation/qplaceicon.h
/usr/include/qt5/QtLocation/qplaceidreply.h
/usr/include/qt5/QtLocation/qplaceimage.h
/usr/include/qt5/QtLocation/qplacemanager.h
/usr/include/qt5/QtLocation/qplacemanagerengine.h
/usr/include/qt5/QtLocation/qplacematchreply.h
/usr/include/qt5/QtLocation/qplacematchrequest.h
/usr/include/qt5/QtLocation/qplaceproposedsearchresult.h
/usr/include/qt5/QtLocation/qplaceratings.h
/usr/include/qt5/QtLocation/qplacereply.h
/usr/include/qt5/QtLocation/qplaceresult.h
/usr/include/qt5/QtLocation/qplacereview.h
/usr/include/qt5/QtLocation/qplacesearchreply.h
/usr/include/qt5/QtLocation/qplacesearchrequest.h
/usr/include/qt5/QtLocation/qplacesearchresult.h
/usr/include/qt5/QtLocation/qplacesearchsuggestionreply.h
/usr/include/qt5/QtLocation/qplacesupplier.h
/usr/include/qt5/QtLocation/qplaceuser.h
/usr/include/qt5/QtLocation/qtlocation-config.h
/usr/include/qt5/QtLocation/qtlocationversion.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qclipperutils_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qdoublematrix4x4_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qdoublevector2d_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qdoublevector3d_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeoaddress_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeocircle_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeocoordinate_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeocoordinateobject_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeolocation_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeopath_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeopolygon_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeopositioninfo_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeopositioninfosource_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeorectangle_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qgeoshape_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qlocationdata_simulator_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qlocationutils_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qnmeapositioninfosource_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qpositioningglobal_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qtpositioning-config_p.h
/usr/include/qt5/QtPositioning/5.13.2/QtPositioning/private/qwebmercator_p.h
/usr/include/qt5/QtPositioning/QGeoAddress
/usr/include/qt5/QtPositioning/QGeoAreaMonitorInfo
/usr/include/qt5/QtPositioning/QGeoAreaMonitorSource
/usr/include/qt5/QtPositioning/QGeoCircle
/usr/include/qt5/QtPositioning/QGeoCoordinate
/usr/include/qt5/QtPositioning/QGeoLocation
/usr/include/qt5/QtPositioning/QGeoPath
/usr/include/qt5/QtPositioning/QGeoPolygon
/usr/include/qt5/QtPositioning/QGeoPositionInfo
/usr/include/qt5/QtPositioning/QGeoPositionInfoSource
/usr/include/qt5/QtPositioning/QGeoPositionInfoSourceFactory
/usr/include/qt5/QtPositioning/QGeoRectangle
/usr/include/qt5/QtPositioning/QGeoSatelliteInfo
/usr/include/qt5/QtPositioning/QGeoSatelliteInfoSource
/usr/include/qt5/QtPositioning/QGeoShape
/usr/include/qt5/QtPositioning/QNmeaPositionInfoSource
/usr/include/qt5/QtPositioning/QtPositioning
/usr/include/qt5/QtPositioning/QtPositioningDepends
/usr/include/qt5/QtPositioning/QtPositioningVersion
/usr/include/qt5/QtPositioning/qgeoaddress.h
/usr/include/qt5/QtPositioning/qgeoareamonitorinfo.h
/usr/include/qt5/QtPositioning/qgeoareamonitorsource.h
/usr/include/qt5/QtPositioning/qgeocircle.h
/usr/include/qt5/QtPositioning/qgeocoordinate.h
/usr/include/qt5/QtPositioning/qgeolocation.h
/usr/include/qt5/QtPositioning/qgeopath.h
/usr/include/qt5/QtPositioning/qgeopolygon.h
/usr/include/qt5/QtPositioning/qgeopositioninfo.h
/usr/include/qt5/QtPositioning/qgeopositioninfosource.h
/usr/include/qt5/QtPositioning/qgeopositioninfosourcefactory.h
/usr/include/qt5/QtPositioning/qgeorectangle.h
/usr/include/qt5/QtPositioning/qgeosatelliteinfo.h
/usr/include/qt5/QtPositioning/qgeosatelliteinfosource.h
/usr/include/qt5/QtPositioning/qgeoshape.h
/usr/include/qt5/QtPositioning/qnmeapositioninfosource.h
/usr/include/qt5/QtPositioning/qpositioningglobal.h
/usr/include/qt5/QtPositioning/qtpositioning-config.h
/usr/include/qt5/QtPositioning/qtpositioningversion.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qdeclarativegeoaddress_p.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qdeclarativegeolocation_p.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qdeclarativeposition_p.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qdeclarativepositionsource_p.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qpositioningquickglobal_p.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qquickgeocoordinateanimation_p.h
/usr/include/qt5/QtPositioningQuick/5.13.2/QtPositioningQuick/private/qquickgeocoordinateanimation_p_p.h
/usr/include/qt5/QtPositioningQuick/QtPositioningQuick
/usr/include/qt5/QtPositioningQuick/QtPositioningQuickDepends
/usr/include/qt5/QtPositioningQuick/QtPositioningQuickVersion
/usr/include/qt5/QtPositioningQuick/qpositioningquickglobal.h
/usr/include/qt5/QtPositioningQuick/qtpositioningquickversion.h
/usr/lib64/cmake/Qt5Location/Qt5LocationConfig.cmake
/usr/lib64/cmake/Qt5Location/Qt5LocationConfigVersion.cmake
/usr/lib64/cmake/Qt5Location/Qt5Location_GeoServiceProviderFactoryEsri.cmake
/usr/lib64/cmake/Qt5Location/Qt5Location_QGeoServiceProviderFactoryItemsOverlay.cmake
/usr/lib64/cmake/Qt5Location/Qt5Location_QGeoServiceProviderFactoryMapbox.cmake
/usr/lib64/cmake/Qt5Location/Qt5Location_QGeoServiceProviderFactoryMapboxGL.cmake
/usr/lib64/cmake/Qt5Location/Qt5Location_QGeoServiceProviderFactoryNokia.cmake
/usr/lib64/cmake/Qt5Location/Qt5Location_QGeoServiceProviderFactoryOsm.cmake
/usr/lib64/cmake/Qt5Positioning/Qt5PositioningConfig.cmake
/usr/lib64/cmake/Qt5Positioning/Qt5PositioningConfigVersion.cmake
/usr/lib64/cmake/Qt5Positioning/Qt5Positioning_QGeoPositionInfoSourceFactoryGeoclue.cmake
/usr/lib64/cmake/Qt5Positioning/Qt5Positioning_QGeoPositionInfoSourceFactoryGeoclue2.cmake
/usr/lib64/cmake/Qt5Positioning/Qt5Positioning_QGeoPositionInfoSourceFactoryPoll.cmake
/usr/lib64/cmake/Qt5Positioning/Qt5Positioning_QGeoPositionInfoSourceFactorySerialNmea.cmake
/usr/lib64/cmake/Qt5PositioningQuick/Qt5PositioningQuickConfig.cmake
/usr/lib64/cmake/Qt5PositioningQuick/Qt5PositioningQuickConfigVersion.cmake
/usr/lib64/libQt5Location.prl
/usr/lib64/libQt5Location.so
/usr/lib64/libQt5Positioning.prl
/usr/lib64/libQt5Positioning.so
/usr/lib64/libQt5PositioningQuick.prl
/usr/lib64/libQt5PositioningQuick.so
/usr/lib64/pkgconfig/Qt5Location.pc
/usr/lib64/pkgconfig/Qt5Positioning.pc
/usr/lib64/pkgconfig/Qt5PositioningQuick.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_location.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_location_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_positioning.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_positioning_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_positioningquick.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_positioningquick_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Location.so.5
/usr/lib64/libQt5Location.so.5.13
/usr/lib64/libQt5Location.so.5.13.2
/usr/lib64/libQt5Positioning.so.5
/usr/lib64/libQt5Positioning.so.5.13
/usr/lib64/libQt5Positioning.so.5.13.2
/usr/lib64/libQt5PositioningQuick.so.5
/usr/lib64/libQt5PositioningQuick.so.5.13
/usr/lib64/libQt5PositioningQuick.so.5.13.2
/usr/lib64/qt5/plugins/geoservices/libqtgeoservices_esri.so
/usr/lib64/qt5/plugins/geoservices/libqtgeoservices_itemsoverlay.so
/usr/lib64/qt5/plugins/geoservices/libqtgeoservices_mapbox.so
/usr/lib64/qt5/plugins/geoservices/libqtgeoservices_mapboxgl.so
/usr/lib64/qt5/plugins/geoservices/libqtgeoservices_nokia.so
/usr/lib64/qt5/plugins/geoservices/libqtgeoservices_osm.so
/usr/lib64/qt5/plugins/position/libqtposition_geoclue.so
/usr/lib64/qt5/plugins/position/libqtposition_geoclue2.so
/usr/lib64/qt5/plugins/position/libqtposition_positionpoll.so
/usr/lib64/qt5/plugins/position/libqtposition_serialnmea.so
/usr/lib64/qt5/qml/Qt/labs/location/liblocationlabsplugin.so
/usr/lib64/qt5/qml/Qt/labs/location/plugins.qmltypes
/usr/lib64/qt5/qml/Qt/labs/location/qmldir
/usr/lib64/qt5/qml/QtLocation/libdeclarative_location.so
/usr/lib64/qt5/qml/QtLocation/plugins.qmltypes
/usr/lib64/qt5/qml/QtLocation/qmldir
/usr/lib64/qt5/qml/QtPositioning/libdeclarative_positioning.so
/usr/lib64/qt5/qml/QtPositioning/plugins.qmltypes
/usr/lib64/qt5/qml/QtPositioning/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtlocation/1c92a2b8d0646e9c5e8696397c40b1407b46fddf
/usr/share/package-licenses/qtlocation/2402d654960118ffda4e8cd9db4d05531f5ceaae
/usr/share/package-licenses/qtlocation/34b2b37ec594d86bd391137b4fb644eccb17bdbb
/usr/share/package-licenses/qtlocation/385f23556b74e358767dc3349fbe58201f95a634
/usr/share/package-licenses/qtlocation/3a267029cb82d0e9c3188d47cdcbc3e8d939e7e2
/usr/share/package-licenses/qtlocation/3c4a0cf53278b001dd25ca8dea8d543fc0374181
/usr/share/package-licenses/qtlocation/42a688ebbcdf9cb6db783ade7cdfa2f922ab9715
/usr/share/package-licenses/qtlocation/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtlocation/4ed94404009026adb05e6da8bf8c857ca26760bb
/usr/share/package-licenses/qtlocation/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtlocation/644a9caba03cab9194094c168962c125e7d6b8dc
/usr/share/package-licenses/qtlocation/69d5aab915ac11e2d4afbdbf664824e654b7ae93
/usr/share/package-licenses/qtlocation/6aa54cc12e002b5197172fe3796fb0ddd09ebc7c
/usr/share/package-licenses/qtlocation/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
/usr/share/package-licenses/qtlocation/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtlocation/ae3dbcee04c86fbc589fcf2547d4aaaeb41db3c2
/usr/share/package-licenses/qtlocation/d8b489a3c3d500a6601181e3db39bec6124b86fc
/usr/share/package-licenses/qtlocation/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtlocation/ea1ed91b37e5c99835b9ebf0861f96dfda2524cd
/usr/share/package-licenses/qtlocation/f45ee1c765646813b442ca58de72e20a64a7ddba
