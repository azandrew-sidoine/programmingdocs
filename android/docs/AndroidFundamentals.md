# Android Fundamentals

## Introduction

### Android Os is a Stack based OS

{ System Apps}  {User Apps} - System and User Applications
{ Java API Framework } - Android OS API in Java Framework `(View hierachy to create UI|Notification Manager|Activity Manager|Content Providers for data sharing)`

{ Native C/C++ } { Android Runtime (JVM)} - Runs Native APIs `ART`

{ Hardware Abstraction Layer (HAL)} - Exposes Device hardware capabilities
{ Linux Kernel } - `Threading and Low level memory management|Security|Drivers`

Note:

    From Android 4.4 Android migrated from Dalvik Virtual Machine `DVM` to Android RunTime `ART`

### Adroid Apps

* One or more interactive screens
* Writting Java and XML
* Uses Android SDK
* Android Libraries and Android Application Framework
* Executed by Android Runtime Virtual Machine (ART)

### Component types

* Activity - Single screen with UI. Let's say a activities are visual things

* Services - Performs long-running tasks in background.
    - Intents : Services that are available when requested
    - Background services

* Content Provider - Manages shared set of data
* Broadcast receiver - Responds to system-wide announcements, or sys-wide events and performs a given task.

## Basics

* The @ operator in XML files

`@` reference a resource element in the XML layout.
Resouces are `strings` , `color` , `mimap` , `drawable` , `styles` , etc... Meaning anything in `res` folder.

### Layout, Views and Resources

* View properties in XML

```xml
<TextView android:<property_name>="<property_value>" />

<TextView android:<property_name>="@<resource_type>/resource_id" />

<TextView android:<property_name>="@+id/view_id" />
```

* In Java code

```java
TextView textView = new TextView(this); // this is the context
textView.setText("Text value");
```

* Context

It's a global interface to the global information about an application environment.

```java
// Get the application context
Context context = getApplicationContext();
```

Note: An activity is a context on it own.

* View Group

It's a type of view that can contains other views(children). It's the base class for layout containers (ScrollView[ `Contains one child view` ], LinearView[ `arrange elements in h/v row` ], RecyclerView [ `Scrollable List view` ])

* Layout

They specify the view groups. They are subclasses of viewgroups.

-- ConstraintLayout - Connect views with constraints
-- LinearLayout - Vertically or Horizontally
-- RelativeLayout - Child Views relative to each other
-- TableLayout - In Row and Columns manner
-- FrameLayout - Stack Layout per say
-- GridView - 2D Scrollable grid

--- Layout Hierarchy

    It's how view elements are arranged.

* Event Handling

It provides a way to passing information between components upon user actions.

-- UI Events: Click, Tap, Drap
-- System Events
-- ActivityEvent: Walking

---- Event bindings

```xml
<Button android:text="@string/buttonText" android:onClick="clickHandler" />
```

```java
class ViewFragment extends Fragment {

    // view create methods

    public void clickHandler(View v)
    {
        Toast toast = Toast.makeText("", Toast.LENGTH_SHORT);
        toast.show();
    }
}
```

* Resources

They allow to separate static data from imperative codes.

Accessing resources:

```java
// Layout
// Loading layout into a component
R.layout.activity_main;
setContentView(R.layout.activity_main)

// View
// <RecyclerView android:id="recyclerView">
recycleView = (RecyclerView) findViewById(R.id.recyclerView);

// Strings
// In XML: <android:text="@string/title">
string = R.string.title;
```

* Measurements

-- Device Independent Pixels (dps) for View
-- Scale Independent Pixels (sp) for Text

#### TextView (TextView extends View)

It is a view element for displaying single and multiline texts.

AutoLink:

```xml
<TextView android:autoLink="web" android:text="@string/article_text" />
```

It add an href to the text view so that when user click on it, they are redirected to web view.

#### EditView (Text input) (EditView extends TextView)

Textview with an editable text.

#### ScrollView (ScrollView extends FrameLayout)

Used to scroll data it contains. To make a view scrollable, put it inside the ScrollView view group.

Note: Scollview accepts only on child. Therefore, wrap ScrollView arround a layout element that can hold more than one element.

