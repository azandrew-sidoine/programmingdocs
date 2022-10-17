# JavaFX Deep Dive into Controls (JavaFX 5 and later)

> `javafx.scene.chart` -> House Charting components for building chart as line, bar, area, Pie, Bubble, Scatter charts.
> `javafx.scene.control` -> House the APIs for all UI controls in JFX.
> `javafx.scene.control.cell` -> APIs for `cell factories`

> `javafx.scene.control.skin` -> APIs house visual components for each UI control.

**Note**
Most JFX UI Controls extends from the `javafx.controls.Control` class.

> `OOP hierrarchie` : Node -> Parent -> Control

**Warning**
`HTMLEditor extends javafx.web.WebView` component is the exception to the control rule.

## JavaFX Basic Controls

### Labeled Controls

Abstract class for `Label` , `Button` , `CheckBox` , `RadioButton` , `ToggleButton` .

Most controls that display read-only text extend from a common abstract superclass known as Labeled.

> `aligment` -> ObjectProperty<Pos> -> How the Text & Graphic should be aligned
> `contentDisplay` -> ObjectProperty<ContentDisplay> -> Positioning of the graphic relative to the text
> `font` -> ObjectProperty<Font> -> Text font to be used
> `graphic` -> ObjectProperty<Node> -> An option icon for the `Labeled`

> `textAlignment` -> ObjectProperty<TextAlignment> -> Behaviour for line of text
> `text` -> StringProperty -> Text to be Displayed
> `wrapText` -> BooleanProperty -> Wether the text should wrap

### Label `javafx.controls.Label extends javafx.controls.Labeled`

> `labelFor` -> It works like an `for` attribute of an HTML Label element.

### Button `javafx.controls.Button extends javafx.controls.Labeled`

Used to execute user actions.

> `armed` -> ReadOnlyBooleanProperty4 -> Indicates whether user is currently pressing button
> `cancelButton` -> BooleanProperty -> Handle escape key press if true
> `defaultButton` -> BooleanProperty -> Handle `enter` key press
> `onAction` -> ObjectProperty<EventHandler<ActionEvent>> -> Callback that is fired executed when button is cliked
> `fire()` -> Programatically invoke button click event.

```java
var button = new Button("Click Me!");
button.setOnAction(event -> System.out.println("Button was clicked"));
```

### Checkbox

Typically, a CheckBox enables a user to specify whether something is true or false.
In JavaFX this is possible, but there is also the ability to show a third state:
indeterminate.

> `allowIndeterminate` -> BooleanProperty  -> Determines if the CheckBox should toggle into the `indeterminate` state.
> `indeterminate` -> BooleanProperty -> Specifies whether the CheckBox is currently

indeterminate.

> `selected` -> BooleanProperty -> Specifies whether the CheckBox is currently

selected.

```java
var checkbox = new CheckBox("Enable Power Plant");
checkbox.setIndeterminate(false);
checkbox.setOnAction(e -> log("Action event fired"));
checkbox.selectedProperty()
        .addListener(i -> log("Selected state change to " + cb.isSelected()));
```

### Hyperlink `javafx.controls.HyperLink extends javafx.controls.Button`

The Hyperlink control is essentially a Button control that is presented in the form of a hyperlink – text with an underline.

> `visited` -> BooleanProperty -> Toggles to true when the hyperlink has been fired for the first time by the user.

```java
var hyperlink = new Hyperlink("Click Me!");
hyperlink.setOnAction(event -> log("Hyperlink was clicked"));
```

### ToggleButton `javafx.controls.ToggleButton extends javafx.controls.Button`

When a ToggleButton is selected, its visual appearance is different, appearing to be “pushed in.” ToggleButton instances may be added to a ToggleGroup to control selection.

* What is a ToggleGroup?
ToggleGroup is a class that simply contains a list of Toggle instances for which it
manages their selected state. ToggleGroup ensures that at most only one Toggle can be selected at a time.

**Note**
`Toggle` is an interface with two properties – `selected` and `toggleGroup` . Classes that implement this interface include `ToggleButton` , `RadioButton` , and `RadioMenuItem` .

> `selected` -> BooleanProperty -> Indicates whether the toggle is selected.
> `toggleGroup` -> ObjectProperty<ToggleGroup> -> The ToggleGroup to which this

ToggleButton belongs

```java
// create a few toggle buttons
ToggleButton tb1 = new ToggleButton("Toggle button 1");
ToggleButton tb2 = new ToggleButton("Toggle button 2");
ToggleButton tb3 = new ToggleButton("Toggle button 3");
// create a toggle group and add all the toggle buttons to it
ToggleGroup group = new ToggleGroup();
group.getToggles().addAll(tb1, tb2, tb3);

group.selectedToggleProperty()
 .addListener(i -> log("Selected toggle is " + group.
    getSelectedToggle()));
```

### RadioButton

`RadioButton` is a `ToggleButton` , with a different styling applied and a slightly different behavior when placed in a `ToggleGroup` .

**Note**
Whereas ToggleButtons in a ToggleGroup can be all unselected, in the case of RadioButtons in a ToggleGroup, there is no way for a user to unselect all RadioButtons.

### Text Input Controls

The next set of controls to cover, after the simple Labeled controls, are the three controls primarily used for text input, namely, `TextArea` , `TextField` , and `PasswordField` .

**Note**
TextArea and TextField extend from an abstract class called `TextInputControl` , enables caret positioning (caret is the blinking cursor that indicates where text input will appear), text selection and formatting, and of course
editing.

> `anchor` -> ReadOnlyIntegerProperty -> The anchor of the text selection. The range

between anchor and caret represents the
text selection range.

> `caretPosition` -> ReadOnlyIntegerProperty -> The current position of the caret within the text.
> `editable` -> BooleanProperty -> Whether the user can edit the text in the

control.

> `font` -> ObjectProperty<Font> -> The font to use to render the text.
> `length` -> ReadOnlyIntegerProperty -> The number of characters entered in the

control.

> `promptText` (Placeholder) -> StringProperty -> Text to display when there is no user input.
> `selectedText` ReadOnlyStringProperty -> The text that has been selected in the control, via mouse or keyboard or programmatically.
> `textFormatter` -> ObjectProperty<TextFormatter<?>> -> See section “TextFormatter.”
> `text` -> StringProperty -> The textual content of this control.

