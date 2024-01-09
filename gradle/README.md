# Gradle lab

```sh
brew install gradle
gradle wrapper
```

Build:

```sh
./gradlew tasks
./gradlew :app:tasks
./gradlew build
./gradlew test
./gradlew run
./gradlew clean
./gradlew bundle # custom task
./gradlew :app:bundle --console=plain
./gradlew :app:count --console=plain
```