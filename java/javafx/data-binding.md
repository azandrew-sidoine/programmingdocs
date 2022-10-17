# JavaFX Data Bindings

JavaFX `javafx.base` is the home of most properties binding classes. It export the list of packages below:

```java
import javafx.beans;
import javafx.beans.binding; // JavaFX bindings
import javafx.beans.property;
import javafx.beans.property.adapter; // Property adapters for types
import javafx.beans.value; // For observable value classes
import javafx.beans.collections; // For working with observable collections
import javafx.collections.transformation; // Transformation function of the jfx collections
import javafx.event; // Event classes
import javafx.util; // Utilities classes
import javafx.util.converter; // Convertion utilities classes
```

## Property Bindings

### Observable & InvalidationListener

`InvalidationListener` is registered on an `Observable` instance, to get notified when the binding becomes invalid.

**Note**
A Property becomes invalidated if its set() or setValue() method is called with a value different from its currently held value. A Binding becomes invalidated when its invalidate() method is called or when its dependencies become invalidated.

**Warning**
An invalidation event is fired only once by the properties in JavaFX if you call the setters with the same value several times in a row.

### ObservableValue & ChangeListener

`ChangeListeners` can be registered on `ObservableValue` types. Listeners are notified when property binding value change from one value to another.

**Note**
Weak versions of the InvalidationListener and the ChangeListener, and some other listeners introduced later in this chapter, exist to help avoid memory leaks.

### WritableValue and ReadOnlyProperty

`WritableValue` provides a `setValue` method interface, while `ReadOnlyProperty` interface inject 2 method `getBean() -> Holder of the property` & `getName() -> Descriptive property name` .

### Property

> `bind()` -> established unilateral property binding, between a property and an `ObservableValue` . (1)
> `unbind()` -> release the binding created in (1). (2)
> `isBound()` -> Return boolean value indicating if binding is in effect.
> `set()|setValue()` -> Throws RuntimeException when called in `bind` mode, but in `bindBidirectional` mode, they update the value of both source and destination
> `get()|getValue()` -> return the `ObservableValue` of the property.

**Warning**
each Property may have at most one active unidirectional binding at a time. it may have as many bidirectional bindings as you want. the isBound() method pertains only to unidirectional bindings. Calling bind() a second time with a different ObservableValue will unbind the previous one and replace it with the new one.

**Note**
`prop1.bind(prop2)` -> Changes from property `prop2` will update `prop1` .

### Bindings

```java
public interface Binding {

    public boolean isValid(); // Binding validity can be queried when if `isValid()` returns true
    public void invalidate(); // Invalidate the binding
    public ObservableList<?> getDependencies(); // Returns the list of dependant properties
    void dispose(); // Invoke to signals that the binding is not usable anymore
}
```

**Note**
When a binding is marked invalidated, call to `get()` and `getValue()` calls recalculate it value based on dependencies. Else, the a cached value is returned till the binding state become invalidated again.

**Warning**
as with any complex structures, care must be taken to avoid performance degradations and behavior mistakes, especially under high-load scenarios.

### Bindings Factory Methods

The Bindings class contains more than 200 factory methods that make new bindings out of existing observable values and regular values.

> `add(...): NumberBinding` -> Compute the sum of observable value of JavaFX properties
> `substract(...): NumberBinding` -> Compute the substraction of observable value of JavaFX properties
> `multiply(...): NumberBinding` -> Compute the multiplication of observable value of JavaFX properties
> `divide(...): NumberBinding` -> Compute the division of observable value of JavaFX properties
> `or()` -> Compute Logical `or` comparison of JavaFX observable value
> `and()` -> Compute Logical `and` comparison of JavaFX observable value
> `not()` -> Compute Logical `negation` comparison of JavaFX observable value
> `min()` -> Compute `min` of an observable value
> `max()` -> Compute `max` of an observable value
> `negate()` -> Compute `opposite` of a Java expression on an Observable value

Ex: `lenght` , `isNull()` , `isNotNull()` , `isEmpty()` , `isNotEmpty` , `isEmpty` , `equal()` , `equalIgnoreCase()` , `greaterThan()` , `graterThanOrEqual()` , `lessThan()` , `lessThanOrEqual()` , `notEqual()` , and `notEqualIgnoreCase()` .

> `Bindings.createDoubleBinding(javafx.util.Callable)` -> Create a binding from a callable instance.

**Note** All this method returns a binding `NumberBinding` class, that get update when properties value changes.

```java
// sendButton is enabled only when recipient is not selected and amount is not greater than 0
sendBtn.disableProperty().bind(Bindings.not(
    Bindings.and(recipientSelected,
        Bindings.greaterThan(amount, 0.0))));
```