### TextFormatter (Pipe)

A TextFormatter has two distinct mechanisms that enable it to influence what is accepted and displayed within text input controls:

* A filter that can intercept and modify user input. This helps to keep the text in the desired format. A default text supplier can be used to provide the initial text.
* A value converter and value can be used to provide special format that represents a value of type V. If the control is editable and the text is changed by the user, the value is then updated to correspond to the text.

### TextField, PasswordField, and TextArea

> `onAction(javafx.utils.Callback)` -> Handles `enter` key when textfield is focused.

```java
TextField textField = new TextField();
textField.setPromptText("Enter name here");
// this is fired when the user hits the Enter key
textField.setOnAction(e -> log("Entered text is: " + textField.getText()));
// we can also observe input in real time
textField.textProperty()
        .addListener((o, oldValue, newValue) -> log("current text input is "
        + newValue));
```

> `prefColumnCount` -> IntegerProperty -> Preferred number of text columns.
> `prefRowCount` -> IntegerProperty -> Preferred number of text rows
> `wrapText` -> BooleanProperty -> Whether to wrap text or let the TextArea scroll

horizontally when a line exceeds the width available.

### ProgressBar and ProgressIndicator

JavaFX offers two UI controls for displaying progress to users: `ProgressBar` and
`ProgressIndicator` .

**Note**
To show progress, developers should set the progress property to a value between
0.0 and 1.0.
If progress value is -1, the progress is `indeterminate` .

> `indeterminate` -> ReadOnlyBooleanProperty -> A boolean flag indicating if the indeterminate progress animation is playing.
> `progress` -> DoubleProperty The actual progress (between 0.0 and 1.0), or

can be set to -1 for indeterminate.

```java
ProgressBar p2 = new ProgressBar();
p2.setProgress(0.25F);
```

### Slider

The Slider control is used to enable users to specify a value within a certain min/max range. This is made possible by displaying to the user a “track” and a “thumb.”

> `blockIncrement` -> DoubleProperty -> How much the Slider moves if the track is clicked.
> `max` -> DoubleProperty -> The maximum value represented by the Slider.
> `min` -> DoubleProperty -> The minimum value represented by the Slider.
> `orientation` -> ObjectProperty<Orientation> -> Whether the Slider is horizontal or vertical.
> `value` -> DoubleProperty -> The current value represented by the Slider.

```java
Slider slider = new Slider(0.0f, 1.0f, 0.5f);
slider.valueProperty()
 .addListener((o, oldValue, newValue) -> log("Slider value is " + newValue));
```

## JavaFX Container Controls

### Accordion and TitledPane `javafx.controls.layout.TitledPane extends javafx.controls.Labeled`

* TitlePane
TitledPane is a container that displays a title area and a content area and has the ability to expand and collapse the content area by clicking on the title area.

> `animated` -> BooleanProperty -> Whether the TitledPane animates as it expands and

collapses.

> `collapsible` -> BooleanProperty -> Whether the TitledPane can be collapsed by the user.
> `content` -> ObjectProperty<Node> -> The Node to display in the content area of the TitledPane.
> `expanded` -> BooleanProperty -> Whether the TitledPane is currently expanded or not. text StringProperty The text to show in the header area of the TitledPane.

* Accordion
It's a control that is simply a container of zero or more TitledPanes. When an Accordion is displayed to the user, it only allows for one TitledPane to be expanded at any time.

> `expandedPane` -> ObjectProperty<TitledPane> -> The currently expanded TitledPane in the Accordion.

```java
TitledPane t1 = new TitledPane("TitledPane 1", new Button("Button 1"));
TitledPane t2 = new TitledPane("TitledPane 2", new Button("Button 2"));
TitledPane t3 = new TitledPane("TitledPane 3", new Button("Button 3"));
Accordion accordion = new Accordion();
accordion.getPanes().addAll(t1, t2, t3);
```

### ButtonBar

ButtonBar can be thought of as being essentially a HBox for Button
controls (although it works with any Node), with the added functionality of placing
the provided Buttons in the correct order for the operating system on which the user
interface is running.

> `buttonMinWidth` -> DoubleProperty -> The minimum width of all buttons placed in the ButtonBar.
> `buttonOrder` -> StringProperty -> The ordering of buttons in the ButtonBar.

```java
ButtonBar buttonBar = new ButtonBar();
// Create the buttons to go into the ButtonBar
Button yesButton = new Button("Yes");
ButtonBar.setButtonData(yesButton, ButtonData.YES);
Button noButton = new Button("No");
ButtonBar.setButtonData(noButton, ButtonData.NO);
// Add buttons to the ButtonBar
buttonBar.getButtons().addAll(yesButton, noButton);
```

### ScrollPane

ScrollPane is a control that is crucial to almost every user interface – the ability to scroll horizontally and vertically when content extends beyond the bounds of the user interface.

**Note**
There is no need to wrap `ListView` , `TableView` , & some other controls in `ScrollPane` .

> `content` -> ObjectProperty<Node> -> The Node to be displayed.
> `fitToHeight` -> BooleanProperty -> Will attempt to keep content resized to match

height of viewport.

> `fitToWidth` -> BooleanProperty -> Will attempt to keep content resized to match width of viewport.
> `hbarPolicy` ObjectProperty<ScrollBarPolicy> -> Sets policy for when to show horizontal scrollbars.
> `hmax` -> DoubleProperty -> The maximum allowed hvalue.
> `hmin` -> DoubleProperty -> The minimum allowed hvalue.
> `hvalue` -> DoubleProperty -> The current horizontal position of the ScrollPane.
> `vbarPolicy` -> ObjectProperty<ScrollBarPolicy> -> Sets policy for when to show vertical scrollbars. This can be one of the enum constants in ScrollPane ScrollBarPolicy: `ALWAYS` , `AS_NEEDED` , or `NEVER` .
> `vmax` -> DoubleProperty -> The maximum allowed vvalue.
> `vmin` -> DoubleProperty -> The minimum allowed vvalue.
> `vvalue` -> DoubleProperty -> The current vertical position of the `ScrollPane` .

