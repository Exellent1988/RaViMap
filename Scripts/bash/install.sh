#change swap size
sudo sed -i -- 's/CONF\_SWAPSIZE\=100/CONF\_SWAPSIZE\=500/g' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start


#Get raspi monitor
sudo apt-get install - y apt-transport-https ca-certificates
sudo wget http://goo.gl/rsel0F -O /etc/apt/sources.list.d/rpimonitor.list
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 2C0D3C0F 
sudo apt-get update
sudo apt-get install -y rpimonitor
sudo /usr/share/rpimonitor/scripts/updatePackagesStatus.pl


#OLA DEPENDENCIES
sudo apt-get update
sudo apt-get install -y libcppunit-dev libcppunit-1.13-0 uuid-dev pkg-config libncurses5-dev libtool autoconf automake g++ libmicrohttpd-dev \
 libmicrohttpd10 protobuf-compiler libprotobuf-lite9 python-protobuf libprotobuf-dev libprotoc-dev zlib1g-dev bison flex make libftdi-dev  libftdi1 libusb-1.0-0-dev liblo-dev libavahi-client-dev

 #make OLA
 git clone https://github.com/OpenLightingProject/ola.git ola
 cd ola
 autoreconf -i
 ./configure --enable-rdm-tests  --enable-gcov --enable-ja-rule --enable-python-libs --enable-rdm-tests --no-create --no-recursion
make -j4 all
make -j4 check
sudo make -j4 install
sudo ldconfig
