# RasViMap
#INSTALL NOTES

##POCO
cd ~<br>
wget http://pocoproject.org/releases/poco-1.7.2/poco-1.7.2-all.tar.gz<br>
tar xzfv poco-1.7.2-all.tar.gz<br>
cd poco-1.7.2-all/<br>
./configure --omit=Data/ODBC,Data/MySQL<br>
make -j4<br>
sudo make -s install<br>

##openframework
wget http://openframeworks.cc/versions/nightly/of_latest_linuxarmv7l_nightly.tar.gz<br>
nano .bashrc<br>
add<br><code>
'# This reads .bash_aliases file for aliases<br>
if [ -f ~/.bash_aliases ]; then               <br>  
. ~/.bash_aliases<br>
fi'<br>
</code><br>
nano .bash_aliases<br>
add <br>
<code>
  alias oF='cd /home/pi/openFramework'
  alias projectgenerator='oF && ./apps/projectGenerator/commandLine/bin/projectGenerator'
  # Read temperature of rPi
  alias temp='/opt/vc/bin/vcgencmd measure_temp'
 </code><br>
nano .bash_profile<br>
<code>
export MAKEFLAGS=-j4 PLATFORM_ARCH=armv7l PLATFORM_VARIANT=rpi2
</code><br>
mkdir openFramework<br>
tar vxfz of_latest_linuxarmv7l_nightly.tar -C openFramework --strip-components 1<br>
cd ~/openFramework/scripts/linux/debian<br>
./install_dependencies.sh<br>
./install_codecs.sh<br>
cd ~<br>
export MAKEFLAGS=-j4 PLATFORM_ARCH=armv7l PLATFORM_VARIANT=rpi2 <br>
make Release -C /home/pi/openFramework/libs/openFrameworksCompiled/project<br>
cd ~/openFramework/scripts/linux/<br>
nano buildallRPIexamples.sh<br>
change <code></code><br>to<br><code></code><br>
