import com.example.gradle.CountJars

plugins {
    id("application")
    id("my-java-base")
}

tasks.register<Zip>("bundle") {
    group = "My Group"
    description = "My Description"

    from(tasks.jar)
    from(configurations.compileClasspath)

    destinationDirectory.set(layout.buildDirectory.dir("distribution"))
}

tasks.register<CountJars>("countJars") {
    group = "My Group"
    description = "Count jar files"
    listJars.from(tasks.jar)
    listJars.from(configurations.compileClasspath)

    resultFile.set(layout.buildDirectory.file("txt/count.txt"))
}

tasks.build {
    dependsOn(tasks.named("bundle"))
}

tasks.register("doAll") {
    group = "My Group"
    description = "Do all my tasks"

    dependsOn(tasks.build)
    dependsOn(tasks.named("countJars"))
}