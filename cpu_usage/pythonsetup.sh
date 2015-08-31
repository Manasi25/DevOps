#
# Script to run on each EC2 server
# Setup python-dev, pip, psutil
#

sudo apt-get install python-dev

wget https://bootstrap.pypa.io/get-pip.py

sudo python get-pip.py

sudo pip install psutil

sudo apt-get update
