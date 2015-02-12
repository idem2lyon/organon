#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	clear
	echo "This script must be run as root" 1>&2
	exit
fi
#Check if already installed
if [ -e /opt/organon ]
then
	rm -rf /opt/organon
fi

if [ -e /usr/bin/organon ]
then
	rm /usr/bin/organon
fi

#end check

#Install Dependencies
apt-get install ruby-full python libmysqlclient-dev rubygems
gem install mysql

#Move organon to opt
cd .. && mv organon /opt/

echo \#\!/bin/bash >> /usr/bin/organon
echo cd /opt/organon >> /usr/bin/organon
echo exec python organon.py \"\$\@\" >> /usr/bin/organon

chmod +x /usr/bin/organon
chmod +x /opt/organon/src/*

echo '[+] Complete!'
echo 'Type "organon" in order to use it'