```java
// in this sample we create a linear gradient to make the scrolling visible
Stop[] stops = new Stop[] { new Stop(0, Color.BLACK), new Stop(1, Color.
RED)};
LinearGradient gradient = new LinearGradient(0, 0, 1500, 1000, false,
CycleMethod.NO_CYCLE, stops);
// we place the linear gradient inside a big rectangle
Rectangle rect = new Rectangle(2000, 2000, gradient);
// which is placed inside a scrollpane that is quite small in comparison
ScrollPane scrollPane = new ScrollPane();

scrollPane.setPrefSize(120, 120);
scrollPane.setContent(rect);
// and we then listen (and log) when the user is scrolling vertically or horizontally
ChangeListener<? super Number> o = (obs, oldValue, newValue) -> {
        log("x / y values are: (" + scrollPane.getHvalue() + ", " + scrollPane.getVvalue() + ")");
    };
scrollPane.hvalueProperty().addListener(o);
scrollPane.vvalueProperty().addListener(o);
```

### SplitPane

The SplitPane control accepts two or more children and draws them with a draggable
divider between them. The user is then able to use this divider to give more space to one child, at the cost of taking space away from the other child. A SplitPane control is great for user interfaces where there is a main content area, and then an area on the left/right/bottom of the content area is used to display more context-specific information.

**Warning**
It is recommended that all nodes added to a SplitPane be wrapped inside a separate layout container, such that the layout container may handle the sizing of the node, without impacting the SplitPane’s ability to function.

> `orientation` -> ObjectProperty<Orientation> -> The orientation of the SplitPane.

```java
final StackPane sp1 = new StackPane();
sp1.getChildren().add(new Button("Button One"));
final StackPane sp2 = new StackPane();
sp2.getChildren().add(new Button("Button Two"));
final StackPane sp3 = new StackPane();
sp3.getChildren().add(new Button("Button Three"));

SplitPane splitPane = new SplitPane();
splitPane.getItems().addAll(sp1, sp2, sp3);

// Each layout container takes 1/3 of the available width or height
splitPane.setDividerPositions(0.3f, 0.6f, 0.9f);
```

### TabPane

TabPane is a UI control that enables for tabbed interfaces to be displayed to users. The JavaFX TabPane functions by exposing an ObservableList of Tab instances.

**Note**
The two most useful properties are the side property and the tabClosingPolicy property. The side property is for specifying on which side of the TabPane the tabs will be displayed (by default this is Side. TOP, which means that the tabs will be at the top of the TabPane).

**Note** `TabClosingPolicy`

> `TabClosingPolicy.UNAVAILABLE` -> Tabs cannot be closed by the user.
> `TabClosingPolicy.SELECTED_TAB` -> The currently selected tab will have a small close button in the tab area.
> `TabClosingPolicy.ALL_TABS` -> : All tabs visible in the TabPane will have the small close button visible.

**Note** `Tab` Instance of Tab in the TabPane

> `title` -> StringProperty -> Title or Label of the tab
> `content` -> ObjectProperty<Node> -> The tab content

* TabPane Properties

> `rotateGraphic` -> BooleanProperty -> Whether graphics should rotate to display

appropriately when tabs are placed on the left/right side.

> `selectionModel` -> ObjectProperty<SingleSelectionModel> -> The selection model being used in the TabPane.
> `side` -> ObjectProperty<Side> -> The location at which tabs will be displayed.
> `tabClosingPolicy` -> ObjectProperty <TabClosingPolicy> Described in the preceding text.

```java
TabPane tabPane = new TabPane();
tabPane.setTabClosingPolicy(TabPane.TabClosingPolicy.UNAVAILABLE);
for (int i = 0; i < 5; i++) {
 Tab tab = new Tab("Tab " + I, new Rectangle(200, 200, randomColor()));
 tabPane.getTabs().add(tab);
}
```

### ToolBar

`ToolBar` can be thought of as a stylized HBox that is, it presents whatever nodes are added to it horizontally, with a background gradient.

**Note**
ToolBar are other UI controls such as Button, ToggleButton, and Separator, but there is no restriction on what can be placed within a ToolBar, as long as it is a Node.

**Note**
The ToolBar control does offer one useful piece of functionality – it supports the
concept of overflow, so that if there are more elements to be displayed than there is space to display them all, it removes the “overflowing” elements from the ToolBar and instead shows an overflow button that when clicked pops up a menu containing all overflowing elements of the `ToolBar` .

Recommendations suggest that toolbar being placed below `MenuBar` .

> `orientation` -> ObjectProperty<Orientation> -> Whether the ToolBar should be horizontal or vertical.

```java
ToolBar toolBar = new ToolBar();
toolBar.getItems().addAll(
 new Button("New"),
 new Button("Open"),
 new Button("Save"),
 new Separator(),
 new Button("Clean"),
 new Button("Compile"),
 new Button("Run"),
 new Separator(),
 new Button("Debug"),
 new Button("Profile")
);
```

## Other Controls

### Pagination

Pagination is an abstract way of representing multiple pages, where only the currently showing page actually exists in the scene graph and all other pages are only generated upon request.

> `currentPageIndex` -> IntegerProperty -> The current page index being displayed.
> `pageCount` -> IntegerProperty -> The total number of pages available to be displayed.
> `pageFactory` -> ObjectProperty<Callback<Integer, Node>> -> Callback function that returns the page corresponding to the given index.

```java
Pagination pagination = new Pagination(10, 0);
pagination.setPageFactory(pageIndex -> {
    VBox box = new VBox(5);
    for (int i = 0; i < 10; i++) {
        int linkNumber = pageIndex * 10 + i;
        Hyperlink link = new Hyperlink("Hyperlink #" + linkNumber);
        link.setOnAction(e -> log("Hyperlink #" + linkNumber + " clicked!"));
        box.getChildren().add(link);
    }
    return box;
});
```

### ScrollBar

The `ScrollBar` control is essentially a Slider control with a different style. It consists of a track over which a thumb can be moved, as well as buttons at either end of incrementing and decrementing the value (and thus moving the thumb). 

> `blockIncrement` -> DoubleProperty -> How much the thumb moves if the track is clicked.
> `max` -> DoubleProperty -> The maximum allowed value.
> `min` -> DoubleProperty -> The minimum allowed value.
> `orientation` -> ObjectProperty<Orientation> -> Whether the ScrollBar is horizontal or vertical.
> `unitIncrement` -> DoubleProperty -> The amount to adjust the value when increment/decrement methods are called.
> `value` -> DoubleProperty -> The current value of the ScrollBar

