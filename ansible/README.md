# Ansible Lab

Choose `NATSwitch` when prompted.

```sh
vagrant up
vagrant ssh mgmt01
```

Install ansible:

```sh
sudo apt update
sudo apt install ansible
ansible localhost -m command -a hostname
ssh-keygen
ssh-copy-id mgmt01
ssh-copy-id lb01
ssh-copy-id web01
ssh-copy-id web02
ssh-copy-id db01
cd ~/data
ansible webstack -i hosts -m command -a hostname
```

## Update servers

```sh
ansible all -i hosts --become -m apt -a "update_cache=yes"
ansible proxy -i hosts --become -m apt -a "name=nginx state=present"
ansible webserver -i hosts --become -m apt -a "name=nodejs state=present"
ansible database -i hosts --become -m apt -a "name=postgresql state=present"
ansible database -i hosts --become -m service -a "name=postgresql state=started"
```

## Run playbook

```sh
ansible-playbook -i hosts -K playbook.yml
```

## Result

<http://192.168.200.101/>
