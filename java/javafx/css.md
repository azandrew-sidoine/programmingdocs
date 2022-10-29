# Mastering Visual and CSS Design

## Introduction

* syntax

```css
selector [>childSelector] {
    property: value;
    /* CSS declaration */
}

selector [childSelectors] {
    property: value;
    /* CSS declaration */
}
```

> property = -fx- `hyphen(JavaFXProperty)` -> Ex: backgroundColor = -fx-background-color

**Note**
`JavaFX` Css dialect uses `-fx-` prefix to define properties, to distinguish them from web standards, b'cause most `jFX` are name after web standard properties.

```css
label {
    -fx-background-color: black;
    -fx-text-fill: white;
    -fx-padding: 10px;
}
```

**Note**
`.root` refers to the root of the scene of the destop application.

* Using the css in jFx application

> Scene.add(...) -> Add a stylesheet to the javaFX application Scene.

```java

public void start(Stage primaryStage) {
    Label label = new Label('...');
    VBox root = new VBox(label);
    Scene scene = new Scene(root, 200, 100);

    // This assume resources/styles.css exists in the project structure
    // 
    scene.getStylesheets().add(getClass().getResource("styles.css").toExternalForm());

    // ...
    primaryStage.show();
}
```

**Note** Styles inheritance
Just like the Web DOM, styles are applied to `Nodes` of the application and `Child Nodes` ihnerit from parent styles.

## Selector

