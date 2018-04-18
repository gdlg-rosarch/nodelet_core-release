# Script generated with Bloom
pkgdesc="ROS - The nodelet package is designed to provide a way to run multiple algorithms in the same process with zero copy transport between algorithms. This package provides both the nodelet base class needed for implementing a nodelet, as well as the NodeletLoader class used for instantiating nodelets."
url='http://ros.org/wiki/nodelet'

pkgname='ros-lunar-nodelet'
pkgver='1.9.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-lunar-bondcpp'
'ros-lunar-catkin'
'ros-lunar-cmake-modules>=0.3.2'
'ros-lunar-message-generation'
'ros-lunar-pluginlib>=1.10.0'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'util-linux'
)

depends=('boost'
'ros-lunar-bondcpp'
'ros-lunar-message-runtime'
'ros-lunar-pluginlib>=1.10.0'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rospy'
'ros-lunar-std-msgs'
'util-linux'
)

conflicts=()
replaces=()

_dir=nodelet
source=()
md5sums=()

prepare() {
    cp -R $startdir/nodelet $srcdir/nodelet
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

