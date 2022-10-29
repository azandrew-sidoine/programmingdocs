# JavaFX Web & Cloud Infrastructure

## The webview component

JavaFX provides a webview component that works like a web browser for rending HTML based content. It provides javascript bridge API that allow to interacts with web components (Calling JS function)

**Note**
With the help of the open source project “DukeScript, ” you can even bind HTML elements directly to JavaFX properties.

```java

public class MenuElement {

    private Sting label;
    private ActionInterface actionHandler;

    public MenuElement(String label) {
        this.label = label;
    }

    public MenuElement(String label, ActionInterface actionHandler) {
        this(label);
        this.actionHandler = actionHandler;
    }

    public getLabel() {
        return label;
    }

    public getActionHandler() {
        return actionHandler;
    }
}

public class WebViewApp extends Application {

    @Override()
    public void start(Stage stage)
    {
        var webview = createWebView("https://openjfx.io");
        BorderPane main = new BorderPane(webview); //
        main.setTop(createMenuBar(new HashMap<String, ?>()));
        Scene page = new Scene(webview, 300, 250);
        stage.setTitle("...");
        stage.setScene(page);

        //
        stage.show();
    }

    public Webview createWebView(String url)
    {
        var webview = createWebView();
        loadURL(webview,url);
        return webview;
    }

    public Webview createWebView()
    {
        Webview webview = new WebView();
        // Disable the context menu on the webview
        webview.setContextMenuEnabled(false);
        return webview;
    }

    private void loadURL(Webview view, String url)
    {
        WebEngine engine = view.getEngine().load(url);
    }

    private Node createMenuBar(Map<String, MenuElement> items) {
        MenuBar menuBar = new MenuBar();
        var menuItems = items.stream().map(index -> {
            var element = items.get(index);
            final Menu menu = new Menu(element.getLabel());
            if (element.getActionHandler() != null) {
                menu.setOnAction(element.getActionHandler());
            }
        });
        menuBar.getMenus().addAll(menuItems);
        return menuBar;
    }
}
```

### Webview Engine

The web engine is the object or class to control content in the webview.

*  Working with the history API

> WebEngine.getHistory().getEntries().addListener(ListChangeLister) -> Returns an `ObservableList` of history of the web engine.

* Tracking page load progress

> WebEngine.getLoadWorker().progressProperty() -> Observable<float|ProgressProperty> which an observable of the load worker progress property.

```java
ProgressBar progressBar = new ProgressBar();
        progressBar.progressProperty().bind(
engine.getLoadWorker().progressProperty()); progressBar.visibleProperty().bind(engine.getLoadWorker(). stateProperty().isEqualTo(State.RUNNING));
```

* Load state property of the web engine

> engine.getLoadWorker().stateProperty() -> Observable<StateEnum> Returns an observable of the state property of the web engine.

It can be use to make sure the web view completely load the page before executing a javascript code:

```java
engine.getLoadWorker().getStateProperty().addListener((e, o, n) -> {
    if (n == State.SUCCEEDED) {
        // Construct java script logic
        String js = constructJavascript(...);

        // executing javascript
        engine.executeScript(js);
    }
});
```

* Executing Javascript code

As mention previously, JavaFX allow developper to execute javascript code and 

Example code:

```java
public class WebViewCharts extends Application {
    @Override
    public void start(Stage primaryStage) {
        WebView webView = new WebView();
        final WebEngine engine = webView.getEngine();
        engine.load(WebViewCharts.class.getResource("charts.html").
        toExternalForm());
        Scene scene = new Scene(webView, 300, 250);
    primaryStage.setTitle("JavaFX WebView Chart Demo");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```

**Note**
To get the URL of the HTML page, we can call getClass().getResource(“charts.html”). For this, the file needs to be in the same package as the main class.

Executing a Js code after the browser page is loaded:

```java
engine.getLoadWorker().getStateProperty().addListener((e, o, n) -> {
    if (n == State.SUCCEEDED) {
        // Construct java script logic
        String js = constructJavascript(...);

        // executing javascript
        engine.executeScript(js);
    }
});

public String constructJavascript(...) {
    String result = "... javascript script";
    return result;
}
```