### Separator

The Separator control is perhaps the simplest control in the entire JavaFX UI toolkit. It is a control that lacks any interactivity and is simply designed to draw a line in the relevant section of the user interface.

**Note**
By default, a Separator is oriented vertically such that is draws appropriately when
placed in a horizontal `ToolBar` .

### Spinner (JavaFX 8)

A Spinner can be thought of as a single-line TextField that may or may not be editable, with the addition of increment and decrement arrows to step through some set of values.

**Note**
Because a Spinner can be used to step through various types of value
(integer, float, double, or even a List of some type), the Spinner defers to a
SpinnerValueFactory to handle the actual process of stepping through the range
of values (and precisely how to step).

> `editable` -> BooleanProperty -> Whether text input is able to be typed by

the user.

> `editor` -> ReadOnlyObjectProperty<TextField> The editor control used by the Spinner.
> `promptText` -> StringProperty -> The prompt text to display when there is no

user input.

> `valueFactory` -> ObjectProperty<SpinnerValueFactory<T>> -> As discussed in the preceding text.
> `value` -> ReadOnlyObjectProperty<T> -> The value selected by the user.

```java
Spinner<Integer> spinner = new Spinner<>();
spinner.setValueFactory(new SpinnerValueFactory.IntegerSpinnerValueFactory(5, 10));
spinner.valueProperty().addListener((o, oldValue, newValue) -> {
    log("value changed: '" + oldValue + "' -> '" + newValue + "'");
});
```

### Tooltip

Tooltips are common UI elements which are typically used for showing additional
information about a Node in the scene graph when the Node is hovered over by the
mouse.

> `install(Node, [new Tooltip(...)])` -> Configure the UI renderer to show a tootip on the node if the node is hovered
> `graphic` -> ObjectProperty<Node> -> An icon or arbitrarily complex scene graph to display within the Tooltip popup.
> `text` -> StringProperty -> The text to display within the Tooltip popup.
> `wrapText` -> BooleanProperty -> Whether to wrap text when it exceeds the Tooltip width.

```java
Rectangle rect = new Rectangle(0, 0, 100, 100);
Tooltip t = new Tooltip("A Square");
Tooltip.install(rect, t);

// Or using setToolTip() method of controls
Button button = new Button("Hover Over Me");
button.setTooltip(new Tooltip("Tooltip for Button"));
```

> `Control.setTooltip(new Tooltip(...))` -> Similar to `Tooltip.install()`

## Popup Controls

Behind the scenes, popup controls are placed in their own window that is separate from the main stage of the user interface, and as such they may appear outside of the window in situations whether they are taller or wider than the window itself.

### Menu-Based Controls

#### Menu & MenuItem

Building a menu in JavaFX starts with the Menu and MenuItem classes. Both classes are notable for not actually extending Control, which is because they are designed to represent a menu structure, but the implementation is handled behind the scenes by JavaFX.

* MenuItem (Required to be used with Menu component)
MenuItem acts essentially in the same fashion as a Button does. It supports a similar set of properties – `text` , `graphic` , and `onAction` . On top of this, it adds support for specifying keyboard accelerators (e.g., Ctrl-c).

> `CheckMenuItem extends MenuItem` -> Add Checkbox to the menu item
> `RadioMenuItem extends MenuItem` -> Add radio button to the menu item
> `SeparatorMenuItem extends MenuItem` -> Add separator to the menu items of a menu
> `CustomMenuItem` -> allows developpers to embbed custom controls in the Menu control.

`accelerator` -> ObjectProperty<KeyCombination> -> A keyboard shortcut to access this menu item.

> `disable` -> BooleanProperty -> Whether the menu item should be user interactive. > `graphic` -> ObjectProperty<Node> -> The graphic to show to the left of the menu item text.

`onAction` -> ObjectProperty<EventHandler<ActionEvent>> -> The event handler to be called when the menu item is clicked.

> `text` -> StringProperty -> The text to display in the menu item.
> `visible` -> BooleanProperty -> Whether the menu item is visible in the menu or not.

* Menu
It has `getItems()` method that works in similar standard way of most other JavaFX APIs. Menu class extends the `MenuItem` class, to makes it a candidate to the `getItems().add()` method to create a submenu.

#### MenuBar

This class is traditionally placed at the top of the user interface (e.g., if a BorderLayout is used, it is typically set to be the top node), and it is constructed simply by creating an instance and then adding Menu instances to the list returned by calling getMenus().

**Note**
JavaFX supports this, and the MenuBar class has a `useSystemMenuBar` property that, if set to true, will remove the MenuBar from the application window and instead render the menu bar natively using the system menu bar. This will happen automatically on platforms that have a system menu bar `(MacOS)` , but will have no effect on platforms that do not (and in which case, the MenuBar will be positioned in the user interface however it is specified to appear by the application developer).

```java
// Firstly we create our menu instances (and populate with menu items)
final Menu fileMenu = new Menu("File");
final Menu helpMenu = new Menu("Help");
// we are creating a Menu here to add as a submenu to the File menu
Menu newMenu = new Menu("Create New...");
newMenu.getItems().addAll(
    makeMenuItem("Project", console),
    makeMenuItem("JavaFX class", console),
    makeMenuItem("FXML file", console)
);
// add menu items to each menu
fileMenu.getItems().addAll(
    newMenu,
    new SeparatorMenuItem(),
    makeMenuItem("Exit", console)
);
helpMenu.getItems().addAll(makeMenuItem("Help", console));
// then we create the MenuBar instance and add in the menus
MenuBar menuBar = new MenuBar();
menuBar.getMenus().addAll(fileMenu, helpMenu);
```

#### MenuButton and SplitMenuButton

* MenuButton
MenuButton is a button-like control that, whenever clicked, will show a menu
consisting of all MenuItem elements added to the items list. Because the MenuButton
class extends from ButtonBase (which itself extends from Labeled), there is a significant amount of API overlap with the JavaFX Button control.

* SplitMenuButton

It extends the MenuButton class, but unlike MenuButton, the visuals
of SplitMenuButton split the button itself into two pieces:

