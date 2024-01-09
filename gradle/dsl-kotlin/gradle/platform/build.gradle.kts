plugins {
    id("java-platform")
}

group = "com.example"

javaPlatform.allowDependencies()

dependencies {
    api(platform("com.fasterxml.jackson:jackson-bom:2.16.0"))
    api(platform("org.junit:junit-bom:5.8.2"))
}

dependencies.constraints {
    api("org.apache.commons:commons-lang3:3.12.0")
    api("org.slf4j:slf4j-api:2.0.5")
    api("org.slf4j:slf4j-simple:2.0.5")

    api("com.google.guava:guava:20.0-jre")
}