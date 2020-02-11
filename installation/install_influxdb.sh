#!/bin/bash

echo Installing InfluxDB!

sudo curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -

source /etc/lsb-release

echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt update
sudo apt install influxdb -y
sudo systemctl start influxdb
sudo systemctl enable influxdb

echo "now installing influxdb python"

pip install influxdb
pip install --upgrade influxdb

echo "execute [$netstat -plntu] and check influxdb running"