**Note**
The `convert()` , `concat()` , and a couple of overloaded `format()` methods can be used to convert non-string observable values into observable string values

```java
// Each time the text property changes, it's formatted to a double with 1 decimal point.
tempLbl.textProperty().bind(Bindings.format("%2.1f \u00b0C",
        temperature));
```

### Fluent API

The fluent API for creating bindings is embodied in the IntegerExpression series of classes. These expression classes are superclasses of both the property classes and the binding classes. Thus, the fluent API methods
are readily available from the familiar property and binding classes.

With fluent api, `sendBtn` example can be written like:

```java
sendBtn.disableProperty().bind(recipientSelected.and(amount.greaterThan(0.0)).not());
```

And temparature example like:

```java
temperature.asString("%2.1f \u00b0C")
```

**Note**
Numeric bindings built with the `fluent API` have more specific types than those built with factory methods in the `Bindings` class.

> `When(ObservableValue o)` -> It's the class allowing to perform if/then/else logic in the fluent API.
> `then(Object|Observable result)` -> Overloaded on the `When` object, with nested condition, returning if clause result.
> `otherwise(Object|Observavble alternative)` -> Overloaded method on then object, returns else clause result.

**Note**
It should be noted that the fluent API has its limitations. As the relationship becomes more complicated or goes beyond the available operators, the direct extension method is preferred.

Direct expression example, provides a mechanism to inherit from existing binding class, an provide the mechanism to compute the result of an expression in `computeValue` , when the binded properties changes.

It can be used to create angular Pipe like classes, to compute the result of a binded expression.

```java
DoubleBinding area = new DoubleBinding() {
    {
        super.bind(a, b, c);
    }
    @Override
    protected double computeValue() {
        double a0 = a.get();
        double b0 = b.get();
        double c0 = c.get();
        if ((a0 + b0 > c0) && (b0 + c0 > a0) &&
                (c0 + a0 > b0)) {
            double s = (a0 + b0 + c0) / 2.0D;
            return Math.sqrt(s * (s - a0) *
                    (s - b0) * (s - c0));
        } else {
            return 0.0D;
        }
    }
};
```

### Observable Collections `javafx.collections`

They allow to observe(register, unregister and listen for changes) on the data structure they manipulate.

```java
import javafx.collections.ObservableList; // Based on Java List collection. Has methods to manipulate Java list more efficiently.
import javafx.collections.ObservableMap; // Based on Java Map collection 
import javafx.collections.ObservableSet; // Based on java Set
import javafx.collections.ObservableArray; // Based on Java Array object. Mostly used in JavaFX 3D API as it hold primitive types int|float
```

> `ObservableList.iterator()` -> Creates an iterator from the observable list
> `ObservableList.remove(start, end)`

> `ObservableList.addAll(offset, List)`

#### FXCollections `javafx.collection.FXCollections`

The FXCollections utility class contains factory methods for creating observable collections and arrays. They resemble the factory methods in java.util. Collections except that they return observable collections and arrays.

Manipulation methods `copy()` , `addAll(observable, [List])` , `fill()` , `reverse(observable)` , `rotate(observable, [int])` , `shuffle()` , `sort(observable, [Lambda])` , etc... provided by fxcollections are efficient in minimizing notification changes.

> `FXCollections.observableArrayList()`

> `FXCollections.observableHashMap()`

> `FXCollections.observableSet()`

> `FXCollections.observableFloatArray()`

> `FXCollections.observableIntegerArray()`

```java
FXCollections.observableFloatArray().addListener((array, sizeChanged, from, to) -> {
    // sizeChanged -> The current change
    // from -> Last state of the array
    // to -> current state of the array
});
```

#### Create Bindings for Observable Collections

The Bindings utility class includes factory methods for creating bindings out of observable collections.

> `bindContent()` -> Bind changes of an observable collectoon to a non-observable collection. Non-observable collection changes whenever obserble changes.

**Note**
The overloaded methods valueAt(), booleanValueAt(), intgerValueAt(), longValueAt(), floatValueAt(), doubleValueAt(), and stringValueAt() create a binding of the appropriate type out of an observable collection of the same type, and an index or a key of the appropriate type, either observable or non-observable.

### JavaFX Beans `javafx.beans`

The Java Beans concept existed almost from the beginning. It introduces three architectural concepts: properties, events, and methods.

* `Methods` are straightforward in Java.
* `Events` are provided through listener interfaces and event objects, which JavaFX controls still use.
* `Properties` are provided using the now very familiar public getter and setter methods.

**Note**
JavaFX introduces the JavaFX Bean concept where in addition to the getter and the setter, a JavaFX Bean property also has a property `getter` returning a property `Property` .

