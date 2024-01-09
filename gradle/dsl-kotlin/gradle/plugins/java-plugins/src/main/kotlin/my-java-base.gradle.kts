// import com.example.gradle.Slf4jSimpleRule

plugins {
    id("java")
}

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(21))
}

// tasks.compileJava {
//     options.encoding = "UTF-8"
//     options.compilerArgs.addAll(listOf("-Xlint:unchecked", "-Xlint:deprecation"))
// }

// tasks.compileTestJava {
//     options.encoding = "UTF-8"
//     options.compilerArgs.addAll(listOf("-Xlint:unchecked", "-Xlint:deprecation"))
// }

// Check in the implementation
// do it carefully when selecting tasks by type
tasks.withType<JavaCompile>().configureEach {
    options.encoding = "UTF-8"
    options.compilerArgs.addAll(listOf("-Xlint:unchecked", "-Xlint:deprecation"))
}

dependencies.components {
    withModule<Slf4jSimpleRule>("org.slf4j:slf4j-simple")
}

// sourceSets.main {
//     java.setSrcDirs(listOf(layout.projectDirectory.dir("sources")))
// }

tasks.test {
    useJUnitPlatform {
        excludeTags("slow")
    }
    maxParallelForks = 2
    maxHeapSize = "1g"
}

tasks.register<Test>("testSlow") {
    testClassesDirs = sourceSets.test.get().output.classesDirs
    classpath = sourceSets.test.get().runtimeClasspath

    useJUnitPlatform {
        includeTags("slow")
    }
}

tasks.register<Test>("integrationTest") {
    testClassesDirs = sourceSets["integrationTest"].output.classesDirs
    classpath = sourceSets["integrationTest"].runtimeClasspath

    useJUnitPlatform()
}

tasks.check {
    dependsOn("testSlow")
}