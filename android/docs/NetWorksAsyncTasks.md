# Network & Async Tasks

- Working with strings.xml
In Java, you can get a String saved in res -> values -> strings.xml by calling the getString method. If you’re in an Activity, you can just call getString, and pass in the String resource ID. The String resource ID can be found in the strings.xml XML. For example, let's look at Sunshine's strings.xml file:

```xml
<string name="today">Today</string>

<!-- For labelling tomorrow's forecast [CHAR LIMIT=15] -->
<string name="tomorrow">Tomorrow</string>

<!-- Date format [CHAR LIMIT=NONE] -->
<string name="format_full_friendly_date">
    <xliff:g id="month">%1$s</xliff:g>, <xliff:g id="day">%2$s</xliff:g>
</string>

```

```java
// In Java activity file
String myString = getString(R.string.today);
```

## Android Menu

1) Create a menu using the editor wizard by right clicking the res folder and add a resource of type menu

-- Example

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    <item
        android:id="@+id/menu_search"
        android:title="@string/search"
        app:showAsAction="ifRoom" />
</menu>
```

2) Next in the activity override the `onCreateOptionsMenu` to handle menu creation action and `onOptionsItemSelected` to handle menu items click action.

```java
public class MenuActivity extends AppCompatActivity {

    // ...
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
}

```

### Showing a Toast

```java
Toast toast = Toast.makeText(Context, "String", duration);
toast.show();
```

## Making HTTP Request

### Build URI

```java
// Returns an instance of URI
uri = Uri.parse(BASE_URL).buildUpon()
    .appendQueryParameter(NAME, VALUE)
    .appendQueryParameter(NAME, VALUE)

    // Use appendPath to append a path parameter
    .build();

// Passing the Android builded URI to Java URL
try {
    URL url = new URL(uri.toString());
} catch (MalformedURLException e) {
    Log.e(e.getMessage());
}
```

### Basic Http request

```java
HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
try {
    InputStream in = urlConnection.getInputStream();

    Scanner scanner = new Scanner(in);
    scanner.useDelimiter("\\A");

    boolean hasInput = scanner.hasNext();
    if (hasInput) {
        return scanner.next();
    } else {
        return null;
    }
} finally {
    urlConnection.disconnect();
}
```

### Permissions

Permissions required by the application must be declare in android manifest.

-- Example

```xml
<manifest 
    // ...
>
    //...
    <uses-permission android:name="android.permission.INTERNET" />
    //...
</manifest>
```

Note: Android Will throw an Exception when performing Async task on the Main OS thread `NetworkOnMainThreadException`;

The Main thread is responsible for UI, and UI Events... Therefore when performing async task, make an async call.

### Async Task

Allow to run a task in the background thread will providing the result to the UI Thread when done.

Note:
    AsyncTask is Generic class offering 3 methods that must be ovewriting when performing async action.

`doInBackground`, `onProgressUpdate`, `onPostExecute`, `onPreExecute` on UI thread.

`onPreExecute` -> `doInBackground` ->   `onPostExecute`

Note: in `doInBackground`, call to `publishProgress` notify UI thread of the progress of the async action.

### Read JSON String

```java
JSONObject contact = new JSONObject(string);

// Getting fields
JSONObject name = contact.getJSONOBject("name");

// Get String
String firstname = contact.getString("firstname")
```
