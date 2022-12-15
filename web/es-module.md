# ES Module

All modern browser support standard `es modules`. These are javascrript files using `import` & `export` statements.

- Loading ES modules in the browser

You can load javascript modules using scripts with type="module".

```html
<html>
  <body>
    <script type="module" src="./app.js"></script>
    <script type="module">
      import './app.js';
      // Implementation code
    </script>
  </body>
</html>
```

- Dynamic import

You can also import other modules using dynamic import() function. It's executed lazily, as the browserr will download the file only when the function needs the required source code.

```ts
function loadComponent(): Promise<TModule> {
  return import('./components/my-component.js');
}
```

- File extension

You will often see es modules using the `.mjs` file extension. For node js the `.mjs` file extension is an indication to execute the file as an es module. Node js will treat a file as an es module if it has a `.mjs` file extension, or if it has `.js` file extension and the package.json has `type="module"` set.

- Import path

In ES module, file extension is required to import a given library. But in node there is a logic to resolve modules imports so that `extension` is not needed.
