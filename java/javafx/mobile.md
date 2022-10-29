# Native Mobile Apps for iOS and Android (Gluon)

Java started as a programming language for embedded devices. In the early nineties, a team inside Sun Microsystems worked on a software stack for a set of next generation hardware products.

## Different Approaches for Mobile Apps

Using OS-specific native controls, as is the case in approach 3, allows for a real smooth integration with the native operating system. In this case, the native controls (e.g., buttons, labels, lists, etc.) are used to render the user interface. For the end user, this is convenient, as he recognizes the typical UI components he also uses in other apps.

Moreover, the OS-specific native controls are subject to fast changes. While many end users love the fast innovation in those environments, for software developers, it is often problematic as they have to upgrade their native apps very often or risk that they are outdated.

## Mobile Web Sites

The simplest approach is often simply creating a mobile-friendly web site and have that rendered in the mobile browser that is available on mobile devices – optionally integrated with an app icon so that users can start the application more easily.

## Device Native Rendering

The JavaFX approach falls into the second category. JavaFX has its own set of controls, and developers can easily create their own controls. The rendering of JavaFX is done on top of the hardware-accelerated drivers on the target platform. At this moment, 
the rendering pipelines for both JavaFX for iOS and JavaFX for Android use OpenGL, using the same code as the rendering on Mac OS X and Linux.

## The Development Flow

While it is, at least in theory, possible to create a mobile app and only test/run it on a mobile device, it is highly recommended to work on desktop first.

A typical deployment cycle contains a number of steps:

    • Write some code.
    • Compile the code.
    • Run the code.
    • Test if the output and behavior is as expected.

* javafxplugin
`javafxplugin` is the general plugin for developing JavaFX applications and dealing with the JavaFX modules and dependencies. This is the plugin you typically use for developing JavaFX applications.

* client-gradle-plugin
`client-gradle-plugin` is Gluon’s plugin that is capable of cross-compiling code for iOS and Android devices.

* Configure maven repository

```groovy
pluginManagement {
    repositories {
        maven {
            url "https://nexus.gluonhq.com/nexus/content/repositories/
            releases"
}
        gradlePluginPortal()
    }
}
```

### Requirements

* OpenJDK 11.0.2 or later
* AdoptOpenJDK
* JAVA_HOME environment variable
* LLVM 6.0 or later and add LLVM binaries path to environment

## Gluon Framework

### Using the Plugin Options

* bundlesList
A list of additional full qualified bundle resources that will be added to the default bundles list that already includes

    – com/sun/javafx/scene/control/skin/resources/controls
    – com.sun.javafx.tk.quantum.QuantumMessagesBundle

For instance, if you are using a resource bundle for internalization purposes, like `src/resources/hellofx/hello.properties` (and hello_EN.properties and others), you will need to include, using Gradle:

```groovy
bundlesList = ["hellofx.hello"]
```

* resourcesList
A list of additional resource patterns or extensions that will be added to the default resources list that already includes:
    – png, gif, jpg, jpeg, bmp,
    – ttf, css, fxml, json,
    – frag, gls, license

For instance, if you are using a properties file (not included as a resource bundle), like src/resources/hellofx/logging.properties, you will need to include, using Gradle,

```groovy
resourcesList = ["properties"]
```

* reflectionList

A list of additional full qualified classes that will be added to the default reflection list that already includes most of the JavaFX classes.
The current list is added to file under `build/client/gvm/reflectionconfig- $target.json`.

If you are using FXML in your project, since the FXMLLoader uses reflection to inspect the FXML file, you will need to add a few classes from this file to the reflection list: mainly the FXMLLoader itself (“javafx.fxml.FXMLLoader”), the controller class, and the controls classes (the containers are already included in this list).

```groovy
reflectionList = ["javafx.fxml.FXMLLoader"]
```

* jniList

A list of additional full qualified classes that will be added to the default jni list that already includes most of the JavaFX classes.
The current list is added to file under `build/client/gvm/jniconfig-$target.json`.

* delayInitList
A list of additional full qualified classes that will be added to the default delayed initialization list.

* releaseSymbolsList
A list of additional JNI functions that will be added to the default release symbols list that already includes most of the JNI methods.
The current list is added to file under `build/client/gvm/release.symbols`.

## Mobile Native Look

**Note** Provides a platform service

```java
public class Platform {

    static boolean ios() {
        return System.getProperty("os.name").equals("ios");
    }

    static boolean android() {
        return System.getProperty("os.name").equals("android");
    }
}
```

### Glisten

[see https://docs.gluonhq.com/charm/5.0.2/#_charm_glisten]
Provides mobile styled look for existing JavaFX controls and compoments.
