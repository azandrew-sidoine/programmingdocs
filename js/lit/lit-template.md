# Lit Templating

## Lit Template Expression

* Template composition

```ts
const partial = html`
    <nav></nav>
`;

const view = html`
    ${partial}
    <main>...</main>
`
```

* DOM nodes
Any DOM node can be passed to a child expression. Typically DOM nodes should be rendered by specifying a template using html, but a DOM node can be directly rendered like this when needed.

```ts
const domElement = document.createElemet('div');

const view = html`
    ${domElement}
    <main>...</main>
`
```

* Iterables

You can use this feature along with standard JavaScript like the `Array map` method to create repeating templates and lists.

### Attribute binding

* Default attributes

```js
const view = html`
    <div attribute=${expression}>...</div>
`
```

**Note**
`expresion` should return a string value.
`attribute` can be any HTML attribute.

* Boolean attributes `?attribute`

To set a boolean attribute, use the ? prefix with the attribute name. The attribute is added if the expression evaluates to a truthy value, removed if it evaluates to a falsy value

```js
const view = html`<div ?hidden=${!this.showAdditional}>This text may be hidden.</div>`;
```

* removing attributes -> `attribute=${strinvalue ?? nothing}`

Lit's nothing sentinel value addresses this by removing the attribute when any expression in the attribute value evaluates to `nothing` .

### Property expression `.property`

It's like a property binding in Angular framework. You can set a JavaScript property on an element using the . prefix and the property name.

```js
const view = html`
    <input .value=${this.itemCount}/> 
`
```

### Event Listeners `@event=${listener}`

Templates can also include declarative event listeners. Use the prefix `@` followed by the event name. The expression should evaluate to an event listener.

```js
const view = html`
    <button @click=${this.clickHandler}>Click Me!</button>
`
```

**Note**
The event listener can be either a plain function, or an object with a `handleEvent` method — the same as the `listener` argument to the standard `addEventListener` method.

### Reference directive

`ref` is a built-in directive that provides a reference to the rendered element. It works like `@ViewChild()` angular decorator or `useRef()` in React.

```js
const view = html`
    <button ${ref(this.buttonRef )} ></button>
`
```

### Static Expressions

Static expressions return special values that are interpolated into the template before the template is processed as HTML by Lit.

To use static expressions, you must import a special version of the html or svg template tags from Lit's `static-html` module:

```js
import {
    html,
    literal
} from 'lit/static-html.js';
```

**Note**
The static-html module contains html and svg tag functions which support static expressions and should be used instead of the standard versions provided in the lit module. Use the literal tag function to create static expressions.

## Conditionals

Since Lit leverages normal Javascript expressions, you can use standard Javascript control flow constructs like conditional operators, function calls, and if or switch statements to render conditional content.

```js
render() {
    return this.userName ?
        html`Welcome ${this.userName}` :
        html`Please log in <button>Login</button>`;
}
```

### Conditional with statements

You can express conditional logic with if statements outside of a template to compute values to use inside of the template

```js
getUserMessage() {
    if (this.userName) {
        return html`Welcome ${this.userName}`;
    } else {
        return html`Please log in <button>Login</button>`;
    }
}
render() {
    return html`<p>${this.getUserMessage()}</p>`;
}
```

### Template caching

In most cases, JavaScript conditionals are all you need for conditional templates. However, if you're switching between large, complicated templates, you might want to save the cost of recreating DOM on each switch.

```js
render() {
    return html`${cache(this.userName ?
    html`Welcome ${this.userName}`:
    html`Please log in <button>Login</button>`)
  }`;
}
```

### Rendering nothing

Sometimes, you may want to render nothing in one branch of a conditional operator. This is commonly needed for child expressions and also sometimes needed in attribute expressions.

```js
render() {
    return html`<user-name>${this.userName ?? nothing}</user-name>`;
}
```

## List rendering

**Note**
Prefer use of `repeat` as it's optimize directive for rendering lists.

You can use standard JavaScript constructs to create repeating templates.

Lit also provides a repeat directive to build certain kinds of dynamic lists more efficiently.

### Rendering Arrays

When an expression in the child position in returns an array or iterable, Lit renders all of the items in the array:

```js
@property() colors = ['red', 'green', 'blue'];

render() {
    return html`<p>Colors: ${this.colors}</p>`;
} // returns Colors: redgreenblue
```

### Using map

To render lists, you can use map to transform a list of data into a list of templates:

```js
@property() colors = ['red', 'green', 'blue'];

render() {
    return html`
    <ul>
      ${this.colors.map((color) =>
        html`<li style="color: ${color}">${color}</li>`
      )}
    </ul>
  `;
}
```

### Repeat directive

It provides a virtual scroll implementation arround list elements.

> repeat(items, keyFn, templateFn)

