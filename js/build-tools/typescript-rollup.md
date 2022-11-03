# Typescript rollup confifuration

> `@open-wc/building-rollup` -> a rollup plugin for integration between Rollup.js and TypeScript
> `rimraf` -> Node js library similar to `rm -rf`
> `deepmerge` -> a tool to merge enumerable properties or more objects deeply.

## Typescript

- tsc
`tsc` is a typescript compiler that uses typescript configuration file `tsconfig.json` present at the root of any project to compile typescript files.

To create a typescript configuration file for a project.

> tsc --init

## Rollup

`rollup` is a module bundler, meaning it takes javascript codes splitted in modules using ES6 `import` and `export` mechanism, and compile them in a javascript bundle(s) that can be served by modern or legacy browsers.

- Module system
Rollup is build with new javascript module system in mind, therefore it by default bundles modules using the new `ES` module standard.

**Note** Rollup can support legacy module system like AMD, CommonJS or SystemJS through use of plugins.

The `@open-wc/building-rollup` provides developpers with basic configuration for working with rollup and typescript. Below is a base configration for such case:

```js
import merge from 'deepmerge';

import { createBasicConfig } from '@open-wc/building-rollup';

const base = createBasicConfig();

export default merge(base, {
    input: './lib/src/app.js',
    output: {
        dir: 'dist'
    }
})
```

**Note**
In case you're planning to build a SPA project(Single Page Application), you can use the createSpaConfig in Rollup configuration. Also, you can install the `@rollup/plugin-typescript` for seamless integration between Rollup and TypeScript.

The `@rollup/plugin-typescript` will load any compilerOptions from the tsconfig.json file by default.

```js

// rollup.config.js
import merge from 'deepmerge';
import { createSpaConfig } from '@open-wc/building-rollup';
import typescript from '@rollup/plugin-typescript';

const baseConfig = createSpaConfig({
    developmentMode: process.env.ROLLUP_WATCH === 'true',
    injectServiceWorker: false
});

export default merge(baseConfig, {
  // any <script type="module"> inside will be bundled by Rollup
  input: './index.html',
  plugins: [typescript()],
});
```

## What is Web Dev Server?

Web Dev Server, as its name states, it's a web server for development. It helps development using native browser features like ES modules. It has a plugin architecture for code transformations.

**Note** It's the successor of `es-dev-server` module.

**Note** It's worth mentioning that Web Dev Server allows configuring auto-reload on file changes along with efficient browser caching for faster reloads. It's configurable and supports `rollup plugins` too!

To install the web-dev-server:

> npm install --save-dev @web/dev-server

Web dev derver configuration:

The alternative option to include the CLI flags as parameters is the creation of the web-dev-server.config.js file.

**Note**
The file extension can be `.js`, `.cjs` or `.mjs`. A `.js` file will be loaded as an es module or common js module based on your version of node, and the package type of your project.

```js
// web-dev-server.config.js
module.exports = {
    port: 8000,
    nodeResolve: true,
    open: true,
    watch: true,
    appIndex: 'index.html',
};
```

- concurrently

`Concurrently` is a package allow us to execute commands in parallel. It allows developper to run any command he wants. It's possible to kill all of them if anyone fails.

An npm script for running a dev stack can be as follow:

**Note** This is simply a template, and can be altered to developper needs.

```json
"scripts": {
    "tsc:watch": "tsc --watch",
    "start": "concurrently --kill-others --names tsc,web-dev-server \"npm run tsc:watch\" \"web-dev-server --app-index --config web-dev-server.config.js\"",
    "build": "rimraf dist && tsc && rollup -c rollup.config.js"
},
```
