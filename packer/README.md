# Packer Labs

```pwsh
Remove-NetFirewallRule -DisplayName "Packer_http_server" -Verbose
New-NetFirewallRule -DisplayName "Packer_http_server" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8000-9000
Get-VMHostSupportedVersion
```

```pwsh
packer init --upgrade config.pkr.hcl
```
