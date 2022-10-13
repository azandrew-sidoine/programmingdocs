# Introduction

JavaFx is a UI library framework for building modern UI applications. It's based on Java and uses XML to represent the UI (even though the UI can be design using Java itself as well).

**Note**
A JavaFX application is controlled by the JavaFX platform, a runtime system that builds your application object and constructs the JavaFX Application Thread.

## Application

The `Application class` represent a JavaFx application instance. Any javafx application must inherit from the base `Application` class.

* Application class method

> `launch()` -> internally written in the `Application` base class that will call the startup abstract method ovewritten in subclasses

> `start(State  stage)` -> Looks like the initialization method of the application. This is where application bootstrap codes must be called.

**Note**

`Stage` -> Screens of JavaFX applications, are called `Stage` , we represent a view in JavaFx application.
`Scene` -> It's the current frame of the application view

**Note**
`Stage.show()` -> `show()` method brings the application in the front of OS stack.
`Stage.setScene(Scene s)` -> `setScene()` set the current frame to show to the application user.

```java
package dev.domain.app;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Stage;
import javafx.scene.Scene;

import java.io.IOException;

public class AppName extends Application
{
    @Override()
    public void start(Stage s) throws IOException
    {
        // Load an xml view using the FXMLLoader
        FXMLLoader loader = new FXMLLoader(AppName.class.getResource('xml-file.fxml'));
        // Creating a view
        s.setTitle('App Title');
        s.setScene(new Scene(loader.load(), width, height));
        s.show();
    }

    // Main entry point of the application
    public static void main(String[] args) {
        launch();
    }

}
```

## Architecture

You must always construct and modify the Stage and its scene objects on the JavaFX Application Thread. Note that JavaFX (like Swing) is a single-threaded UI model.

**Warning**
Any Long running task on a UI thread will likely block the Application, thus long running task, or async task must be delegated to it own thread or use concurrency model.

    **Note**
    Fortunately, JavaFX has a well-developed concurrency API that helps developers assign long-running tasks to one or more separate threads.

> `State` -> `Scene` -> `JavaFx Elements Tree`

**Note**
JavaFx Element like HTML element for a DOM (Document Object Model) having a root node. Each node has at least 1 parent `Node` (except for the root node), and 0 or more `Child Nodes` .

* Mathematical Representation (2D by default)

JavaFx element follow a 2D representation structure of (x, y) coordinate.

> `x` -> Left to Right
> `y` -> Top to Bottom

**Note** JFX can in fact also support 3D structure to represent elements in the space (3D Rendering).

## JFX Components

### Layout

Layout are JFX controls in which group other controls. They apply positionning to their children as group.

Layout controls are extremely important in managing your scene graph. These controls not only arrange components for you but also respond to events such as resizing, the addition or removal of elements, and any changes to the sizes of one or more nodes in the scene graph.

**Warning** JFX controls can never be directly added to the scene. They are added to a layout container first and the layout container is the added to the scene.

> `LayoutElement.getChildren().addAll(...)` -> Add a list of element to the element children property
> `LayoutElement.getChildren().add(Control)` -> Add a control to the element children property

**Note** Method defines here get apply to any layout element

#### Group `javafx.scene.layout.Group`

It's a Layout element that group it children but does not provides any capability of positioning then on the scene.
A `Group` will position all it element at (0, 0) coordinate by default.

#### Stack Pane `javafx.scene.layout.StackPane`

JFX `StackPane` class is a class that present it children as stack (Depth -> Top).

**Note**
By default it center all of it children.

> `StackPane.setAlignment(Control, Pos) | StackPane.setAlignment(Pos)` -> Set the alignment of a child control | all it children `javafx.scene.layout.Pos` (BOTTOM_CENTER, TOP_LEFT, TOP_RIGHT, etc...), has a list of positionning constant to use to position elements.

```java
// Programmatically adding ui elements
//...
import javafx.layout.StackPane;

// ...
StackPane stack = new StackPane();
stack.getChildren().addAll(Element, Element, ...);
```

#### AnchorPane `javafx.scene.layout.AnchorPane`

AnchorPane manages its children according to configured anchor points, even when
a container resizes.

