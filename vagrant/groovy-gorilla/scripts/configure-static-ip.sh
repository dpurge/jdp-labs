#!/bin/sh

echo -n 'Setting static IP address: '
echo $1
echo -n 'Setting gateway address: '
echo $2

cat << EOF > /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses: [$1/24]
      gateway4: 192.168.200.1
      nameservers:
        addresses: [8.8.8.8,8.8.4.4]
EOF