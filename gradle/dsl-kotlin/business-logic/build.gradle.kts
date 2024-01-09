plugins {
    id("my-java-library")
}

dependencies {
    implementation(platform("com.example:platform"))

    implementation(project(":data-model"))

    // implementation("org.apache.commons:commons-lang3")
    // implementation("org.slf4j:slf4j-api")
    
    implementation(libs.commons.lang)
    implementation(libs.slf4j.api)

    testImplementation("org.junit.jupiter:junit-jupiter-api")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine")

    // integrationTestImplementation("org.junit.jupiter:junit-jupiter-api")
    // integrationTestRuntimeOnly("org.junit.jupiter:junit-jupiter-engine")
}