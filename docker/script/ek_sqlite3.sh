#!/bin/sh

set -e
yum update -y

echo EKKE
yum install -y wget tar gzip

cd /opt
wget https://www.sqlite.org/2022/sqlite-autoconf-3380200.tar.gz
tar -zxvf sqlite-autoconf-3380200.tar.gz

cd sqlite-autoconf-3380200
yum groupinstall "Development Tools" -y
./configure
make
make install

cp /opt/sqlite-autoconf-3380200/.libs/libsqlite3.so.0 /usr/lib64/.
cp /opt/sqlite-autoconf-3380200/.libs/libsqlite3.so /usr/lib64/.
cp /opt/sqlite-autoconf-3380200/.libs/libsqlite3.so.0.8.6 /usr/lib64/.

yum clean all