-- “action area” : When clicked by the user  the `SplitMenuButton` essentially
acts as if it were a Button executing whatever code is associated with the onAction
property.

-- “menu open area”: When cliked, the popup menu is shown, and the user may interact with the menu as per usual.

> `popupSide` -> ObjectProperty<Side> -> The side the context menu should be shown relative to the button.

```java
MenuButton menuButton = new MenuButton("Choose a meal...");
menuButton.getItems().addAll(
    makeMenuItem("Burgers", console),
    makeMenuItem("Pizza", console),
    makeMenuItem("Hot Dog", console)
);
// because the MenuButton does not have an 'action' area,
// onAction does nothing
menuButton.setOnAction(e -> log("MenuButton onAction event"));

SplitMenuButton splitMenuButton = new SplitMenuButton();
// this is the text in the 'action' area
splitMenuButton.setText("Perform action!");
// these are the menu items to display in the popup menu
splitMenuButton.getItems().addAll(
    makeMenuItem("Burgers", console),
    makeMenuItem("Pizza", console),
    makeMenuItem("Hot Dog", console)
);
// splitMenuButton does fire an onAction event,
// when the 'action' area is pressed
splitMenuButton.setOnAction(e -> log("SplitMenuButton onAction event"));
```

#### ContextMenu

`ContextMenu` is a popup control that contains within it MenuItems. This means that it is never added to a scene graph and instead is called either directly (via the two `show()` methods) or as a consequence of a user requesting a context menu to show using common mouse or keyboard operations (most commonly via right-clicking the mouse).

```java
// create a standard JavaFX Button
Button button = new Button("Right-click Me!");
button.setOnAction(event -> log("Button was clicked"));
// create a ContextMenu
ContextMenu contextMenu = new ContextMenu();
contextMenu.getItems().addAll(
    makeMenuItem("Hello", console),
    makeMenuItem("World!", console),
    new SeparatorMenuItem(),
    makeMenuItem("Goodbye Again!", console)
);
```

In some cases, we want to show a ContextMenu on a class that does not extend from
Control. In these cases, we can simply make use of one of the two show() methods on
ContextMenu to display it when relevant events come up. There are two show() methods
available:

* show(Node anchor, double screenX, double screenY): This method will show the context menu at the specified screen coordinates.
* show(Node anchor, Side side, double dx, double dy): This method will show the context menu at the specified side (top, right, bottom, or left) of the specified anchor node, with the amount of x- and y-axis shifting specified by dx and dy, respectively (also note that dx and dy can be negative if desired, but most commonly these values can simply be zero).

```java
Rectangle rectangle = new Rectangle(50, 50, Color.RED);
rectangle.setOnContextMenuRequested(e -> {
    // show the contextMenu to the right of the rectangle with zero
    // offset in x and y directions
    contextMenu.show(rectangle, Side.RIGHT, 0, 0);
});
```

### ComboBox-Based Controls `Base class : ComboBoxBase`

Combobox based control will show their popup at bottom to allow users to make selection.

> `value` -> ? -> Current selected value ob the control
> `editable` -> BooleanProperty -> Makes the control editable
> `show()` -> Function show the hidden part of the combo box programmatically
> `hide()` -> Function hide the hidden part of the combo box programmatically
> `onAction` -> ObjectProperty<EventHandler<ActionEvent>> -> The event handler when the user sets a new value.
> `promptText` -> StringProperty -> The prompt text to display – whether it displays is dependent on the subclass.

#### ComboBox

Performant when large lists of elements are needing to be displayed.

> `cellFactory` -> ObjectProperty<Callback<ListView<T>,ListCell<T>>> -> Used to customize rendering of items.
> `converter` -> ObjectProperty<StringConverter<T>> -> Converts user-typed input(when editable) to an object of type T to set as value.
> `items` -> ObjectProperty<ObservableList<T>> -> The elements to show in popup.
> `placeholder` -> ObjectProperty<Node> -> What to show when the ComboBox has no items.
> `selectionModel` -> ObjectProperty <SingleSelectionModel<T>> -> Selection model of ComboBox.

```java
ComboBox<String> comboBox = new ComboBox<>();
comboBox.getItems().addAll(
    "Apple",
    "Carrot",
    "Orange",
    "Banana",
    "Mango",
    "Strawberry"
);
comboBox.getSelectionModel()
 .selectedItemProperty()
 .addListener((o, oldValue, newValue) -> log(newValue));
```

#### ColorPicker

The ColorPicker control is a specialized form of ComboBox, designed specifically to
allow users to select a color value.

**Note**
The ColorPicker control does not add any additional
functionality on top of ComboBoxBase, but of course the user interface is vastly different.

```java
final ColorPicker colorPicker = new ColorPicker();
colorPicker.setOnAction(e -> {
    Color c = colorPicker.getValue();
    System.out.println("New Color RGB = "+c.getRed()+" "+c.getGreen()+" "+c.getBlue());
});
```

#### DatePicker

`DatePicker` is a specialization of `ComboBoxBase` for selecting dates – in this case a `java.time.LocalDate` value.

> `chronology` -> ObjectProperty<Chronology> -> Which calendar system to use.
> `converter` -> ObjectProperty<StringConverter<LocalDate>> -> Converts text input into a LocalDate and vice versa.
> `dayCellFactory` -> ObjectProperty<Callback<DatePicker,DateCell>> -> Cell factory to customize individual day cells in popup.
> `showWeekNumbers` -> BooleanProperty -> Whether the popup should show
week numbers.

```java
final DatePicker datePicker = new DatePicker();
datePicker.setOnAction(e -> {
    LocalDate date = datePicker.getValue();
    System.err.println("Selected date: " + date);
});
```

### JavaFX Dialogs (Java 8)

* A `modal` dialog is one that appears atop another window and prevents the user from clicking that window until the dialog is dismissed.

* A `blocking` dialog is one that causes code execution to stop at the very line that caused the dialog to appear. This means that, once the dialog is dismissed, execution continues from that line of code. This can be thought of as a `synchronous dialog`. Blocking dialogs are simpler to work with, as developers can retrieve a return value from the dialog and continue execution without needing to rely on listeners and callbacks.

Note: In Java all dialogs are modal. Calling `initModality(Modality)` makes the dialog non-modal.

> `showAndWait()` -> Open dialog in blocking fashion
> `show()` -> In non-blocking fashion

