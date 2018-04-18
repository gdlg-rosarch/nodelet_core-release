# Script generated with Bloom
pkgdesc="ROS - A package for nodelet_topic_tools unit tests."
url='http://ros.org/wiki/nodelet_topic_tools'

pkgname='ros-kinetic-test-nodelet-topic-tools'
pkgver='1.9.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.68'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-nodelet-topic-tools'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rostest'
'ros-kinetic-std-msgs'
)

depends=('ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-nodelet-topic-tools'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=test_nodelet_topic_tools
source=()
md5sums=()

prepare() {
    cp -R $startdir/test_nodelet_topic_tools $srcdir/test_nodelet_topic_tools
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

