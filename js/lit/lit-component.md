# Lit-Element

A Lit component is a reusable piece of UI. You can think of a Lit component as a container that has some state and that displays a UI based on its state. It can also react to user input, fire events—anything you'd expect a UI component to do. And a Lit component is an HTML element, so it has all of the standard element APIs.

## APIs

### Components

A Lit component is simply a class extending `LitElement` base class.

```ts
@customElement('element-name')
export class ComponentName extends LitElement {
    /* ... */
}
```

**Note**
The `@customElement` is a typescipt decorator is shorthand for calling `customElements.define`

When using javascript:

```js
export class ComponentName extends LitElement {
    /* ... */
}
customElements.define('element-name', SimpleGreeting);
```

**Note** Inheritance Tree

`LitElement` -> `ReactiveElement` -> `HTMLElement`

#### Rendering

Add a template to your component to define what it should render.

**Note**
Templates can include expressions, which are placeholders for dynamic content.

Lit Templates are returned by functional interface `html`

```js
import {
    html
} from 'lit';

render() {
    return html`<p>Hello World!</p>`
}
```

**Note**
Typically, the component's render() method returns a single `TemplateResult` object (the same type returned by the html tag function). But it can returns anything that `lit` can render:

* Primitive values like string, number, or boolean.
* TemplateResult objects created by the html function.
* DOM Nodes.
* Arrays or iterables of any of the supported types.

##### Best Practices

* Avoid changing the component's state.
* Avoid producing any side effects.
* Use only the component's properties as input.
* Return the same result when given the same property values.

**Note** When templates render
A Lit component renders its template initially when it's added to the DOM on a page. After the initial render, any change to the component's `reactive properties` triggers an update cycle, re-rendering the component.

**Note** DOM encapsulation
Lit uses shadow DOM to encapsulate the DOM a component renders. Shadow DOM lets an element create its own, isolated DOM tree that's separate from the main document tree.

#### Reactive properties

Reactive properties are properties of a `lit` component class that can trigger the reactive update cycle when changed, re-rendering the component, and optionally be read or written to attributes.

**Note** Background implementation

* `Lit` creates a getter and setter under the wood for each key, declared as property `@property()` in ts or `get properties() { ... }` in JS, that calls the DOM to re-render when their state changes.
* `Lit` by default observe changes on the attribute with same name as the property and update the property value when attribute changes
* `Lit` apply the properties options declared by the super classes, event though ihneritance is a bad habit.

##### Public props & Internal State

* Public properties

**Note**
Public reactive properties / public properties must be treated as `Inputs` , and must be immutable in regard to the component.

```ts
// Typescript
export class MyLitElement extends LitElement {
    // Restrict the property to be of type string
    @property({type: String})
    mode: string;

    // This property is not binded to any DOM element
    @property({attribute: false})
    data: {}
}

// Javascript

export class MyLitElement extends LitElement {
    static get properties() {
        return {
            mode: { type : String },
            data: { attribute: false }
        }
    }
}
```

* Internal State

Internal state / internal reactive state  refers to reactive properties that aren't part of the component's API. They are kind of private state of the component

```ts
export class CounterComponent extends LitElement {
    @state()
    private counter: number = 0;
}
```

**Note**
In JavaScript you must not use class fields when declaring reactive properties.

* Property options

> `attribute:boolean|string` -> Set custom attribute name if string is provided or disable attribute binding when value is false.

> `converter:Type|{ fromAttribute: (value, type) => {...}, toAttribute: (value: type) => {...} }` -> For converting value from a given type to a given type

> `hasChanged:(prev, current) => boolean` -> To determine if the property has changed.

> `reflect:boolean` -> Whether there is two way communication between property and attributes

> `state:boolean` -> If true makes the property as internal state that can be updated.

**Note**
Users should not access properties marked `state:true` from outside the component.

> `type:Type` -> When converting string values from template, default parsers are used to transform attribute values to property's specified type.

* Internal Reactive state options

> `hasChanged:(prev, current) => boolean` -> To determine if the property has changed.

#### Styles

Your component's template is rendered to its shadow root. The styles you add to your component are automatically scoped to the shadow root and only affect elements in the component's shadow root.

**Note** Component syles
`styles` property set the component shadow styles. Defining styles this way results in the most optimal performance.

```ts
export class MyElement extends LitElement {

    static readonly styles = css `
        p {
            color: green
        }
    `

    // or 
    static readonly styles = [
        css `
            p {
                color: green
            }
        `,
        // other styles
    ]
}

```

**Note** Application vulnerability & Security concerns
To prevent Lit components from evaluating potentially malicious code, the css tag only allows nested expressions that are themselves css tagged strings or numbers.

```js
const mainColor = css`red`;
...
static styles = css`
  div { color: ${mainColor} }
`;
```

> unsafeCSS() -> This function bypass security rules integrated in Lit library for handling styles, to inject `unsanitized` styles.

* Shadow dom styling (Shadow DOM pseudo classes)

> :host[(selector)] - Select the component itself / select an internal element of the component