#### Alert

Show the pre-built OS dialog.

Creating an Alert is simply a matter of calling the constructor with the desired `AlertType` specified. `AlertType` is used to configure which buttons and which graphic are shown by default. Here is a quick summary of the options:

-- `Confirmation` -> Best used to confirm that a user is sure before
performing some action.
-- `Error` -> Best used to inform the user that something has gone wrong.
Shows a red “X” image and a single “OK” button.
-- `Information` -> Best used to inform the user of some useful information.
Shows a blue “I” image (to represent “information”) and a single
“OK” button.

-- `None` -> This will result in no image and no buttons being set. This
should rarely be used unless a custom implementation is about to be
provided.

-- `Warning` -> Best used to warn user of some fact or pending problem.
Shows a yellow exclamation mark image and a single “OK” button.

```java
alert.showAndWait()
 .filter(response -> response == ButtonType.OK)
 .ifPresent(response -> formatSystem());
```

#### TextInputDialog

TextInputDialog is similar to ChoiceDialog, except rather than allow a user to make a selection from a popup list, it instead enables a user to provide a single line of text input.

> `getEditor()` -> TextField -> The TextField the user is shown in the dialog.

```java
TextInputDialog. dialog = new TextInputDialog ("Please enter your name");
dialog.showAndWait()
    .ifPresent(result -> log("Result is " + result));
```

#### ChoiceDialog

ChoiceDialog is a dialog that shows a list of choices to the user, from which they can pick one item at most. In other words, this dialog will use a control such as a ChoiceBox or ComboBox (it is left as an implementation detail; a developer cannot specify their preference) to enable a user to make a selection.

```java
ChoiceDialog<String> dialog = new ChoiceDialog<>("Cat", "Dog", "Cat", "Mouse");
dialog.showAndWait()
    .ifPresent(result -> log("Result is " + result));
```

## JavaFX Advanced Controls

### ListView

It is generic class `ListView<T>` able to contains items of type `T`.

**Note**
a `ListView` only creates enough “cells” to contain the elements in the visible area of the `ListView`. The `ListView` control implements a virtual scrolling to show content to the user. By default, `ListView` scroll vertically. But the orientation can be changed.

> `cellFactory` -> ObjectProperty<Callback<ListView<T>, ListCell<T>>> -> Factory function to creates list view cells.
> `editable` -> BooleanProperty -> Whether the ListView supports editing
cells.
> `selectionModel`
> `focusModel` -> ObjectProperty<FocusModel<T>> -> Handles focused elements of the list
> `items` -> ObjectProperty<ObservableList<T>> -> The elements to show within the
`ListView`.
> `orientation` -> ObjectProperty<Orientation> -> Whether the ListView is vertical or horizontal.
> `placeholder` -> ObjectProperty<Node> -> Text to display within the ListView if the items list is empty.
`selectionModel` -> ObjectProperty<MultipleSelectionModel<T>> -> Handles the selected element of the list view.

* Cells and Cell Factories `javafx.scene.control.Cell extends javafx.controls.Labeled`

Cell factories defines how list view child control are constructed/rendered when presenting the list view. Works the same in `TableView` and `TreeTableView`.

> `editable` -> BooleanProperty -> Whether the Cell instance can enter an editing
state.
> `editing` -> ReadOnlyBooleanProperty -> Whether the Cell is currently in an editing state
> `empty` -> ReadyOnlyBooleanProperty -> Whether the Cell has any item.
> `item` -> ObjectProperty<T> -> The object the Cell is currently representing.
> `selected` -> ReadOnlyBooleanProperty -> Whether the Cell has been selected by the user.

**Note**
When working with a UI control, such as `ListView`, developers do not use Cell
directly, but rather a control-specific subclass (in the case of `ListView`, this would be ListCell). For the TableView and TreeTableView controls, there are in fact two cell types – `TableRow`/`TreeTableRow` and `TableCell`/`TreeTableCell`.

```java
public class ColorRectCell extends ListCell<String> {

    private final Rectangle rect = new Rectangle(100, 20);

    @Override public void updateItem(String item, boolean empty) {
        super.updateItem(item, empty);
        if (empty || item == null) {
            setGraphic(null);
        } else {
            rect.setFill(Color.web(item));
            setGraphic(rect);
        }
    }
}
```

* Cell Editing
When a custom Cell is to be editable, we enable support for it simply by extending the updateItem method, to also add checks to see if the cell is being used to represent the current editing index in the control.

**Note**
For many of the common cases, there already exist a number of pre-built cell
factories that support editing shipping with the core JavaFX APIs, contained within the `javafx.scene.control.cell`.

```java
public class EditableListCell extends ListCell<String> {
    private final TextField textField;
    public EditableListCell() {
        textField = new TextField();
        textField.addEventHandler(KeyEvent.KEY_PRESSED, e -> {
            if (e.getCode() == KeyCode.ENTER) {
                commitEdit(textField.getText());
            } else if (e.getCode() == KeyCode.ESCAPE) {
                cancelEdit();
            }
        });
        setGraphic(textField);
        setContentDisplay(ContentDisplay.TEXT_ONLY);
    }

    @Override public void updateItem(String item, boolean empty) {
        super.updateItem(item, empty);
        setText(item);
        setContentDisplay(isEditing() ?
        ContentDisplay.GRAPHIC_ONLY : ContentDisplay.TEXT_ONLY);
    }

    @Override public void startEdit() {
        super.startEdit();
        setContentDisplay(ContentDisplay.GRAPHIC_ONLY);
        textField.requestFocus();
    }

    @Override public void commitEdit(String s) {
        super.commitEdit(s);
        setContentDisplay(ContentDisplay.TEXT_ONLY);
    }

    @Override public void cancelEdit() {
        super.cancelEdit();
        setContentDisplay(ContentDisplay.TEXT_ONLY);
    }
}
```

* Pre-built Cell Factories
JavaFX ships with a number of pre-built cell factories that make customizing ListView and others a very easy task.

> `TextFieldListCell` -> Editable ListView Cell
> `ProgressBarTableCell` -> Progress bar cell in TableCell component
> `CheckBox` -> ListView, TableView, TreeView, TreeTableView
> `ChoiceBox` -> ListView, TableView, TreeView, TreeTableView
> `ComboBox` -> ListView, TableView, TreeView, TreeTableView
> `ProgressBar` -> TableView, TreeTableView
> `TextField` -> ListView, TableView, TreeView, TreeTableView

