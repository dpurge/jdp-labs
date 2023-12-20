pluginManagement {
    repositories {
        mavenCentral()
    }

    includeBuild("gradle/plugins")
}

dependencyResolutionManagement {
    repositories {
        mavenCentral()
    }
}

rootProject.name = "dsl-kotlin"

include ("app")
include ("business-logic")
include ("data-model")