> ::slotted(selector) - Match child components that are included via `<slot>` tag. Using `*` will apply the style to all child components.

* Dynamic classes and styles

Similar to Angular rendering engines `ngClass` & `ngStyle` attributes, lit provides a `classMap()` and `styleMap()` attributes to binding classes to template elements.

```ts
export class MyElement extends LitElement {
    @property()
    classes = { className: true, otherClassName: true};

    @property()
    styles: {color: 'lightgreen' };

    render() {
        return html`
            <div class=${classMap(this.classes)} style=${styleMap(this.styles)}> ... </div>
        `
    }
}
```

* Theming

By using CSS inheritance and CSS variables and custom properties together, it's easy to create themable elements. By applying css selectors to customize CSS custom properties, tree-based and per-instance theming is straightforward to apply.

#### Component LifeCycle

Lit components use the standard custom element lifecycle methods. In addition Lit introduces a reactive update cycle that renders changes to DOM when reactive properties change.

* connectedCallback()
Invoked when a component is added to the document's DOM.

**Note**
In such life cycle state, developpers are advise to add `event` listeners, etc...

* disconnectedCallback()
Invoked when a component is removed from the document's DOM. Developpers are advised to cleanup resource aquired in `connectedCallback` hook.

* attributeChangedCallback()
Invoked when one of the element’s observedAttributes changes. Lit uses this callback to sync changes in attributes to reactive properties.

-- Lit element Reactive Hooks
The reactive update cycle is triggered when a reactive property changes or when the requestUpdate() method is explicitly called

**Note**
Lit performs updates asynchronously so property changes are batched.

**Note** `changedProperties:PropertyValues<this>`

Many reactive update methods receive a Map of changed properties having type `PropertyValues<this>` . The Map keys are the property names and its values are the previous property values. You can always find the current property values using this.property or this[property].

> `shouldUpdate(properties: PropertyValues<this>): boolean` -> Called to determine whether an update cycle is required. If return value is false, update cycle stops. It returns `true` by default.

```ts
shouldUpdate(changedProperties: Map<string, any>) {
  // Only update element if prop1 changed.
  return changedProperties.has('prop1'); 
}
```

> `willUpdate(properties: PropertyValues<this>)` -> Called before update() to compute values needed during the update.

```ts
export class MyElement extends LitElement {
    willUpdate(changedProperties: PropertyValues<this>) {
        // only need to check changed properties for an expensive computation.
        if (changedProperties.has('firstName') || changedProperties.has('lastName')) {
            this.sha = computeSHA(`${this.firstName} ${this.lastName}`);
        }
    }
}
```

> `update(properties: PropertyValues<this>)` -> Called to update the component's DOM. Internally invoked by `Lit` to re-render the DOM template. If overriden, must call `super.update()` else the DOM is not re-rendered.

> `render()` -> Called by update() and should be implemented to return a renderable result (such as a TemplateResult) used to render the component's DOM.

> `firstUpdated(properties: PropertyValues<this>)` -> Called after the component's DOM has been updated the first time, immediately before updated() is called.

**Note**
Implement `firstUpdated(properties: PropertyValues<this>)` to perform `one-time` work after the component's DOM has been created. Some examples might include focusing a particular rendered element or adding a ResizeObserver or IntersectionObserver to an element.

> `updated(properties: PropertyValues<this>)` -> Called whenever the component’s update finishes and the element's DOM has been updated and rendered.

**Note**
Implement updated() to perform tasks that use element DOM after an update.

-- External Lifecycle hooks: Controllers & Decoratoes

> `addInitializer()` -> allows code that has access to a Lit class definition to run code when instances of the class are constructed.

```ts
// A TypeScript decorator that add a hook when the lit component instance is created
const init = (proto: ReactiveElement, key: string) => {
  const ctor = proto.constructor as typeof ReactiveElement;

  ctor.addInitializer((instance: ReactiveElement) => {
    // This is run during construction of the element
    new MyController(instance);
  });
};
```

> `addController` -> adds a reactive controller to a Lit component so that the component invokes the controller's lifecycle callbacks.

> `removeController()` -> removes a reactive controller so it no longer receives lifecycle callbacks from this component.

#### Shadown DOM

Lit components use shadow DOM to encapsulate their DOM. Shadow DOM provides a way to add a separate isolated and encapsulated DOM tree to an element.

> @query(selector)

Modifies a class property, turning it into a getter that returns a node from the render root. The optional second argument when true performs the DOM query only once and caches the result.

> @queryAll(selector)

Identical to `query` except that it returns all matching nodes, instead of a single node. It's the equivalent of calling `querySelectorAll` .

```ts
export class MyElement extends LitElement {
    @queryAll('button')
    buttons!: NodeListOf<HTMLButtonElement>;

}
```

> @queryAsync()

Similar to `@query` , except that instead of returning a node directly, it returns a `Promise` that resolves to that node after any pending element render is completed.
It's similar to `@ViewChild({static: false})`

* Slot
To render an element's children, create a `<slot>` for them in the element's template. It's similar `<ng-content>` in Angular.