* Reacting to event from the webview event or js calls

The example is not quite relevant, and more documentation on the section must be look for:

```java

JSObject script = (JSObject) engine.executeScript("window");
                script.setMember("formValues", new ValuePrinter());
```

### FXML and the Model View ViewModel Pattern

`DukeScript` is a framework for interacting with Javascript in Java programming language. Its core features are an API for painless Java and JavaScript interaction and an API for direct binding of HTML elements and attributes to Java properties.

**Note**
DukeScript allows you to use HTML views in the same way you use FXML. FXML is, just like HTML, a declarative markup language for designing user interfaces. The view elements and their properties can be bound to view logic in a controller (or viewmodel) class.

* HTML Controller

To use HTML controlers, we require `net.java.html` , `net.java.html.json` , `ko4j` , and `net.java.html.boot.fx` from `org.netbeans.html` group and `javafx.beaninfo` artifact from `com.dukescript.api` group.

**Note**
While the FXMLLoader relies on reflection and annotations to set up the wiring between the view and its viewmodel, we’re using a class called FXBeanInfo, which gives direct access to the properties exposed by the viewmodel. The benefit of this is that there’s no reflection required, which makes the system faster and easier to test. To expose properties, you’ll implement a single method interface, `FXBeanInfo.Provider` :

```java
class HTMLController implements FXBeanInfo.Provider {
    private final StringProperty labelText = new SimpleStringProperty(this,
    "labelText", "");

    private final Property<EventHandler<ActionEvent>> action =
            new SimpleObjectProperty<EventHandler<ActionEvent>>(
                    this, "action",
                    (e) -> labelText.set("Hello World!"));

    // FXBeanInfo supports the builder pattern for easily creating the FXBeanInfo using the actual properties of your bean
    // **Note** You’re not required to write getters and setters for your properties, since they can be accessed using the FXBeanInfo. The consumer of the FXBeanInfo can simply call the method getProperties in order to get a map of the available properties. It’s a map instead of a set or list, so you can also easily access a property by its name.
    private final FXBeanInfo info = FXBeanInfo
        .newBuilder(this)
        .property(labelText)
        .build();

    @Override
    public FXBeanInfo getFXBeanInfo() {
        return info;
    }
```

**Note**
Instead of scanning the controller via reflection for getters and setters of a bound property, the loader could simply access the Property via the FXBeanInfo. No reflection is required at all – clean, fast, and standardized access to all exposed properties.

```java
// Test the HTML controller
public class HTMLControllerTest {
    @Test
    public void hello() {
        HTMLController controller = new HTMLController();
        FXBeanInfo fxBeanInfo = controller.getFXBeanInfo();

        // Returns the list of available property on the element being expected
        ObservableValue<?> labelText = fxBeanInfo.getProperties().
        get("labelText");
        assertEquals("", labelText.getValue());

        // Query for the handler on the controller element
        EventHandler<? super ActionDataEvent> action =
                fxBeanInfo.getActions().get("action").getValue();
        // Invoke the handler action
        action.handle(null);
        assertEquals("Hello World!", labelText.getValue());
    }
}
```

`DukeScript` uses `data-bind:attribute|property` to bind an attribute or an action to a javascript code.

For example in the code below, span inner html is binded using `data-bind="text propertyKey"` and a click `data-bind="click:actionHandler"`

```html
<div class="row">
    <div class="flex-item"><span data-bind="text: labelText">
        </span></div>
    <div class="flex-item"><button data-bind="click:
    action">Click me!</button></div>
</div>
```

* HTML loader

To support more than one HTML-based view, it’s better to hide that in an HTMLLoader which can be used similar to the FXMLLoader.

```java
public class HTMLLoader {

    // Load an HTML content into the web view and 
    public static WebView load(URL html, final FXBeanInfo.Provider
    viewModel){
        WebView webView = new WebView();
        FXBrowsers.load(webView, html, new Runnable() {
            @Override
            public void run() {
                Models.applyBindings(viewModel);
            }});
        return webView;
    }
}
```

