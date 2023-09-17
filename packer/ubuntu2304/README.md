# Ubuntu 23.04 (Lunar Lobster)

- <https://github.com/maroskukan/packer-cookbook/tree/main/boxes/ubuntu2304>
- <https://medium.com/@maros.kukan/automating-golden-image-builds-with-packer-3b1c6010b467>

```sh
packer init ./box-config.pkr.hcl
packer validate ./box-config.pkr.hcl
packer build -only=hyperv-iso.efi ./box-config.pkr.hcl
```

```sh
packer console box-config.pkr.hcl
```
