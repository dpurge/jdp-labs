plugins {
    id("my-java-library")
}

dependencies {
    implementation(platform("com.example:platform"))

    implementation(project(":data-model"))

    implementation("org.apache.commons:commons-lang3")
    implementation("org.slf4j:slf4j-api")
    implementation("org.apache.commons:commons-lang3")
}