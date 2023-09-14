#!/bin/sh

echo -n 'Adding IP to hosts file: '
echo $1
echo -n 'Host name is: '
echo $2

echo "$1 $2" >> /etc/hosts