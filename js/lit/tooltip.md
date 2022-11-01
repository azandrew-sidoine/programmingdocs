# Lit Element Tooltip example

```ts

import {html, css, LitElement, ElementPart, render} from 'lit';
import {customElement, property} from 'lit/decorators.js';
import {Directive, DirectiveParameters, directive} from 'lit/directive.js';
import {computePosition, autoPlacement, offset, shift} from '@floating-ui/dom';

const enterEvents = ['pointerenter', 'focus'];
const leaveEvents = ['pointerleave', 'blur', 'keydown', 'click'];

// Tooltip component
@customElement('simple-tooltip')
export class SimpleTooltip extends LitElement {

  // Lazy creation
  static lazy(target: Element, callback: (target: SimpleTooltip) => void) {
    const createTooltip = () => {
      const tooltip = document.createElement('simple-tooltip') as SimpleTooltip;
      callback(tooltip);
      target.parentNode!.insertBefore(tooltip, target.nextSibling);
      tooltip.show();
      // We only need to create the tooltip once, so ignore all future events.
      enterEvents.forEach(
        (eventName) => target.removeEventListener(eventName, createTooltip));
    };
    enterEvents.forEach(
      (eventName) => target.addEventListener(eventName, createTooltip));
  }

  static styles = css`
    :host {
      display: inline-block;
      position: fixed;
      padding: 4px;
      border: 1px solid darkgray;
      border-radius: 4px;
      background: #ccc;
      pointer-events: none;
      /* Animate in */
      opacity: 0;
      transform: scale(0.75);
      transition: opacity, transform;
      transition-duration:  0.33s;
    }

    :host([showing]) {
      opacity: 1;
      transform: scale(1);
    }
  `;

  @property({type: Number})
  offset = 4;

  // Attribute for styling "showing"
  @property({reflect: true, type: Boolean})
  showing = false;

  _target: Element|null = null;

  get target() {
    return this._target;
  }
  set target(target: Element|null) {
    // Remove events from existing target
    if (this.target) {
      enterEvents.forEach(name =>
        this.target!.removeEventListener(name, this.show));
      leaveEvents.forEach(name =>
        this.target!.removeEventListener(name, this.hide));
    }
    // Add events to new target
    if (target) {
      enterEvents.forEach(name =>
        target!.addEventListener(name, this.show));
      leaveEvents.forEach(name =>
        target!.addEventListener(name, this.hide));
    }
    this._target = target;
  }

  constructor() {
    super();
    // Finish hiding at end of animation
    this.addEventListener('transitionend', this.finishHide);
  }

  connectedCallback() {
    super.connectedCallback();
    this.target ??= this.previousElementSibling;
    this.finishHide();
  }

  render() {
    return html`<slot></slot>`;
  }

  show = () => {
    this.style.cssText = '';
    computePosition(this.target, this, {
      strategy: 'fixed',
      middleware: [
        offset(this.offset),
        shift(),
        autoPlacement({allowedPlacements: ['top', 'bottom']})
      ],
    }).then(({x, y}: {x: number, y: number}) => {
      this.style.left = `${x}px`;
      this.style.top = `${y}px`;
    });
    this.showing = true;
  };

  hide = () => {
    this.showing = false;
  };

  finishHide = () => {
    if (!this.showing) {
      this.style.display = 'none';
    }
  };

}

// Tooltip directive
class TooltipDirective extends Directive {
  didSetupLazy = false;
  tooltipContent?: unknown;
  part?: ElementPart;
  tooltip?: SimpleTooltip;

  // A directive must define a render method.
  render(tooltipContent: unknown = '') {}

  update(part: ElementPart, [tooltipContent]: DirectiveParameters<this>) {
    this.tooltipContent = tooltipContent;
    this.part = part;
    if (!this.didSetupLazy) {
      this.setupLazy();
    }
    if (this.tooltip) {
      this.renderTooltipContent();
    }
  }

  setupLazy() {
    this.didSetupLazy = true;
    SimpleTooltip.lazy(this.part!.element, (tooltip: SimpleTooltip) => {
      this.tooltip = tooltip;
      this.renderTooltipContent();
    });
  }

  renderTooltipContent() {
    render(this.tooltipContent, this.tooltip!, this.part!.options);
  }
}

export const tooltip = directive(TooltipDirective);

```

```ts
// Usage
import {html, css, LitElement} from 'lit';
import {customElement, property} from 'lit/decorators.js';
import './simple-tooltip.js';
import {tooltip} from './simple-tooltip.js';

@customElement('my-content')
export class MyContent extends LitElement {
  /* playground-fold */
  static styles = css`
    .box {
      height: 80px;
      width: 80px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: steelblue;
    }

    .right {
      position: absolute;
      right: 16px;
    }

    .container, #greeting {
      display: inline-flex;
      align-items: center;
    }

    .icon {
      font-family: 'Material Icons';
      font-size: 20px;
      margin: 0 0.25em;
      cursor: pointer;
    }

  `;

  @property()
  name = 'Katara';
  /* playground-fold-end */

  render() {
    return html`
      <h3>Welcome</h3>
      <p>Who are you?
        <span class="container">
          <input .value=${this.name} @input=${this._inputChange}>
          <span class="icon">help_outline</span>
        </span>
        <simple-tooltip>Enter your name...</simple-tooltip>
      </p>
      <p>
        <span id="greeting" ${tooltip(html`${this.name}, there's coffee available in the lounge.`)}>Hello, ${this.name}! <span class="icon">info_outline</span></span>
      </p>

      <h3>Some boxes hinted with tooltips</h3>
      <section>
        <div class="box">1</div>
        <simple-tooltip>This is box 1.</simple-tooltip>
        <div class="box">2</div>
        <simple-tooltip>This is box 2.</simple-tooltip>
        <div class="box right">3</div>
        <simple-tooltip>This is box 3 and it's way off on its own.</simple-tooltip>
      </section>
    `;
  }

  private _inputChange(e: InputEvent) {
    this.name = (e.target as HTMLInputElement).value;
  }

}
```
