# First steps in Android development

## Project Strutures

-- app
   |

    -- manifest : Contains all the manifests configurations
    -- java : The java source code
    -- res : Resources values like colors, template strings, images, etc...
       |
        -- layout : Application UI in XML
        -- values: Resources values
          |
           -- colors: Contains colors values
           -- strings.xml: List of template strings
           -- Themes : Adnroid themes

## Variables

Loading template variables from configure values require:

> @color/<VARIABLE> - for loading predefined colors
> @string/<STRING_VARIABLE> - for loading string values

## UI elements

### View constraints

This constraints defines the position of the element they are used on. They belongs to the `app` namespace and allow to position element based on the position of other elements or their parent.

Note: To reference an element on the view use the syntax: `@+id/<IDVALUE>`

```xml
<Button
    // ... other attributes definitions
    app:layout_constraintBottom_toBottomOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toBottomOf="@+id/textview_first" />
```

Properties:

* layout_constraintVertical_bias - Bias the position of a view element upward or downward. `Range (0 - 1)`
* layout_constraintHorizontal_bias - Perform bias operation horizontally. `Range (0 - 1)`

### Android namespace

Properties like `id` , `background` , `textColor` , `text` , `textSize` , etc... are from the android namespace. In order to specify them as attribute prefix them with `android:` keyword.

Example:

```xml
<TextView
    android:id="@+id/textview_first"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:background="@color/colorPrimaryDark"
    android:text="@string/hello_first_fragment"
    android:textSize="72sp"
    android:fontFamily="sans-serif"
    android:textColor="@color/white" />
```

Properties of the android namespace:

* textSize - Font size of the text in `dps`
* fontFamily -  For setting font family of the element
* layout_marginEnd - Gives the margin right of the element in `dps`
* layout_marginStart - Gives the margin left of the element in `dps`
* layout_marginStart - Gives the margin left of the element in `dps`
* layout_width - Gives the width of the elemens `dps` or use `wrap_content`
* layout_height - Gives the height of the elemens `dps` or use `wrap_content`

## View bindings

### Android Views LifeCycle

* onCreateView - Works like an ngOnInit call
* onViewCreated -  Handle code after view is created like AfterViewInit
* onDestroyView -  When the view is destructed

### Selecting elements on the view

We can select element on a fragment by calling `findViewById(R.id.<VIEWELEMENTID>)` method on the `View` object.

* In onCreateView

In the `onCreateView` , we make use of the inflater to build the view fragment and use that fragment to select the element.

```java
@Override
public View onCreateView(
        LayoutInflater inflater,
        ViewGroup container,
        Bundle savedInstanceState
) {

    binding = FragmentFirstBinding.inflate(inflater, container, false);
    // Get the view element from the inflater
    View layout = inflater.inflate(R.layout.fragment_first, container, false);
    countTextView = layout.findViewById(R.id.textview_first);
    return binding.getRoot();

}
```

* In other lifecycles

```java

class FragmentClass extends Fragment {

    // ... 

    // Handle the code when the view is created
    public void onViewCreated(@NonNull View view, Bundle instance) {
        super.onViewCreated(view, instance);

        // Binding click listener for toast_button
        // Select an element on the view by id 
        view.findViewById(R.id.element_id).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Make a toast object
                Toast toast = Toast.makeText(getActivity(), "Hello Toaster!", Toast.LENGTH_LONG);
                // Show the toast on the view
                toast.show();
            }
        });
    }
}
```

### Navigation

Navigation definitions can be configured in the `navgraph` resources values defintions, with the parameters to pass in.

The Java code for navigating from on fragment to another is performed as follow:

```java
// Handle navigation when random button is clicked
view.findViewById(R.id.random_button).setOnClickListener(new View.OnClickListener(){
    @Override
    public void onClick(View v) {
        int currentCount = Integer.parseInt(countTextView.getText().toString());
        FirstFragmentDirections.ActionFirstFragmentToSecondFragment action = FirstFragmentDirections.actionFirstFragmentToSecondFragment(currentCount);
        NavHostFragment.findNavController(FirstFragment.this).navigate(action);
    }
});
```