```js
import {
    repeat
} from 'lit/directives/repeat.js';
/* playground-fold */

@customElement('my-element')
class MyElement extends LitElement {

    private sort = 1;

    @property() employees = [{
            id: 0,
            givenName: 'Fred',
            familyName: 'Flintstone'
        },
        {
            id: 1,
            givenName: 'George',
            familyName: 'Jetson'
        },
        {
            id: 2,
            givenName: 'Barney',
            familyName: 'Rubble'
        },
        {
            id: 3,
            givenName: 'Cosmo',
            familyName: 'Spacely'
        }
    ];
    /* playground-fold-end */

    render() {
        return html`
    <ul>
      ${repeat(this.employees, (employee) => employee.id, (employee, index) => html`
        <li>${index}: ${employee.familyName}, ${employee.givenName}</li>
      `)}
    </ul>
    <button @click=${this.toggleSort}>Toggle sort</button>
  `;
    }
```

## Built-in Directives

Directives are functions that can extend Lit by customizing the way an expression renders. Lit includes a number of built-in directives to help with a variety of rendering needs.

[https://lit.dev/docs/templates/directives/]

> `when<T, F>(condition: False, trueCase: () => T, falseCase: () => F)`

When condition is true, returns the result of calling trueCase(), else returns the result of calling falseCase() if falseCase is defined.

```js
class MyElement extends LitElement {
    render() {
        return html`
      ${when(this.user, () => html`User: ${this.user.username}`, () => html`Sign In...`)}
    `;
    }
}
```

> `choose<T,V>(value: T, cases: Array<[T, () => V]>), defaultCase?: () => V)`

```js
class MyElement extends LitElement {
    render() {
        return html`
      ${choose(this.section, [
        ['home', () => html`<h1>Home</h1>`],
        ['about', () => html`<h1>About</h1>`]
      ],
      () => html`<h1>Error</h1>`)}
    `;
    }
}
```

> `map<T>(items: Iterable<T>|undefined, f: (value: T, index: number) => unknown )`

map() is a simple wrapper around a `for/of loop` that makes working with iterables in expressions a bit easier. `map()` always updates any DOM created in place - it does not do any diffing or DOM movement. It works like `Array.map()` .

```js
class MyElement extends LitElement {
    render() {
        return html`
      <ul>
        ${map(items, (i) => html`<li>${i}</li>`)}
      </ul>
    `;
    }
}
```

> `repeat(items: Iterable<T>, keyfn: KeyFn<T>, template: ItemTemplate<T>)`

> `repeat(items: Iterable<T>, template: ItemTemplate<T>)`

> `range(end)`

> `range(start, end: number[, step: number])`

Returns an iterable of integers from start to end (exclusive) incrementing by step.

> `ifDefined()`

Sets an attribute if the value is defined and removes the attribute if undefined.

```js
class MyElement extends LitElement {

    @property()
    filename: string | undefined = undefined;

    @property()
    size: string | undefined = undefined;

    render() {
        // src attribute not rendered if either size or filename are undefined
        return html`<img src="/images/${ifDefined(this.size)}/${ifDefined(this.filename)}">`;
    }
}
```

> `cache(value: TemplateResult|unknown)`

Caches rendered DOM when changing templates rather than discarding the DOM. You can use this directive to optimize rendering performance when frequently switching between large templates.

When the value passed to cache changes between one or more TemplateResults, the rendered DOM nodes for a given template are cached when they're not in use.
When the template changes, the directive caches the current DOM nodes before switching to the new value, and restores them from the cache when switching back to a previously-rendered value, rather than creating the DOM nodes anew.

```js
const detailView = (data) => html`<div>...</div>`;
const summaryView = (data) => html`<div>...</div>`;

@customElement('my-element')
class MyElement extends LitElement {

    @property()
    data = {
        showDetails: true,
        /*...*/
    };

    render() {
        return html`${cache(this.data.showDetails
      ? detailView(this.data)
      : summaryView(this.data)
    )}`;
    }
}
```

### Custom Directives

Directives are functions that can extend Lit by customizing how a template expression renders. Directives are useful and powerful because they can be stateful, access the DOM, be notified when templates are disconnected and reconnected, and independently update expressions outside of a render call.

Using a directive in a template is asimply as calling a function.

#### Function directives

It's a javascript function that returns a transformation result to render.

```js
export noVowels = (str) => str.replaceAll(/[aeiou]/ig, 'x')
```

#### Class based directives

Provides a complex function that function directives does not provides. Class based directives must implements `Directive` interface.

* Access the rendered DOM directly
* Persist states between renders
* Updated DOM synchronously outside of render calls
* Cleanup resources when the directive is disconnected

Example:

```js
import {
    directive,
    Directive
} from 'lit/directive.js';

class MyDirective extends Directive {

    // For imperative access to the DOM elements
    update() {
        // Note: Default implementation calls and return result of render()
    }

    // Must be declared by any directive
    // It works like Angular `transform` method for pipe
    render() {
        //... renders content 
    } // DirectiveResult|TemplateResult|Primitive|nothing
}

export const myDirective = directive(MyDirective)
```

**Note**
Directive function can be created from directive classes by passing them to the `directive()` factory functions.

#### Imperative DOM access

Imperative DOM manipulation `read/update` is done in the update method of the directive.

> `update(value: Part, arguments: Array<unknown>)`

A Part object with an API for directly managing the DOM associated with the expression.

-- Part
Each expression position has its own specific Part object:

* `Childpart` ->  for expressions in HTML child position.
* `AttributePart` -> for expressions in HTML attribute value position.
* `BooleanAttributePart` -> for expressions in a boolean attribute value (name prefixed with ?).
* `EventPart` -> for expressions in an event listener position (name prefixed with @).
* `PropertyPart` -> for expressions in property value position (name prefixed with .).
* `ElementPart` -> for expressions on the element tag.

```js
// Renders attribute names of parent element to textContent
class AttributeLogger extends Directive {
  attributeNames = '';
  update(part: ChildPart) {
    this.attributeNames = (part.parentNode as Element).getAttributeNames?.().join(' ');
    // Need to call render() method explicitly
    return this.render();
  }
  render() {
    return this.attributeNames;
  }
}
const attributeLogger = directive(AttributeLogger);

const template = html`<div a b>${attributeLogger()}</div>`;
```

The `render()` arguments are passed into `update()` as an array. You can pass the arguments to `render()` like this:


```js
class MyDirective extends Directive {
  update(part: Part, [fish, bananas]: DirectiveParameters<this>) {
    // ...
    return this.render(fish, bananas);
  }
  render(fish: number, bananas: number) { ... }
}
```

**Note**
While the `update()` callback is more powerful than the `render()` callback, there is an important distinction: When using the `@lit-labs/ssr` package for server-side rendering (SSR), only the `render()` method is called on the server. To be compatible with SSR, directives should return values from `render()` and only use `update()` for logic that requires access to the DOM.

#### Signaling no change

Sometimes a directive may have nothing new for Lit to render. You signal this by returning `noChange` from the `update()` or `render()` method. This is different from returning `undefined`, which causes `Lit` to clear the `Part` associated with the directive. Returning noChange leaves the previously rendered value in place.

```js
import {Directive} from 'lit/directive.js';
import {noChange} from 'lit';

class CalculateDiff extends Directive {
  a?: string;
  b?: string;
  render(a: string, b: string) {
    if (this.a !== a || this.b !== b) {
      this.a = a;
      this.b = b;
      // Expensive & fancy text diffing algorithm
      return calculateDiff(a, b);
    }
    return noChange;
  }
}
```

#### Async directive

The previous example directives are synchronous: they return values synchronously from their `render()/update()` lifecycle callbacks, so their results are written to the DOM during the component's `update()` callback.

To update a directive's result asynchronously, a directive needs to extend the `AsyncDirective` base class, which provides a `setValue()` API. `setValue()` allows a directive to "push" a new value into its template expression, outside of the template's normal `update/render` cycle.

```js
class ResolvePromise extends AsyncDirective {
  render(promise: Promise<unknown>) {
    Promise.resolve(promise).then((resolvedValue) => {
      // Rendered asynchronously:
      this.setValue(resolvedValue);
    });
    // Rendered synchronously:
    // Returns the default placeholder when the promise does not
    // resolve
    return `Waiting for promise to resolve`;
  }
}
export const resolvePromise = directive(ResolvePromise);
```


```js
class ObserveDirective extends AsyncDirective {
  observable: Observable<unknown> | undefined;
  unsubscribe: (() => void) | undefined;
  // When the observable changes, unsubscribe to the old one and
  // subscribe to the new one
  render(observable: Observable<unknown>) {
    if (this.observable !== observable) {
      this.unsubscribe?.();
      this.observable = observable
      if (this.isConnected)  {
        this.subscribe(observable);
      }
    }
    return noChange;
  }
  // Subscribes to the observable, calling the directive's asynchronous
  // setValue API each time the value changes
  subscribe(observable: Observable<unknown>) {
    this.unsubscribe = observable.subscribe((v: unknown) => {
      this.setValue(v);
    });
  }
  // When the directive is disconnected from the DOM, unsubscribe to ensure
  // the directive instance can be garbage collected
  disconnected() {
    this.unsubscribe!();
  }
  // If the subtree the directive is in was disconnected and subsequently
  // re-connected, re-subscribe to make the directive operable again
  reconnected() {
    this.subscribe(this.observable!);
  }
}
export const observe = directive(ObserveDirective);
```

**Note** AsyncDirective API

> `disconnected()`: Called when a directive is no longer in use. Directive instances are disconnected in three cases:

When the DOM tree the directive is contained in is removed from the DOM
When the directive's host element is disconnected
When the expression that produced the directive no longer resolves to the same directive.
After a directive receives a disconnected callback, it should release all resources it may have subscribed to during update or render to prevent memory leaks.

> `reconnected()`: Called when a previously disconnected directive is being returned to use. Because DOM subtrees can be temporarily disconnected and then reconnected again later, a disconnected directive may need to react to being reconnected. Examples of this include when DOM is removed and cached for later use, or when a host element is moved causing a disconnection and reconnection. The `reconnected()` callback should always be implemented alongside `disconnected()`, in order to restore a disconnected directive back to its working state.

> `isConnected`: Reflects the current connection state of the directive.
