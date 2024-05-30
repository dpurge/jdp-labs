$plugins = Get-ChildItem $PSScriptRoot/plugins

foreach ($plugin in $plugins) {
    Write-Host "Installing: $($plugin.FullName)"
    docker cp $plugin.FullName jenkins:/var/jenkins_home/plugins/
}