It's basically use as top level control to control margin of the elements even if the window is resized. It's can be consider a Container element.

> `AnchorPane.setLeftAnchor(Control, int)` -> Position the element `int` pixel from the left
> `AnchorPane.setBottomAnchor(Control, int)` -> Position the element `int` pixel from the bottom

```java
AnchorPane anchorPane = new AnchorPane();
Label label = new Label("My Label");
anchorPane.getChildren().add(label);
AnchorPane.setLeftAnchor(label, 10.0);
AnchorPane.setBottomAnchor(label, 10.0);

```

#### GridPane `javafx.scene.layout.GridPane`

It's a 2-dimentional grid layout positionning control.

**Note**
Components can span rows and/or columns, but the row size is consistent for all components in a given row.

> `GridPane.add(Control, int r, int c, [int rowSpan, int colSpan])` -> `add()` method of the GridPane class, use cell coordinates to position elements.

#### FlowPane and TilePane `javafx.scene.layout.FlowPane`

FlowPan is like a `flexbox` element. It either manages its children in either a horizontal or vertical flow.

> `setOritation(javafx.scene.layout.Orientation.VERTICAL|javafx.scene.layout.Orientation.HORIZONTAL)` -> Defines the orientation of the `FlowPane` children

```java
FlowPane flex = new FlowPane(javafx.scene.layout.Orientation.VERTICAL);
```

**Note**
The default orientation is horizontal.
FlowPane wraps child nodes according to a configurable boundary. If you resize a pane that contains a FlowPane, the layout will adjust the flow as needed. The size of the cells depends on the size of the nodes, and it will not be a uniform grid unless all the nodes are the same size.

`TilePane` is similar to `FlowPane` unless it cell size are similar ( `flexbox` ).

### BorderPane `javafx.scene.layout.BorderPane`

BorderPane is convenient for desktop applications with discreet sections, including a top toolbar (Top), a bottom status bar (Bottom), a center work area (Center), and two side areas (Right and Left)

> `BorderPane.setAlignment(Control, Pos.CENTER)` -> static method to set the alignment of a control in the pane
> `BorderPane.setMargin(Control, new Insets(top, right, bottom, left))` -> Static method to set the margins of a conrol in the layout

```java
import javafx.scene.layout.BorderPane;

BorderPane borderPane = new BorderPane();
```

**Note**
Note that BorderPane uses a center alignment by default for the center area and a left alignment for the top.

#### SplitPane `javafx.scene.layout.SplitPane`

`SplitPane` split the layout space into multiple horizontally or vertically configured areas. The divider is movable, and you typically use other layout controls in each of SplitPane’s areas.

#### HBox, VBox, and ButtonBar

The `HBox` and `VBox` layout controls respectively provide single `horizontal` or `vertical` placements for child nodes.

`ButtonBar` is convenient for placing a row of buttons of equal size in a horizontal container. It act like a `button group` component.

### Controls

**Note** Any method defines here is applicable to any control element

> `Control.getLayoutBounds(): { getWidth(): int|float, getHeight(): int|float }` -> Get the inner width and height of the parent element
> `Element.setX(int)` -> Absolute positionning of the element on the view on the horizontal axis
> `Element.setY(int)` -> Absolute positionning of the element on the view on the vertical axis
> `Element.setOnMouseClicked(Lambda)`

```java
text.setOnMouseClicked(mouseEvent -> {
            System.out.println(mouseEvent.getSource().getClass()
                 + " clicked.");
});
```

#### Text Control `javafx.scene.text.Text`

Text control is a control of the `javafx.scene.text` namespace, used to print text to the end user. It has styling property to customize the font, the weight, the color, etc... of the control.

> `Text.setFont(javafx.scene.text.Font f)` -> Set the font of JFX text control.

```java
// ...
import javafx.scene.text.Text;
import javafx.scene.text.Font;

// Create a Text shape with font and size
Text text = new Text("My Shapes");
text.setFont(new Font("Arial Bold", 24));
```

### Paint

`javafx.scene.paint` namespace contain classes for painting an application scene.

#### Color `javafx.scene.paint.Color`

