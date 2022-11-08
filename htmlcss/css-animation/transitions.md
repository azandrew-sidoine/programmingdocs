# CSS Transitions

## Definition

CSS transition makes it possible to transition DOM element from 1 state to another.

```css
selector {
    transition: [property] [duration] [timing] [delay]
}
```

- Property: The CSS property or CSS properties that will be candidate to transition functions. Ex: transform, width, etc...
- duration: Transition duration
- Timing: Transition timing function to be used. Defines the speed at which the transition is played by the browser. Ex. ease, ease-in, ease-out, linear, ease-in-out, etc... Default: ease
- delay: Delay before the transition start to play.

## CSS Transform (2D transform)

Now that we reviewed how to make smooth and gradual transitions, let’s look at CSS transforms - how to make an element change from one state to another. With the CSS transform property you can rotate, move, skew, and scale elements.

**Note**
Transforms are triggered when an element changes states, such as on mouse-hover or mouse-click.

- scale `scale(x, y), scaleX(n), scaleY(n)`

The scale value allows you to increase or decrease the size of an element.

- rotate `rotate(angle)`

With the rotate value, the element rotates clockwise or counterclockwise by a specified number of degrees.

**Note**
Angle value are in `degree` when suffixed with `deg` keyword, else it's computed in gradient.

- Translate `translate(x, y), translateX(n), translateY()`

The translate value moves an element left/right and up/down. The movement is based on the parameters given for the X (horizontal) Y (vertical) axes.
A positive X value moves the element to the right, while a negative X moves the element to the left. A positive Y value moves the element downwards and a negative Y value, upwards.

- transform-origin
The transform-origin property is separate from the transform property but works in tandem with it. It allows you to specify the location origin of the transform. By default, the origin is in the center of the element.

- perspective

The `perspective()` CSS function defines a transformation that sets the distance between the user and the z=0 plane, the perspective from which the viewer would be if the 2-dimensional interface were 3-dimensional.
The `perspective()` transform function is part of the transform value applied on the element being transformed. This differs from the `perspective` and `perspective-origin` properties which are attached to the parent of a child transformed in 3-dimensional space.