* Eagerly Instantiated Property

It's the same concept used when creating the `Person` class in the `modernclient` project.

* Half-Lazily Instantiated Property

If the setter and the property getter are never called, the getter will always return the default value of a property; and you don’t need a property instance to know that. This is the basis of the half-lazy instantiation strategy

**Note**
In this strategy the property is instanciated if it get called.

```java

import javafx.beans.property.StringProperty;
import javafx.beans.property.SimpleStringProperty;

public class ExampleModel {

    private static final String _defaultStr = "";
    private StringProperty str;
    private String _str = _defaultStr;

    public final String getStr() {
        if (str != null) {
            return str.get()
        }
        return _str;
    }

    public void setStr(String value) {
        if ((str != null) || !value.equals(_defaultStr)) {
            str.set(value);
            return;
        }
        _str = value;
    }

    public StringProperty strProperty() {
        if (str == null) {
            str = new SimpleStringProperty(this, "str", _defaultStr);
        }
        return str;
    }
}
```

* Fully Lazily Instantiated Property

Provides an alternative to halfly instanciated property, with no initialization of the property.

### Selection Bindings

> `select(Object instsnce, String... steps)` -> Deeply select an `instance property` that is a JFX property.
> `selectInteger(Object instsnce, String... steps)` -> Deeply select an integer type JXF Property in a instance.

```java
//
final ObjectBinding<Color> colorBing = Bindings.select(root, "light", "color"); // Based on the analogy, the root object must have a `light` property which in turn is an object with `color` property
colorBinding.addListener((o, oldValue, newValue) ->
                System.out.println("\tThe color changed:\n" +
                        "\t\told color = " + oldValue +
                        ",\n\t\tnew color = " + newValue));
```

#### Adapting Java Beans

For the many old-fashioned Java Beans written over the years, JavaFX provides a set of adapter classes in the `javafx.beans.property.adapter` package that turn Java Bean properties into JavaFX properties.

**Note**
Recall that a Java Bean property is a bound property if a `PropertyChange` event is fired when the property is changed. It is a constrained property if a `VetoableChange` event is fired when it is changed.
It looks like Java implementation of C# or . NET `WPF` , `INotifyPropertyChanged` .

**Warning**
It is a constrained property if a `VetoableChange` event is fired when it is changed.
And if a registered listener throws a PropertyVetoException, the change does not take effect

```java

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.beans.PropertyVetoException;
import java.beans.VetoableChangeListener;
import java.beans.VetoableChangeSupport;

class Person {

    private PropertyChangeSupport propertyChanges = new PropertyChangeSupport(this);
    private VetoableChangeSupport vetoableChanges = new VetoableChangeSupport(this);

    private String name;
    private String address;

    public String getName() { return name; }
    public void setName(String value) { name = value }
    private JavaBeanStringProperty _nameProperty;

    // Or using java bean property builder
    public JavaBeanStringProperty nameProperty() {
        // A Java Bean property of type String can be adapted into a JavaBeanStirngProperty using the JavaBeanStringPropertyBuilder:
        if (_nameProperty == null) {
            _nameProperty = JavaBeanStringPropertyBuilder.create()
                                                    .bean(this)
                                                    .name("name")
                                                    .build();
        }
        return _nameProperty;
    }

    // Property changes
    public String getAddress() { return address; }
    public void setAddress(String value) {
        String oldValue = address;
        address = value;
        // Call to method notifying property changes just like in .NET implementation
        propertyChanges.firePropertyChange("address", oldValue, address);
        // Or using property builder using property builder
        // _nameProperty.fireValueChangedEvent();
    }

    public void addListener(PropertyChangeListener l) {
        propertyChanges.addPropertyChangeListener(l);
    }

    public void removeListener(PropertyChangeListener l) {
        propertyChanges.removePropertyChangeListener(l);
    }

    public PropertyChangeListener[] getListeners() {
        return propertyChanges.getPropertyChangeListeners();
    }

    public void addvetoableListener(VetoableChangeListener l) {
        vetoableChange.addVetoableChangeListener(l);
    }
    public void removeVetoableListener(VetoableChangeListener l) {
        vetoableChange.removeVetoableChangeListener(l);
    }
    public VetoableChangeListener[] getVetoableListeners() {
        return vetoableChange.getVetoableChangeListeners();
    }
}
```

To build a string property base on `name` be property:

```java
Person p = new Person();
// Adding listener to javafx bean property
p.nameProperty().addListener((observable, oldValue, newValue) -> {
            System.out.println("JavaFX property " +
                    observable + " changed:");
            System.out.println("\toldValue = " +
                    oldValue + ", newValue = " + newValue);
});
```
