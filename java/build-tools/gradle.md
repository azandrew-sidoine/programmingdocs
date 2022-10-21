# Gradle build Tool

## What is Gradle?

Gradle is a build automation tool known for it flexibility to build sofware.
It's primary used for Java based project, but can be extended to other language (Scala, Groovy, C/C++, Android, etc..) based project using plugins.

Gradle handles task like compilation, linking and code packagist for deployment.

## How is gradle different from Maven

- <Gradle uses groovy based Domain specific language, (meaning it configuration files is written in groovy), while Maven is using `xml`.

- <The goal of `Gradle` is to add functionality to a project, while `Maven` goal is related to project phases.

- `Gradle is more dynamic and customizable`-> <Gradle is based on graph of Task & dependencies where `Maven` is based on the phases of linear and fixed model.

- <Gradle works on the tasks that have been changed to give better performance, while `Maven` does not have build cache making build task slow

- <Gradle tries to fixes the cons of using `Maven` and `Ant` to create a modern build

## Why is Gradle used ?

- Gradle helps focuses on maintanbility, flexibility and performances
- Lot of plugins, and features

## Gradle installation

1) Check system for requirements
2) Download & Install Gradle [https://gradle.org/install]
3) Configure & Setup environment variables
4) Test gradle installation

## Gradle Core concepts

- Project
It represents a `task` that must be done, like deploying application to stagging environment.

**Note**
Gradle project itself if set of small configured tasks to execute in sequence.

- Tasks

It's a piece of work performed by a build. Tasks can be compiling classes, creating JAR files, making Javadoc, or publishing some archives.

- Build Scripts `build.gradle`

A build script is located in the root directory of project. It contains, dependencies, artifact configuration, etc...

**Note**
Every Gradle build consist of 1 or more projects.

## Features of gradle

- High Performance (Make use of an internal cache)
- Provides support on how the build must be performed.
- Multi-Project build system
- Incremental builds
- Build Scans, to scan the source code and understand how the build has been performed.
- Familiarity with Java

## Java Project with Gradle

- `apply`
It's like an import statement that set the plugins to be used by the gradle task.

```groovy
// build.gradle

apply plugin: 'java'
apply plugin: 'application'
```

- `dependencies`

Specify project(s) dependencies.

```syntax
dependencies {
    implementation 'package:<version>'
    testImplementation 'package:<version>'
    api 'package:<version>'
}
```

```groovy
dependencies {
    // Use JUnit test framework
    testImplementation 'junit:junit:4.13'

    // 
    implementation 'com.google.guava:guava:29.0-jre'
}
```

- `repositories`

Specify the list of repositories to be used by the gradle build tools.

```groovy

repositories {
    jcenter()
}
```

- `plugin`

List of plugin to apply to the build automation.

```groovy
plugins {
    // Apply the java-library plugin for API and implementation separation
    id 'java-library'
}
```

**Note** Gradle commands
> gradle tasks [-v] -> returns the list of tasks that can be configured
> gradle clean build [-v] -> Clean the gradle repository