`Color` class is a member of `javafx.scene.paint` namespace use to adding color to element of the scene or the scene itself. It has predefine color constant like `Color.LIGHTBLUE` , `Color.GREEN` , etc... and the contructor of the class also allow to create colors from RGB standards.

> `Color.web('#hex')` -> Create a JFX color using web color standard
> `Color.rgb(R, G, B, opacity)` -> Create JFX color using web standard

#### Gradient

Gradients give depth to a shape and can be either radial or linear.

```java
// This program degrades the background of the control in 2 stop, 0 -> .5, .5 -> 1.0
import javafx.scene.paint.Stop;
import javafx.scene.paint.LinearGradient;
import javafx.scene.paint.CycleMethod;

// Creates a list stop for a linear gradient
Stop[] stops = new Stop[] { new Stop(0, Color.DODGERBLUE),
                new Stop(0.5, Color.LIGHTBLUE),
                new Stop(1.0, Color.LIGHTGREEN)};
// startX=0, startY=0, endX=0, endY=1
// Makes a vertical gradient startX=0, startY=0, endX=1, endY=0
LinearGradient gradient = new LinearGradient(0, 0, 0, 1, true,
                CycleMethod.NO_CYCLE, stops);
```

**Note**
`Boolean` true indicates the gradient stretches through the shape (where 0 and 1 are proportional to the shape), and `NO_CYCLE` means the pattern does not repeat. Boolean false indicates the gradient’s x and y values are instead relative to the local coordinate system of the parent.

* Linear Gradient

`Linear gradients` require two or more colors, called Stops. A gradient `stop` consists of a color and an offset between 0 and 1.

#### DropShadow

They are effects that can be added to control to add a `box shadow` to the control.

> `Control.setEffect(new DropShadow(nPixel, offsetX, offsetY, Color))` -> Add an effect to the control

**Note** For `DropShadow` or `BoxShadow` , When the offsets are 0, the shadow surrounds the entire shape, as if the light source were shining directly above the scene.

#### Reflection

A reflection effect mirrors a component and fades to transparent, depending on how you configure its top and bottom opacities, fraction, and offset.

> `Reflection.setFraction()` -> Reflection fraction of the reflected object

> `Reflection.setTopOffset()` ->  The offset specifies how far below the bottom edge the reflection starts in pixels

```java
import javafx.scene.effects.Reflection;

Reflection r = new Reflection();
r.setFraction(.8); // .8 for the fraction, so that the reflection will be eight-tenths
// of the reflected component
r.setTopOffset(1.0); // Vertical offset the reflection. Default:0
text.setEffect(r);
```

## Animations

JavaFX makes animation very easy when you use the built-in transition APIs. Each JavaFX Transition type controls one or more Node (or Shape) properties.

### Transition

It is the base class for most transition in the Fx framework. 

**Note**
If a transition is applied on a Group of controls, all element of the control will inherit the animation when it start.

> `Transition.setDelay(n)` -> Delay the transition for the given time before playing it
> `Transition.onFinished(Lambda)` -> Execute a callback after a given transition
> `Transition.play()|Transition.playFromStart()` -> Start palying the animation. `play()` will resume a transition at a given point in time, while `playFromStart()` will always start the transition from the begenning.
> `Transition.pause()` -> Pauses the animation
> `Transition.stop()` -> Stops the animation
> `Transition.getStatus():  Animation.Status.RUNNING|Animation.Status.PAUSED|Animation.Status.STOPPED` -> Returns the status of the animation

### RotateTransition

> `new RotateTransition(Duration d, Control c)` -> Creates a new rotate animation

```java
// Define RotateTransition
RotateTransition rotate = new RotateTransition(
                Duration.millis(2500), new StackPane());
rotate.setToAngle(360);
rotate.setFromAngle(0);
rotate.setInterpolator(Interpolator.LINEAR);
```

### FadeTransition

It controls a node’s opacity, varying the property over time. Fade value is comprise between `0 -> 1 (Fully opaque)`

### TranslateTransition

Move element on the scene by modifying/translating it `x` and `y` positions, or even `z` in 3D representation.

### ParallelTransition