Now to load the HTML resource:

```java
// Main
WebView webview = HTMLLoader.load(getClass().getResource("/html/view.
html"), new HTMLController());
tabPane.getTabs().add(new Tab("HTML",webview));
```

* HTML Data Binding

`DukeScript` has more component binding including `loops` and `conditionals`

```java
public class TodoListHTMLController implements FXBeanInfo.Provider {
    final ObjectProperty<String> input = new SimpleObjectProperty<>(this,"input");

    final ObjectProperty<TodoElement> selected = new SimpleObjectProperty<>(this, "selected");

    final ListProperty<TodoElement> todos = new SimpleListProperty<>(this, "todos", FXCollections.observableArrayList());

    final Property<EventHandler<Event>> add = new SimpleObjectProperty<>(this, "add");

    final Property<EventHandler<ActionDataEvent>> remove = new SimpleObjectProperty<>(this, "remove");

    final FXBeanInfo info = FXBeanInfo.newBuilder(this).
        property(input).
        property(selected).
        property(todos).
        action(remove).
        action(add).
        build();

    public TodoListHTMLController() {
        todos.add(new TodoElement("Buy milk!"));
        add.setValue(e -> todos.add(new TodoElement(input.get())));
        remove.setValue((event) -> {
            TodoElement toRemove = event.getSource(TodoElement.class);
            todos.get().remove(toRemove);
        }); 
    }

    @Override
    public FXBeanInfo getFXBeanInfo() {
        return info;
    }

    private static final class TodoElement implements FXBeanInfo.Provider {
        final String message;
        final FXBeanInfo info;

        TodoElement(String message) {
                    this.message = message;
                    this.info = FXBeanInfo.newBuilder(this).
                            constant("message", message).
                            build();
        }

        @Override
        public FXBeanInfo getFXBeanInfo() {
            return info;
        }
    }
}
```

-- Foreach binding example:

```html
<ul data-bind="foreach: todos">
    <li>
        <span data-bind="text: message"></span>
        (<a href="#" data-bind="click: $root.remove">remove</a>)
    </li>
</ul>
```

### Displaying a Map with DukeScript

Besides offering an easy way to bind HTML elements to JavaFX properties, the DukeScript project has created a lot of libraries you can directly use in your application.

* Leaflet4j

[https://github.com/dukescript/leaflet4j]

### From Web Sites to APIs

#### Decoding JSON

* Jackson
It's a very popular Java library for encoding and decoding JSON structured data.

-- Maven

```xml
 <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
<version>2.9.8</version>
```

-- Gradle

```groovy
dependencies {
    implementation "com.fasterxml.jackson.core:jackson-databind:2.9.8"
}
```

* Connect

Gluon’s Connect library [https://github.com/gluonhq/connect] not only deserializes the JSON response like Jackson but also does it in an asynchronous way.
It returns a JavaFX observable list or object that can be used directly by the JavaFX UI controls.

```xml
<groupId>com.gluonhq</groupId>
    <artifactId>connect</artifactId>
<version>2.0.1</version>

<!-- -->
<groupId>org.glassfish</groupId>
<artifactId>jakarta.json</artifactId>
<version>1.1.5</version>
<scope>runtime</scope>
```

-- Gradle

```groovy
dependencies {
    implementation "com.gluonhq:connect:2.0.1"
    runtimeOnly 'org.glassfish:jakarta.json:1.1.5
}
```

Example of Gluon based request:

```java
 private GluonObservableObject<Model> getWeather() {
        RestClient client = RestClient.create()
                .method("GET")
                .host("http://api.openweathermap.org/")
                .connectTimeout(10000)
                .readTimeout(1000)
                .path("data/2.5/weather")
                .header("accept", "application/json")
                .queryParam("appid", API_KEY)
                .queryParam("q", CITY);
        return DataProvider.retrieveObject(
             client.createObjectDataReader(Model.class));
}
```
