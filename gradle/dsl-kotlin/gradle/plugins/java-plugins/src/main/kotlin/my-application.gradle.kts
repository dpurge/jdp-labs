plugins {
    id("application")
    id("my-java-base")
}

tasks.register<Zip>("bundle") {
    // from("src")
    // include("**/*.txt")
    // getDestinationDirectory().set(file("build"))
    // archiveFileName = "myBundle.zip"
    from(tasks.jar)
    from(configurations.compileClasspath)
    destinationDirectory.set(layout.buildDirectory.dir("distribution"))
    group = "My Group"
    description = "My Description"
}