Plays multiple transition in parallel.

### SequentialTransition

Play transitions sequencialy.

### PauseTransition

Control the timing between 2 sequential transition

## JFX Properties

**Note** JavaFX Properties
JavaFX Node/Controls, have properties that are private but has getters and setter (for updating them).
Most JFX properties are observables, meaning UI is notified each time the property changes, making it easy for developper to bind and work with controls properties.

**Note**
Because JavaFX properties are observable, you can define listeners that are notified when a property value changes or becomes invalid ().

**Note**
In order to use bind expressions or attach listeners to JavaFX properties, you must access a property through its property getter. A property getter is the name of the property suffix by `Property` .
Ex:

> For `font` property, it getter is `fontProperty(): Observable<{ getName(): string, getValue(): Font }>`

### Property Listeners

JavaFX property listeners that apply to object `properties` (not collections) come in two flavors: `invalidation listeners` and `change listeners` .

#### Invalidation Listener

Invalidation listeners fire when a property’s value is no longer valid. Invalidation listeners have a single method that you override with lambda expressions.

```java
// This assume a rotation transition was previously created
// Using the InvalidationListner object, we listen to when the property gets invalidated
// Here we listen for status property of a RotationTransition
rotate.statusProperty().addListener(new InvalidationListener() {
    @Override
    public  void invalidated(Observable observable) {
        // Because the observable is nongeneric, you must apply an appropriate type cast to access the property value
        text2.setText("Animation status: " + ((ObservableObjectValue<Animation.Status>)observable)
                                                .getValue());
    } 
});

// or using lambda expression
// Here we just reduce the boilerplate code that cast the observable getValue()
rotate.statusProperty().addListener(observable -> {
    text2.setText("Animation status: " +
        rotate.getStatus());
});
```

#### Change Listener (NgOnChanges)

When you need access to the previous value of an observable as well as its `current value`, use a change listener. Change listeners provide the observable and the new and old values.

```java
rotate.statusProperty().addListener(new ChangeListener<Animation.Status>() {
        @Override
        public void changed(ObservableValue<? extends Animation.Status> observableValue, Animation.Status oldValue, Animation.Status newValue) {
                text2.setText("Was " + oldValue + ", Now " + newValue);
        }
});
// Here’s the version with a more compact lambda expression:
rotate.statusProperty().addListener(
            (observableValue, oldValue, newValue) -> {
    text2.setText("Was " + oldValue + ", Now " + newValue);
});
```

**Note**
We can see that using a lambda expression, difference between invalidation and change listeners is a matter of parameter lists.


### Property Binding

JavaFX binding is a flexible, API-rich mechanism that lets you avoid writing listeners in many situations. You use binding to link the value of a JavaFX property to one or more other JavaFX properties.

#### Unidirectional Binding (Data flow one way, Right -> Left)

> `Control.nameProperty().bind(Control2.name2Property())` -> Means that any changes on the `Control2` `name2` property, will update the `Control` `name` property.

**Note**
`name` and `name2` must be of the same type for this to work.

**Note**
Note that when you bind a property, you cannot explicitly set its value unless you unbind the property first.

#### Bidirectional Binding

Bidirectional binding provides a two-way relationship between two properties. When one property updates, the other also updates. Here’s an example with two text properties:

> `Control.nameProperty().bindBidirectional(Control2.name2Property())`

**Note**
Unlike bind(), you can explicitly set either property when using bidirectional binding.

#### Fluent API

The fluent and bindings APIs help you construct bind expressions when more than one property needs to participate in a binding or when it’s necessary to perform some sort of calculation or conversion.

```java
// The rotate property of the stack pane is of float type, therefore, the value must be modify before setting the text property of the text2 control
text2.textProperty().bind(stackPane.rotateProperty().asString("%.1f"));

// Handled a more complex case using When(Observable)
//                                  .isEqualTo(state)
//                                  .then(doneSomething)
//                                  .otherwise(default)
text2.strokeProperty().bind(new When(rotate.statusProperty()
               .isEqualTo(Animation.Status.RUNNING))
               .then(Color.GREEN).otherwise(Color.RED));
```
