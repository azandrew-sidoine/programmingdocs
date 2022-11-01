# Lit Composition

Composition is a strategy for managing complexity and organizing code into reusable pieces. Lit provides a few options for composition and code reuse:

## Component Composition

### Good composition

- What makes a good component ?

  - It has it owns state
  - It has it own template
  - It's used in more than on plac, either in this component or in multiple component
  - It focus on doing one thing well
  - It has a well-defined API

- How data flows ?
  - Properties down `Ng Inputs`: Setting properties on a subcomponent is usually preferable to calling methods on the subcomponent
  - Event up `Ng Outputs`: In the web platform, firing events is the default method for elements to send information up the tree, often in response to user interactions

## Reactive Controllers (Lit v2)

Lit 2 introduces a new concept for code reuse and composition called reactive controllers.

**Note**
A reactive controller is an object that can hook into a component's reactive update cycle.

You can use controllers to implement features that require their own state and access to the component's lifecycle, such as:

- Handling global events like mouse events
- Managing asynchronous tasks like fetching data over the network
- Running annimations

**Note**
Reactive controllers allow you to build components by composing smaller pieces that aren't themselves components. They can be thought of as reusable, partial component definitions, with their own identity and state.

```js
import {ReactiveController, ReactiveControllerHost} from 'lit';

export class ClockController implements ReactiveController {
  host: ReactiveControllerHost;

  private _value = new Date();
  public get value() {
    return this._value;
  }
  timeout: number;
  private _timerID?: number;

  constructor(host: ReactiveControllerHost, timeout = 1000) {

    // Store the host component reference in order to interact with it later
    (this.host = host).addController(this);
    this.timeout = timeout;
  }

  // Register to receive host component connected lifecycle event
  hostConnected() {
    // Start a timer when the host is connected
    this._timerID = setInterval(() => {
      this._value = new Date();
      // Update the host with new value
      this.host.requestUpdate();
    }, this.timeout);
  }

  // Register to receive host component disconnect lifecycle event
  hostDisconnected() {
    // Clear the timer when the host is disconnected
    clearInterval(this._timerID);
    this._timerID = undefined;
  }

}

// Using the controller
export class MyElement extends LitElement {

    // Create a Lit Controller
    private controller =  new Controller(this, 100);

    // Use the controller in render
    render() {
        const formattedTime = timeFormat.format(this.clock.value);
        return html`Current Time: ${formattedTime}`
    }
}
```

### Reactive Controllers Life cycles

The reactive controller lifecycle, defined in the ReactiveController interface, is a subset of the reactive update cycle:

- hostConnected():
    called when the lit-element is connected, after creating `renderRoot` so the shadow root exists. Observers, event listeners, etc can be registered at this point.
- hostUpdate():
    called before host `update()` and `render()` methods. Useful for reading DOM before it's updated.

- hostUpdated():
    Called after updates and before host `updated()` method.

- hostDisconnected():
    called when the host disconnect. Useful for cleaning resource acquired in `hostConnected()` hooks.

### Reactive Controller Host API

- addController(controller: ReactiveController) -> Add a controller to the lit-element
- removeController(controller: ReactiveController) -> Removes controller from a lit-element
- requestUpdate() -> Manually request for lit-element update
- updateComplete: Promise<boolean> -> Hooks into updateComplete hook of the lit-element

### Controllers & Directives

Combining controllers with directives can be a very powerful technique, especially for directives that need to do work before or after rendering, like animation directives; or controllers that need references to specific elements in a template.

- Controller Directives
Reactive controllers do not need to be stored as instance fields on the host. Anything added to a host using `addController()` is a controller. In particular, a directive can also be a controller. This enables a directive to hook into the host lifecycle.

- Controllers that own directives

Directives do not need to be standalone functions, they can be methods on other objects as well, such as controllers. This can be useful in cases where a controller needs a specific reference to an element in a template.

**Note**
Reactive controllers are similar in many ways to class mixins. The main difference is that they have their own identity and don't add to the component's prototype, which helps contain their APIs and lets you use multiple controller instances per host component.

## Class Mixin

Class mixins are a pattern for sharing code between classes using standard JavaScript. As opposed to "has-a" composition patterns like reactive controllers, where a class can own a controller to add behavior, mixins implement "is-a" composition, where the mixin causes the class itself to be an instance of the behavior being shared.

```js
class ResizeDirective {
  /* ... */
}
const resizeDirective = directive(ResizeDirective);

export class ResizeController {
  /* ... */
  observe() {
    // Pass a reference to the controller so the directive can
    // notify the controller on size changes.
    return resizeDirective(this);
  }
}

// Usage
class MyElement extends LitElement {
  private _textSize = new ResizeController(this);

  render() {
    return html`
      <textarea ${this._textSize.observe()}></textarea>
      <p>The width is ${this._textSize.contentRect?.width}</p>
    `;
  }
}
```

**Note**
Mixins can be thought of as "subclass factories" that override the class they are applied to and return a subclass, extended with the behavior in the mixin. Because mixins are implemented using standard `JavaScript` class expressions, they can use all of the idioms available to subclassing, such as adding new `fields/methods`, overriding existing superclass methods, and using `super`.

```js
const mixin = (base) => class extends base {
    // Provides properties, methods and overriding
}

import { LitElement } from 'lit';

// Applying a mixing to LitElement component
class extends mixin(LitElement) {
    /* Class codes ... */
}
```

Example:

```js
const LoggingMixin = (superClass) =>
  class extends superClass {
    constructor() {
      super();
      console.log(`${this.localName} was created`);
    }
    connectedCallback() {
      super.connectedCallback();
      console.log(`${this.localName} was connected`);
    }
    updated(changedProperties) {
      super.updated?.(changedProperties);
      console.log(`${this.localName} was updated`);
    }
  };
```

**Note**
Mixins can also add reactive properties, styles, and API to the subclassed element.

```js
export const Highlightable =
  <T extends Constructor<LitElement>>(superClass: T) => {
    class HighlightableElement extends superClass {
      // Adds some styles...
      static styles = [
        (superClass as unknown as typeof LitElement).styles ?? [],
        css`.highlight { background: yellow; }`
      ];

      // ...a public `highlight` property/attribute...
      @property({type: Boolean}) highlight = false;

      // ...and a helper render method:
      renderHighlight(content: unknown) {
        return html`
          <div class=${classMap({highlight: this.highlight})}>
            ${content}
          </div>`;
        }
      }
      return HighlightableElement as Constructor<HighlightableInterface> & T;
    };
```

- Mixin in Typescript

You should constrain the superClass argument to the type of class you expect users to extend, if any.

```ts
import {LitElement} from 'lit';

type Constructor<T = {}> = new (...args: any[]) => T;

export const MyMixin = <T extends Constructor<LitElement>>(superClass: T) => {
  class MyMixinClass extends superClass {
    /* ... */
  };
  return MyMixinClass as as T;
}
```

**Warning**
In practice this means mixins in TypeScript need to declare a class and then return it, rather than return a class expression directly from the arrow function.

```ts
// This works
export const MyMixin = <T extends LitElementConstructor>(superClass: T) => {
  // ✅ Defining a class in a function body, and then returning it
  class MyMixinClass extends superClass {
    @property()
    mode = 'on';
    /* ... */
  }
  return MyMixinClass;
};

// This does not works
export const MyMixin = <T extends LitElementConstructor>(superClass: T) =>
  // ❌ Returning class expression direcly using arrow-function shorthand
  class extends superClass {
    @property()
    mode = 'on';
    /* ... */
  };
```