Selectors are `class` (.classSelector) based or `id` (#idSelector) based, or `tag` based.

> classSelector = . `hyphen(NodeClassName)` -> Ex: ListView = .list-view
> idSelector = # `hyphen(NodeClassName)` -> Ex: #my-card

**Note**
ID are manually assigned to the node in `fxml` temlate or Java code.

## Applying styles

A stylesheet is usually used as a resource in your application, and thus the Java resource API is the best way to load it.

* Scnene stylesheets property

```java
// Application Root page
scene.getStylesheets().add(
     getClass().getResource("styles.css").toExternalForm()
);

// Or using url resource
scene.getStylesheets().add(
     getClass().getResource("http://website/folder/styles.css").toExternalForm()
);
```

* Global level (Applied to all Scene)

Passing null will return your application to the default stylesheet.

```java
//
Application.setUserAgentStylesheet( STYLESHEET_MODENA );
```

* To JavaFX Nodes

Nodes, inherit from `javafx.scene.Parent` allowing them to be used as css stylesheet container. When you apply CSS to a specific node, it is only applied to the node itself and all the nodes in its children hierarchy.

```java
Label label = new Label("...");
label.setStyle("-fx-background-color: black;")

// API Way
label.setPrefWidth(500); // label.setStyle("-fx-pref-width: 500")
```

**Note**
This method is only recommended in cases where your styling has to be very dynamic, usually based on your own UI changes, like the preceding example. It is also very useful for quick prototyping.

* Applying syles to elements in `fxml`

```xml
<!-- assign a style class -->
<Label styleClass="fancy-label" />

<!-- assign a style directly -->
<Label style="-fx-pref-width: 500px" />

<!-- assign a stylesheet -->
<Label stylesheets="@styles.css" />
```

**Note** Priority
As you can see, the node’s style will override any previous style settings.

1. Apply user agent stylesheets.
2. Apply value set by a JavaFX API call.
3. Apply styles set by scene or node stylesheets property.
4. Apply style from node’s style property.

## Advanced CSS Techniques

* Pseudo Selectors

JavaFX CSS also supports pseudo-classes, which allow you to define styles corresponding to a different state of the JavaFX node.

**Note**
JavaFX does not implement a full range of pseudo-classes specified in the CSS standard. 

Examples:
-- `armed` -> applies when the armed variable is true.
-- `cancel` -> applies if this Button receives VK_esC if the event is not otherwise consumed.
-- `default` -> applies if this Button receives VK_enter if the event is not otherwise consumed.
-- `default` -> applies styles to node when the node is in it default state

* Imports
Starting with JavaFX 8u20, CSS @import rule is partially supported. Currently, only unconditional imports are allowed (media type qualifier is not supported). 

```css
@import "defaults/styles.css"

/* URL based styles */
@import url ("http://website/folder/styles.css")
```

* Font loading (JavaFX v8+)

```css
@font-face {
    font-family: 'sample';
    font-style: normal;
    font-weight: normal;
    src: local('sample'), url('http://font.samples/resources/sample.ttf'; ) format('truetype');
}
```

## Reusing Styles

To allow for higher flexibility, JavaFX CSS supports constants – a nonstandard CSS feature. Currently, only colors can be defined as constants. Besides a lot of predefined named colors, custom constants can be defined, which in the reference guide are called “looked-up colors.” With the looked-up colors, you can refer to any other color property that is set on the current node or any of its parents.

**Note**
The looked-up colors are “live” and react to any style changes since they are not looked up until they are applied.

## Using Advanced Color Definitions

JavaFX specifies multiple ways to define paint values. Those are of the following:

### Using Linear Gradients

Linear gradient syntax is defined as follows:

> linear-gradient( [ [from <point> to <point>] | [ to <side-or-corner>], ]? [ [ repeat | reflect | no_cycle], ]? <color-stop>[, <color-stop>]+)  

 `where <side-or-corner> = [left | right] ||[top | bottom]`

`no_cycle` is the default value for repeat

**Note**
If the points are percentages, they are relative to the size of the area being filled. Percentages and lengths cannot be mixed in a single gradient.

```css
/*
*
  * with yellow at the top left corner and red in the bottom right
*/
-fx-text-fill: linear-gradient(to bottom right, yellow, red);
/* same as above but using percentages */
-fx-text-fill: linear-gradient(from 0% 0% to 100% 100%, yellow 0%, green 100%);
```

### Using Radial Gradients

Radial gradient syntax is defined as follows:

> radial-gradient([ focus-angle <angle>, ]? [ focus-distance <percentage>, ]? [ center <point>, ]? radius [ <length> | <percentage> ] [ [ repeat | reflect ], ]? <color-stop>[, <color-stop>]+)

**Note**
Radial gradient creates a gradient going through all the stop colors radiating outward from the center point to the radius. If the center point is not given, the center defaults to (0 0). Percentage values are relative to the size of the area being filled. Percentage and length sizes cannot be mixed in a single gradient function.

```css
.selector {
    -fx-text-fill: radial-gradient(radius 100%, red, darkgray, black);
    -fx-text-fill: radial-gradient(focus-angle 45deg, focus-distance 20%, center 25% 25%, radius 50%, reflect, gray, darkgray 75%, dimgray);
}
```

### Using Image Pattern

This gives the ability to use image pattern as paint. The following is the syntax for image pattern:

> image-pattern(<string>, [<x_origin>, <rectangle_y_origin>, <rectangle_width>, <rectangle_height>[, <proportional_or_absolute>]?]?)

```css
.selector {
    -fx-text-fill: image-pattern("images/wood.png", 20%, 20%, 80%, 80%);
    -fx-text-fill: image-pattern("images/wood.png", 20%, 20%, 80%, 80%, true);
    -fx-text-fill: image-pattern("images/wood.png", 20, 20, 80, 80, false);
}
```

### Using RGB Color Definitions

The RGB color model is used for numerical color applications. It has a number of different supported forms:

> #<digit><digit><digit>

or #<digit><digit><digit><digit><digit><digit>
or rgb( <integer> , <integer> , <integer> )
or rgb( <integer> %, <integer>% , <integer>% )
or rgba( <integer> , <integer> , <integer> , <number> )
or rgba( <integer>% , <integer>% , <integer> %, <number> )

```css
.label {
    -fx-text-fill: #f00
}

.label {
    -fx-text-fill: #ff0000
}

.label {
    -fx-text-fill: rgb(255, 0, 0)
}

.label {
    -fx-text-fill: rgb(100%, 0%, 0%)
}

.label {
    -fx-text-fill: rgba(255, 0, 0, 1)
}
```

### Using HSB Color Definitions

Colors can also be specified using the HSB (sometimes called HSV) color model as follows:

> hsb( <number> , <number>% , <number>% ) or

hsba( <number> , <number>% , <number>% , <number> )

**Note**
The first number is hue, a number in the range 0–360 degrees.
The second number is saturation, a percentage in the range 0–100%.
The third number is brightness, also a percentage in the range 0–100%.
The hsba(...) form takes a fourth parameter at the end which is an alpha value
in the range 0.0–1.0, specifying completely transparent and completely opaque, respectively.

### Using Color Functions

JavaFX CSS engine provides support for some color computation functions. These functions compute new colors from input colors at the same time the color style is applied.

> derive( <color> , <number>% ) -> Derive a new color from an existing color by modifying it brightness. 0% no changes, 100% brigther, -100% darker.

> ladder (<color> , <color-stop> [, <color-stop>]+) -> The ladder function interpolates between colors. The effect is as if a gradient is created using the stops provided, and then the brightness of the provided <color> is used to index a color value within that gradient.

**Note** Ladder()
At 0% brightness, the color at the 0.0 end of the gradient is used; at 100% brightness, the color at the 1.0 end of the gradient is used; and at 50% brightness, the color at 0.5 the midway point of the gradient, is used.

```css
.selector {
    -fx-text-fill: ladder(background, white 49%, black 50%);
}
```

## Using Effect Definitions

JavaFX CSS currently supports the DropShadow and InnerShadow effects from the JavaFX platform. See the class documentation in javafx.scene.effect for further details about the semantics of the various effect parameters.

* Drop Shadow

> dropshadow( <blur-type> , <shadow_color> , <shadow_blur_radius> , <shadow_spread> , <offset_x> , <offset_y> )

-- `shadow_blur_radius` -> the radius of the shadow blur kernel, in the range [0.0 ... 127.0], typical value 10.

-- `shadow_spread` -> It's the portion of the radius where the contribution of the source material will be 100%. the remaining portion of the radius will have a contribution controlled by the blur kernel.

## Modena theme constant

> `-fx-base` -> Defines base color for most JavaFX applications

```css
.selector {
    -fx-background-color: derive(-fx-base, 20%);
}
```

**Note**
The base color can be override to change the global look and feel of the application.

```css
.root {
    -fx-base: rgba(10, 45, 100);
}
```

## Icons

Instead of loading and assigning images using Java code, we can do it much simpler using CSS definitions.

> -fx-graphic -> Allow to add graphic to JavaFX nodes.

```css
.image-label {
    -fx-graphic: url("path/to/icon.jpg");
}
```

## Advanced CSS API

* Building custom component

Custom components/nodes are based on existing JavaFX Controls by overriding their `styles`,adding custom properties and maybe overriding their rendering.

Custom components provides a way to reutilize codes, in JavaFx applications.

```java
// chapterX/cssapi/WeatherType.java
import javafx.scene.text.Text;
public enum WeatherType {
    SUNNY("\uf00d", false),
    CLOUDY("\uf013", false),
    RAIN("\uf019", false),
    THUNDERSTORM("\uf033", true);
    private final boolean dangerous;
    private final String c;
    WeatherType(String c, boolean dangerous) {
        this.c = c;
        this.dangerous = dangerous;
    }
    public boolean isDangerous() {
        return dangerous;
    }

    Text buildGraphic() {
        Text text = new Text(c);
        text.setStyle("-fx-font-family: 'Weather Icons Regular'; -fx-font-
        size: 25;");
        return text;
    } 
}

// chapterX/cssapi/WeatherIcon.java
public class WeatherIcon extends Label {
    // Css style class to add to the current component
    private static final String STYLE_CLASS       = "weather-icon";

    // Custom prooperty name
    private static final String WEATHER_PROP_NAME = "-fx-weather";

    // Custom added pseudo-class supported by the element
    private static final String PSEUDO_CLASS_NAME = "dangerous";

    // Creates a CSS pseudo class instance
    private static PseudoClass DANGEROUS_PSEUDO_CLASS = PseudoClass.
    getPseudoClass(PSEUDO_CLASS_NAME);

    private static final StyleablePropertyFactory<WeatherIcon> STYLEABLE_
    PROPERTY_FACTORY =
            new StyleablePropertyFactory<>(Region.getClassCssMetaData());
    
    private static CssMetaData<WeatherIcon, WeatherType> WEATHER_TYPE_
    METADATA =
            STYLEABLE_PROPERTY_FACTORY.createEnumCssMetaData(
                    WeatherType.class, WEATHER_PROP_NAME, x ->
                    x.weatherTypeProperty);

    // Boolean property that controls that fire events when the `dangerous`
    // pseudo class changes
    private BooleanProperty dangerous = new BooleanPropertyBase(false) {
        public void invalidated() {
            // Whenever property changes, we call a special method pseudoClassStateChanged to let CSS engine know that state has changed
            pseudoClassStateChanged(DANGEROUS_PSEUDO_CLASS, get());
        }
        @Override public Object getBean() {
            return WeatherIcon.this;
        }
        
        @Override public String getName() {
            return PSEUDO_CLASS_NAME;
        } 
    };

    // The actual property that controls the class styling
    // {@see StyleableObjectProperty} is the base class ihnerited by any style property
    // controller class
    private StyleableObjectProperty<WeatherType> weatherTypeProperty = new
    StyleableObjectProperty<>(WeatherType.SUNNY) {
        @Override
        public CssMetaData<? extends Styleable, WeatherType>
        getCssMetaData() {
            return WEATHER_TYPE_METADATA;
        }

        @Override
        public Object getBean() {
            return WeatherIcon.this;
        }

        @Override
        public String getName() {
            return WEATHER_PROP_NAME;
        }

        @Override
        protected void invalidated() {
            WeatherType weatherType = get();
            dangerous.set( weatherType.isDangerous());
            setGraphic(weatherType.buildGraphic());
            setText(get().toString());
        }   
    };

    // Default Constructor
    public WeatherIcon() {
        getStyleClass().setAll(STYLE_CLASS);
    }

    // Parameter constructor
    //
    public WeatherIcon(WeatherType weatherType ) {
        this();
        setWeather( weatherType);
    }

    @Override
    public List<CssMetaData<? extends Styleable, ?>> getControlCss
    MetaData() {
        // We also implement the getControlCssMetaData method, which allows JavaFX CSS engine to know everything about the control’s CSS metadata by returning a list of control styleable properties
        return List.of(WEATHER_TYPE_METADATA);
    }

    public WeatherType weatherProperty() {
        return weatherTypeProperty.get();
    }

    public void setWeather(WeatherType weather) {
        this.weatherTypeProperty.set(weather);
    }

    public WeatherType getWeather() {
        return weatherTypeProperty.get();
    }
 
}
```

Using the created component and styling it:

```css
/* resources/chapterX/cssapi/styles.css */
@font-face {
    font-family: 'Weather Icons Regular';
    src: url('weathericons-regular-webfont.ttf');
}

.root {
    -fx-background-color: lightblue;
    -fx-padding: 20px;
}

.thunderstorm {
    -fx-weather: THUNDERSTORM;
}

.rain {
    -fx-weather: RAIN;
}

.weather-icon {
    -fx-graphic-text-gap: 30;
    -fx-padding: 10;
}

.weather-icon:dangerous {
    -fx-background-color: rgba(255, 0, 0, 0.25);
}
```

Java application source code look like:

```java
/* chapterX/cssapi/WeatherApp.java */
public class WeatherApp extends Application {
    @Override
    public void start(Stage primaryStage)  {
        // Creates the wether icon
        WeatherIcon rain = new WeatherIcon();

        // Makes the component a rainy wether icon component
        rain.getStyleClass().add("rain");
        WeatherIcon thunderstorm = new WeatherIcon();
        thunderstorm.getStyleClass().add("thunderstorm");
        WeatherIcon clouds = new WeatherIcon( WeatherType.CLOUDY);
        VBox root = new VBox(10, rain, thunderstorm, clouds);
        root.setAlignment(Pos.CENTER);
        Scene scene = new Scene( root);
        scene.getStylesheets().add( getClass().getResource("styles.css").
        toExternalForm());
        primaryStage.setTitle("WeatherType Application");
        primaryStage.setScene(scene);
        primaryStage.show();
    } 
}
```
