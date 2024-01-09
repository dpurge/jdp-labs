plugins {
    id("my-application")
}

dependencies {
    implementation(platform("com.example:platform"))

    implementation(project(":data-model"))
    implementation(project(":business-logic"))
    
    // implementation("org.apache.commons:commons-lang3")
    // runtimeOnly("org.slf4j:slf4j-simple")
    
    implementation(libs.commons.lang)
    runtimeOnly(libs.slf4j.simple)
}

application {
    mainClass.set("com.example.MyApplication")
}