Note: Not good for large amount of data as it load it view in memory.

For horizontal scrollview, use `HorizontalScrollView` element instead.

## Activities and Intents

### Activity

It's an application component. It represent a window/an hierarchy of views.

Note: An activity is a class with a UI... Java + XML.

--- What does activity ?

* Represent activity, such as ordering grocerie, sending email, or getting directions.
* Handles user interaction such as button click, text entry or login verification.
* We can start other activity at the same time
* Activities has lifecycles - Created, Started, Runs, Paused, Resumed, Stopped and destroyed.

--- How to implements activities

* Define XML layout

```xml
<?xml version="1.0" encoding="utf8" ?>
<RelativeLayout ... />

<TextView ... />
</RelativeLayout>
```

* Define a Java activity class (extends AppCompactActivity)
* Connect activity to the layout [onCreate()]

```java
// Uses AppCompactActivity, performs backward compatibilities
public class MyActivity extends AppCompactActivity {

    @Override
    public void onCreate(Bundle instance) {

        super.onCreate(instance);
        // 
        setContentView(R.layout.<RESOURCE_LAYOUT>);
    }
}
```

* Declare the activity in Android Manifest (Most important)

```xml
<!-- AndroidManifest -->

<!-- Activity to load when application is launch must include intent to start from launcher -->
<!-- There can be only one launcher intent per application -->
<activity android:name=".MainActivity">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <action android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
<!-- Custom activities -->
<activity android:name=".MyActivity">
</activity>
```

Note: They are managed by the Android Runtime (ART)

### Intents

It's a description of an operation to be performed.

It's a class object used to request action from another app component, except for content providers (Data handlers), via the Android System.

We are allow to invoke activity, Services, and Broadcast receivers using intent.

--- What can intent do ?

* Start activities
    Button click, start a new activity that allows to pick photos.

* Start Services
    Initiate a file download in the background

* Deliver broadcasts
    The system informs everybody that the phone is now charging.

--- Explicit & Implicit intents

* Explicit intent (The source and the destination is known)
    -- Start a specific activity

        - Request tea with milk by Nikita
        - Main activity start the ViewShoppingCart activity

```java
// Create the intent
// Intent intent = new Intent(<SOURCE_ACTIVITY>, <DESTINATION_ACTIVITY>)
Intent intent =  new Intent(this, MyActivity::class);

// Starting the intent
startActivity(intent);
```

* Implicit intents (Request system to open another app activity[`Intent resolution`])
    -- Ask system to find an activity that can handle the request

        - Find an open store that sells green tea

        - Clicking share opens a chooser with list of apps

```java
// Create the implicit intent
// Intent intent = new Intent(<ACTION>, <DATA>)
// Show web page
// Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://..."))
// Dial phone number
// Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:<PHONE_NUMBER>"))
// tel = telephone handler
// geo = geo points handlers
// etc...
Intent intent =  new Intent(action, uri);

// Starting the intent
startActivity(intent);
```

### Sending and Receiving Data

* Data - One piece of information whose data location can be represendted by an URI

```java
// Sending data to the other activity using data
intent.setData(
    Uri.parse("https://...")
);

// Passing file as data URI
intent.setData(
    Uri.fromFile(new File('/sdcard/sample.jpg' ))
);

// Getting data from activity
Uri location = intent.getData();

// Get extras
int level = intent.getIntExtra("level", 0);

// Get bundle
Bundle bundle =  intent.getExtras();
```

* Extras - One or More pieces of information as a collection of key-value pairs in a `Bundle`.

```java
// Sending extras
// intent.putExtra(String name, int value);
// intent.putExtra(String name, String[] value);
// intent.putExtras(Bundle bundle);
```

Note:

    Bundle is an android class used to transfert or save data dynamically. When the application stopped, the Bundle data memory is cleaned.

--- Activity result

1) Use `startActivityForResult(<INTENT>, <REQUEST_CODE>)` to start an activity that will return a result.
Note: REQUEST_CODE is an integer value used to identify the activity that returned.

2) In the other activity, use `putExtra()` to put data in the intent.

    Use Activity.RESULT_CANCELED, Activity.RESULT_OK and call finish() to notify the source activity

