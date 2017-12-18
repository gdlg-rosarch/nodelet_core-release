Name:           ros-indigo-nodelet-core
Version:        1.9.14
Release:        0%{?dist}
Summary:        ROS nodelet_core package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/nodelet_core
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-nodelet
Requires:       ros-indigo-nodelet-topic-tools
BuildRequires:  ros-indigo-catkin

%description
Nodelet Core Metapackage

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 18 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.14-0
- Autogenerated by Bloom

* Thu Apr 06 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.10-0
- Autogenerated by Bloom

* Tue Nov 15 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.8-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.7-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.6-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.5-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.9.4-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Esteve Fernandez <esteve@osrfoundation.org> - 1.9.3-0
- Autogenerated by Bloom

* Thu Oct 30 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.9.2-0
- Autogenerated by Bloom

* Wed Oct 29 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.9.1-0
- Autogenerated by Bloom