```java
ListView<String> listView = new ListView<>();
listView.setEditable(true);
listView.setCellFactory(param -> new TextFieldListCell<>());
```

### TreeView

The TreeView control is the go-to control inside the JavaFX UI toolkit for displaying treelike data structures to users, for example, for representing a file system or a corporate hierarchy.

**Note**
`TreeView` requires a root property of type `TreeItem<T>`, with `T` being the type of the elements in the tree.

> `cellFactory` ->  ObjectProperty<Callback<TreeView<T>,TreeCell<T>>> -> Cell factory used for creating all cells.
> `editable` -> BooleanProperty -> Whether the TreeView is able to enter editing state.
> `editingItem` ReadOnlyObjectProperty<TreeItem<T>> -> The TreeItem currently being edited.
> `expandedItemCount` -> ReadOnlyIntegerProperty -> The total number of tree nodes able to be visible in the TreeView.
> `focusModel` -> ObjectProperty<FocusModel<TreeItem<T>>> -> Handles focused elements of the list
> `root` -> ObjectProperty<TreeItem<T>> -> The root tree item in the TreeView.
> `selectionModel` -> ObjectProperty<MultipleSelectionModel<TreeItem<T>>> -> Handles selected element of the component
> `showRoot` -> BooleanProperty -> Whether the root is shown or not. If not, all children of the root will be shown as root elements.

* TreeItem
TreeItem is a relatively simple class and behaves in a similar manner to MenuItem.

> `expanded` -> BooleanProperty -> Whether this TreeItem is expanded or collapsed.
> `graphic` -> ObjectProperty<Node> -> The graphic to show beside any text or other representation.
> `leaf` -> ReadOnlyBooleanProperty -> Whether this TreeItem is a leaf node or has children.
> `parent` -> ReadOnlyObjectProperty <TreeItem<T>> -> The parent TreeItem of this TreeItem, or null if it is the root.
> `value` -> ObjectProperty<T> -> The value of the TreeItem – this is what will be rendered in the cell of the TreeView/TreeTableView control.

### TableView

`TableView`, as the name implies, enables developers to display tabular data to users. This control, therefore, can be thought of as a `ListView` with support for multiple columns of data, rather than the single column in a `ListView`.

With this comes a vast array of additional functionality: columns may be `sorted`, `reordered`, `resized`, and `nested`, individual columns may have custom cell factories installed, `resize` policies can be set to control how columns have available space distributed to them, and so much more.
`TableView` has a single generic type, S, which is used to specify the value of the elements allowed in the items list. Each element in this list represents the backing object for one entire row in the `TableView`. For example, if the TableView was to show Person objects, then we would define a `TableView<Person>` and add all the relevant people into the items list.

> `columnResizePolicy` -> ObjectProperty<Callback<ResizeFeatures,Boolean>> -> This handles redistributing column space when columns or the table are resized.
> `comparator` -> ReadOnlyObjectProperty<Comparator<S>> -> The current comparator based on the table columns in the `sortOrder` list.
> `editable` -> BooleanProperty -> Whether the TableView is able to enter editing state.
> `editingCell` -> ReadOnlyObjectProperty<TablePosition<S,?>> -> The position of any cell that is currently being edited.
> `focusModel` -> ObjectProperty<TableViewFocusModel<S>> -> Handles focused elements of the list.
> `items` -> ObjectProperty<ObservableList<S>> -> The elements to show within the `TableView`.
> `placeholder` -> ObjectProperty<Node> -> Text to display within the ListView if the items list is empty.
> `rowFactory` -> ObjectProperty<Callback<TableView<S>,TableRow<S>>> -> The rowFactory is responsible for creating an entire row of TableCells(for all columns).
> `selectionModel` -> ObjectProperty<TableViewSelectionModel<S>> -> Handles selected element of the component.
> `sortPolicy` -> ObjectProperty<Callback<TableView<S>,Boolean>> -> Specifies how sorting should be performed.
> `tableMenuButtonVisible` -> BooleanProperty -> Specifies whether a menu button should show in the top right of TableView

* TableColumn and TreeTableColumn
`TableColumn` exists in the set of classes in JavaFX UI controls that do not extend from Control (previous examples we’ve discussed include `MenuItem`, `Menu`, and `TreeItem`). `TableColumn` extends from `TableColumnBase`, as `TreeTableView` has similar (but not fully identical) API, which therefore necessitated the creation of `TreeTableColumn`. Despite the need for different classes for TableView and TreeTableView, there is still significant overlap, which is why most API is on `TableColumnBase`.

> `comparator` -> ObjectProperty<Comparator<T>> -> The comparator to use when this column is part of the table sortOrder list.
> `editable` -> BooleanProperty -> Specifies if this column supports editing.
> `graphic` -> ObjectProperty<Node> -> Graphic to show in the column header area.
> `parentColumn` -> ReadOnlyObjectProperty<TableColumnBase<S,?>> -> Refer to the “Nested Columns” section.
> `resizable` -> BooleanProperty -> Whether the width of the column can be changed by the user.
> `sortable` -> BooleanProperty Whether the column can be sorted by the user.
> `sortNode` -> ObjectProperty<Node> -> The “sort arrow” to show when the column is part of the sort order list.
> `text` -> StringProperty -> The text to display in the column header area.
> `visible` -> BooleanProperty -> Whether the column shows to the user or not.
> `width` -> ReadOnlyDoubleProperty -> The width of the column.

> `cellFactory` -> ObjectProperty<Callback<TableColumn<S,T>, TableCell<S,T>>> -> Cell factory for all cells in this table column.
> `cellValueFactory` -> ObjectProperty<Callback<CellDataFeatures<S,T>,ObservableValue<T>>> -> The cell value factory for all cells in this table column.
> `sortType` -> ObjectProperty<SortType> -> Specifies, when this column is part of the sort, whether it should be ascending or descending.