3) Implement `onActivityResult(int requestCode, int resultCode, Intent data` ) on the source activity

```java
public void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);

    if (requestCode === <DEFINED_REQUEST_CODE>) {
        if (resultCode == RESULT_OK) {
            // Do something with the extras values
            String reply = data.getStringExtra(SecondActivity.EXTRA_REPLY);
        }
    }
}
```

Note: To get the intent from the source activity in the destination activity, use `getIntent(): Intent`

### Activity States

* Created([`ngOnInit`]) - onCreate(Bundle instance) - Static initialization
* Started ([`ngAfterViewInit`]) - onStart() - Activity screen becomes visble
* onRestart([`like ngOnChanges`]) - Call when activity was stopped [calls `onStart()`]
    -- Resume (visible) - Start interacting with User - onResume()
    -- onPause() - About to resume previous activity `Best state to cleanup data, stop animation, or cleanup resources that may consume memory`

* onStop() - No longuer visible but exists an all state info is preserved [May call `onRestart()` if the OS did not claim memory before user launch the app again]
* onDestroy() - Final when OS is claiming memory holds by the activity

Note: App is `destroyed` when `screen orientation changes` .

Use `onPause()` and `onStop` to save data or state.

--- Saving state

Implements `onSaveInstanceState()` of the activity to save your state, cause Android runtime calls it when there is a possibility of the app being destroyed.

```java
@Override
public void onSaveInstanceState(Bundle state) {
    super.onSaveInstanceState(state);

    state.putString('STR_VAL', '<AVLUE>')
}

// On Activity started
public void onCreate(Bundle state) {
    // ...
    if (state !== null) {
        // Get the value from state
        String value = state.getString('');
    }
}

// On restore instance state
public void onRestoreInstanceState(Bundle state) {
    // ...
    if (state !== null) {
        // Get the value from state
        String value = state.getString('');
    }
}
```

### Contents : Implicit intents

Note:

```java
// Check if a particular application can handle an intent before launching it activity
if (intent.resolveActivity(getPackageManager()) != null) {
    startActivity(intent);
}
```

* Category

They are additional information about the kind of component to handle intent

> Intent. CATEGORY_OPENABLE - Allow URIs files that are openable
> Intent. CATEGORY_BROWSABLE - Allow activities that can start a web browser to display data referenced by the URI
> Intent. CATEGORY_LAUNCHER

```java
// Create the intent
Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);

// Setting the type
intent.setType("application/pdf") // Mime type
intent.setCategory(Intent.CATEGORY_OPENABLE)
```

* Register application as Intentable

1) Declare one or more intent filters for the activity in the Android Manifest file

2) Filter announces activity's ability to accept implicit intents
3) Filter puts conditions on the intents that the activity accepts

```xml
<activity android:name="ShareActivity">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <!-- Filters on Data URI's -->
        <!-- Limit the mime type accepted-->
        <data android:mimeType="text/plain" />
        <!-- Requires URI of https protocol -->
        <data android:scheme="https" />
        <!-- Accepts only request from specified host -->
        <data android:host="developer.android.com" />
    </intent-filter>
    <intent-filter>
        <!-- ... -->
    </intent-filter>
</activity>
```

### Debugging

### Android Support Libraries

* What are Android Support Libraries ?

They are more than 25 libraries in the Android SDK that provide features not built into the Android Framework

* Features
    -- Backward compatibility
    -- Additional Layout and UI comoonent, such as RecyclerView
    -- Different form factors such as TV, Wearables
    -- Provide MUI
    -- etc...

* Recommended

-- v4 Support (compact, core-utils, core-ui, etc...)
    --- Large set of APIs
    --- App Component, UI Features
    --- Data Handling
    --- Network connectivity
    --- Programming Utilities

-- v7 Supports
    --- TV-Specific components [MediaRouter]
    --- Google Cast Support
    --- Color Palette
    --- Preferences
    --- UI Component (Appcompat[compatibility wrappers], CardView, GridLayout, RecyclerView)

Must include in build.gradle:

> com.adroid.support:appcompat-v4:24.2.1 to make AppCompatActivity parent of all activities