-- Named slot
They are used to assign a child to a specific slot, ensure that the child's slot attribute matches the slot's `name` attribute.

```ts
@customElement('my-element')
export class MyElement extends LitElement {
    render() {
        return `
            <slot name="slot-name"></slot>
        `
    }
}

// HTML
export const App = () => {
    return html`
        <my-element>
            <p slot="slot-name"></p>
        </my-element>
    `
}
```

-- Slot fallback content

```ts
export class MyElement extends LitElement {

    static readonly get defaultTemplate() {
        return html`
            <p> Default Slot Content </p>
        `
    }

    render() {
        return html`
            <slot>
                ${defaultTemplate}
            </slot>
        `
    }
}
```

* Accessing Slotted Children
To access children assigned to slots in your shadow root, you can use the standard `slot.assignedNodes` or `slot.assignedElements` methods with the `slotchange` event.

```ts
get _slottedChildren() {
  const slot = this.shadowRoot.querySelector('slot');
  return slot.assignedElements({flatten: true});
}
```

* @slotchange

Event listener when the assigned slot nodes changes.

```ts
export class MyElement extends LitElement {
    handleSlotchange(e) {
        // Get the list of assigned nodes
        const nodes = e.target.assignedNodes({flatten: true});
    }

    render() {
        return html`<slot @slotchange=${this.handleSlotchange}></slot>`;
    }
}
```

* Slot decorators

convert a class property into a getter that returns the result of calling `slot.assignedElements` or `slot.assignedNodes` respectively on a given slot in the component's shadow tree. Use these to query the elements or nodes assigned to a given slot.

> `@queryAssignedElements() -> slot.assignedElements`

> `@queryAssignedNodes -> slot.assignedNodes`

-- Supported properties

--- `flatten` -> Boolean specifying whether to flatten the assigned nodes by replacing any child `<slot>` elements with their assigned nodes.
--- `name` -> Slot name specifying the slot to query. Leave undefined to select the default slot.
--- `selector` (queryAssignedElements only) -> If specified, only return assigned elements that match this CSS selector.

```ts
export class MyElement extends LitElement {
    @queryAssignedElements({slot: 'list', selector: '.item'})
    _listItems!: Array<HTMLElement>;

    @queryAssignedNodes({slot: 'header', flatten: true})
    _headerNodes!: Array<Node>;
}
```

* Customizing render root (To be reviewed)

Each Lit component has a render root—a DOM node that serves as a container for its internal DOM.

#### Component Events

Events are the standard way that elements communicate changes. These changes typically occur due to user interaction. For example, a button dispatches a click event when a user clicks on it; an input dispatches a change event when the user enters a value in it.

##### Listening to Events

In addition to the standard addEventListener API, Lit introduces a declarative way to add event listeners.

> @event

You can use @ expressions in your template to add event listeners to elements in your component's template.

**Note**
Event listeners added using the declarative @ syntax in the template are automatically bound to the component.

```ts
class MyElement extends LitElement {

    handleButtonClick(e: Event) {
        // Provide code that handles click events
    }

    render() {
        return html `
            <p><button @click="${this.handleButtonClick}"></button></p>
        `
    }
}
```

**Note** Event Listener Options
If you need to customize the event options used for a declarative event listener (like `passive` or `capture` ), you can specify these on the listener using the `@eventOptions` decorator.

```ts
class MyElement extends LitElement {

    @eventOption({passive: true})
    private _handleClickEvent(e: Event) {
        // ...
    }
}
```

**Note**
If your component adds an event listener to anything except itself or its templated DOM – for example, to `Window` , `Document` , or some element in the main DOM – you should add the listener in `connectedCallback` and remove it in `disconnectedCallback` .

##### Event Delegation

Using event delegation can reduce the number of event listeners used and therefore improve performance.

* Asynchronously adding Event handlers

To add an event listener after rendering, use the `firstUpdated` method. This is a Lit lifecycle callback which runs after the component `first updates` and `renders` its templated DOM.

```ts
class MyElement extends LitElement {

    // This method is similar to afterViewContentInit in Angular
    async firstUpdated() {
        // Give the browser a chance to paint
        await new Promise((r) => setTimeout(r, 0));
        this.addEventListener('click', this._handleClick);
    }
}
```

* Dispatching Events
All DOM nodes can dispatch events using the dispatchEvent method. First, create an event instance, specifying the event type and options.

```ts
const event = new Event('my-event', {bubbles: true, composed: true});
myElement.dispatchEvent(event);
```

> `bubbles` -> The bubbles option allows the event to flow up the DOM tree to ancestors of the dispatching element.
> `composed` -> option is useful to set to allow the event to be dispatched above the shadow DOM tree in which the element exists.

```ts
class MyElement extends LitElement {

    render() {
        return `
            <button @click=${this._handleAuth}></button>
        `
    }

    private _handleAuth() {
        // ...

        // Uncomment the code to dispatch event
        // only after the component updates
        // await this.updateComplete;
        this.dispatchEvent(new CustomEvent('loggin', {detail: {/* ... */, bubbles: true, composed: true}}));
    }
}
```
