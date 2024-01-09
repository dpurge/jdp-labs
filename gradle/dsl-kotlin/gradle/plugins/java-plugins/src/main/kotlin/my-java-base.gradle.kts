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
