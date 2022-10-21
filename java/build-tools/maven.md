# Maven Build Tool `pom.xml (Project Object Model)`

Repository url: [https://mvnrepository.com]

## Why Maven ?

`Maven` is an Apache Software Foundation project automation tool.
`Maven` handles tasks ranging from:

* Complete Build process automation
* Dependencies management

**Note**
Maven uses `xml` to represent project structure, dependencies, etc... It can be used as build tool for Java, C#, Ruby, Groovy, etc... languages.

## Maven Architecture

(Local Repository) <-> Maven Build System <- (Http Requestx) -> (Remote Repository)

* Local repository -> Cache of project dependencies on the Local machine
* Remote repository -> Public repository hosting libraries.
* Build System -> Maven software for managing dependencies.

## Maven Lifecycle

* Default -> build lifecycle of the maven system
* Clean -> Clean previous maven builds
* Deploy -> Compile and prepare project for deployment && deploy package to a remote repository.

## Maven Plugin

Maven plugin are `Maven Goals` . Plugin are added to Maven default build system to run/execute a specific task in maven lifecycle phases.

Ex: `Compiler` plugin for instance has `compile:compile` (compile java code with resources) and `compileTest:compile` (compile java test sources), for compiling source codes.

## Project Object Model

* `groupId`

The main domain of the package. Used to group related packages together.

```xml
    <groupId>com.domain</groupId>
    <artifactId></artifactId>
```

* `artifactId`

Uniquely identify the package in repostories

```xml
    <groupId>com.domain</groupId>
    <artifactId>maven.testclient</artifactId>
```

* `version`

Version of the current project. `SNAPSHOT` is a standard in `pom` indicating the project is in active development state.

```xml
<project ...>
    <!-- ... -->
    <version>0.1.0-SNAPSHOT</version>
</project>
```

* `dependencies`

Dependencies provides the Maven Build System with information for packages and libraries required to build the current artifact.

- `scope`
The scope defines the enviroment in which dependency should be installed or required.

```xml
    <scope></scope>
```

```xml
<project ...>
    <!-- ... -->
    <dependencies>
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>4.0.0</version>
        </dependency>
    </dependencies>
</project>
```

* `build`

It provides the build configuration for the current project/artifact.

-- Plugins
    Build plugins are specified in `plugins` tag.

-- Build Configurations `configuration`
    Configure the Java SDK version to use for source and destination, etc...

```xml

    <configuration>
        <source>1.8</source>
        <target>1.8</target>
    </configuration>
```

```xml
<project ... >
    <!-- ... -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <!-- ... -->
        </plugins>
    </build>
    <!-- ... -->
</project>
```

* `properties`
Defines properties meta data for the current artifact.

```xml
<project ...>
    <properties>
        <!-- Source code encoding metadata -->
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <!-- JUnit Testing framework meta data -->
        <junit.version>5.7.1</junit.version>
    </properties>
</project>
```
