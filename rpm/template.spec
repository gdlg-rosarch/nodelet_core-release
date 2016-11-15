Name:           ros-indigo-nodelet
Version:        1.9.8
Release:        0%{?dist}
Summary:        ROS nodelet package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nodelet
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libuuid-devel
Requires:       ros-indigo-bondcpp
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pluginlib >= 1.10.0
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       tinyxml-devel
BuildRequires:  boost-devel
BuildRequires:  libuuid-devel
BuildRequires:  ros-indigo-bondcpp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules >= 0.3.2
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pluginlib >= 1.10.0
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  tinyxml-devel

%description
The nodelet package is designed to provide a way to run multiple algorithms in
the same process with zero copy transport between algorithms. This package
provides both the nodelet base class needed for implementing a nodelet, as well
as the NodeletLoader class used for instantiating nodelets.

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