```java
ObservableList<Person> data = ...
TableView<Person> tableView = new TableView<Person>(data);
TableColumn<Person,String> firstNameCol = new TableColumn<Person,String>("First Name");
firstNameCol.setCellValueFactory(new Callback<CellDataFeatures<Person,String>, ObservableValue<String>>() {
    public ObservableValue<String> call(CellDataFeatures<Person, String> p) {
        // p.getValue() returns the Person instance for a particular TableView row 
        return p.getValue().firstNameProperty();
    }
});
tableView.getColumns().add(firstNameCol);
```

* Using a property value factory, JavaFX will try to find `classPropProperty()` method and bind to it. If the method is missing from the object, it try to find `getClassProp()` method and display it without binding to it, simply displaying it.

```java
// Preceeding code looks like with PropertyValueFactory
TableColumn<Person,String> firstNameCol = new TableColumn<Person,String>
("First Name");
firstNameCol.setCellValueFactory(new PropertyValueFactory("firstName"));
````

* or wrapping non-property values for used in JavaFX TableView:

```java
firstNameCol.setCellValueFactory(new Callback<CellDataFeatures<Person,
String>, ObservableValue<String>>() {
    public ObservableValue<String> call(CellDataFeatures<Person, String> p) {
        return new ReadOnlyObjectWrapper(p.getValue().getFirstName());
    }
});
```

**Note**
For the `TreeTableView` control, a class similar to the `PropertyValueFactory`
exists, called `TreeItemPropertyValueFactory`. It performs the same function as the
`PropertyValueFactory` class, but it is designed to work with the TreeItem class that is
used as part of the data model of the `TreeTableView` class.

#### Nested Columns

The `JavaFX` TableView and TreeTableView controls both have built-in support for column nesting. This means that, for example, you may have a `“Name”` column that contains two sub-columns, for first name and last name. The `“Name”` column is for the most part decorative – it isn’t involved in providing a cell value factory or cell factory (this is the responsibility of the child columns), but it can be used by the user to reorder the column position and to resize all child columns.

```java
TableColumn firstNameCol = new TableColumn("First Name");
TableColumn lastNameCol = new TableColumn("Last Name");
TableColumn nameCol = new TableColumn("Name");
nameCol.getColumns().addAll(firstNameCol, lastNameCol);
```

### TreeTableView

The high-level summary of `TreeTableView` is that it uses the same `TreeItem` API
as `TreeView`, and therefore it is required for developers to set the root node in the
`TreeTableView`.

**Note**
`TreeTableView` control makes use of the same `TableColumn-based` approach that the TableView control uses, except instead of using the `TableView-specific` `TableColumn` class, developers will need to use the largely equivalent `TreeTableColumn` class instead.

> `columnResizePolicy` -> ObjectProperty<Callback<ResizeFeatures, Boolean>> -> This handles redistributing column space when columns or the table are resized.
> `comparator` -> ReadOnlyObjectProperty<Comparator<TreeItem<S>>> ->The current comparator based on the table columns in the sortOrder list.
> `editable` -> BooleanProperty -> Whether the TableView is able to enter editing state.
> `editingCell` -> ReadOnlyObjectProperty<TreeTablePosition<S,?>> -> The position of any cell that is currently being edited.
> `expandedItemCount` -> ReadOnlyIntegerProperty -> The total number of tree nodes able to be visible in the `TreeTableView`.
> `focusModel` -> ObjectProperty<TreeTTableViewFocusModel<S>> -> Refer to the “Selection and Focus Models” section.
> `items` -> ObjectProperty<ObservableList<S>> -> The elements to show within the TableView.
> `placeholder` -> ObjectProperty<Node> Text to display within the ListView if the items list is empty.
> `root` -> ObjectProperty<TreeItem<S>> -> The root tree item in the TreeTableView.
> `rowFactory` -> ObjectProperty<Callback<TreeTableView<S>,TreeTableRow<S>>> -> The rowFactory is responsible for creating an entire row of `TreeTableCells` (for all columns).
> `selectionModel` -> ObjectProperty<TreeTableViewSelectionModel<S>> -> Refer to the “Selection and Focus Models” section.
> `sortPolicy` -> ObjectProperty<Callback<TreeTableView<S>,Boolean>> -> Specifies how sorting should be performed.
> `tableMenuButtonVisible` -> BooleanProperty -> Specifies whether a menu button should show in the top right of TreeTableView.
> `treeColumn` -> ObjectProperty <TreeTableColumn<S,?>> Which column should have the disclosure node drawn within it.

### Selection and Focus Models

This abstraction makes it simpler for developers to understand all UI controls,
as they offer the same API for common scenarios. 

#### SelectionModel

`SelectionModel` is an abstract class extended with a single generic type, `T`, that represents the type of the selected item in the related UI control.

> `selectedIndex` -> ReadOnlyIntegerProperty -> The currently selected cell index in the UI control.
> `selectedItem` -> ReadOnlyObjectProperty<T> -> The currently selected item in the UI control.

* SingleSelectionModel

It' s used in UI controls where only a single selection can be made at a time.

* MultipleSelectionModel

`MultipleSelectionModel` supports there being multiple selections existing at the same time (e.g., multiple rows in a ListView may be selected at the same moment).

> `selectedIndices` -> ObservableList<ReadOnlyIntegerProperty> -> List of selected cell indexes.
> `selectedItems` -> ObservableList<ReadOnlyObjectProperty<T>> -> Observable list of selected item in the control

* TreeTableViewSelectionModel & TableViewSelectionModel

These classes add APIs to change selection mode between row and cell selection, and when in cell selection mode make it possible to select cells based on their row/column intersection points.

> `selectedCells` -> ObservableList<ReadOnlyObjectProperty<TablePosition<S,?>>> -> List of cell selected

#### FocusModel

In `JavaFX`, the more correct use of `focus` is related to what happens when the user `“tabs”` through a user interface.

**Note**
Some UI controls have overloaded the term focus to also mean what could more precisely be referred to as “internal focus.” The ListView, TreeView, TableView, and TreeTableView controls all have focus models to allow for programmatic manipulation and observation of this internal focus.

**Note**
In this regard, the focus is not on a Node, but rather on an element inside the UI control, and we do not concern ourselves with the Node, but the value (of type T) in that row (as well as the index position of that row).

> `focusedIndex` -> ReadOnlyIntegerProperty -> The currently focused cell index in the UI control.
> `focusedItem` -> ReadOnlyObjectProperty<T> -> The currently focused item in the UI control.