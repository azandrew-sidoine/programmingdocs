# CSS Notes

- Attribute function

Nous permet de récupérer la valeur d'un attribut sur un element html.

```html
<span data-attrname=""></span>
```

```css
span::after {
    content: attr(attrname)
}
```

- Transformation

Apply mathematic transformation to HTML element. (Translate[X|Y|Z|None], Translate3d, Matrix, Scale[X|Y|Z|None], Scale3d, Rotate[X|Y|None], Rotate3d, Skew[X|Y|None])

```html

<img src="..." />
```

```css
/* Translate */
img {
    transform: translate(100px, 100px); /* transform: translate(x, y); */
}

/* Rotate */
img {
    transform: rotate(90deg); /* transform: rotate(ø); */
}

/* Scale for zooming */
img:hover {
    transform: scale(1.1) rotate(10deg); /* transform: scale(x, y); */
}

/* Transformation suivant un parallelogramme */
img:hover {
    transform: skew(1.1); /* transform: skew(x, y); */
}
```

-- Perspectives

Allow to manipulate the depth of an element when translating, rotating or scaling the element.

Properties: `perspective, perspective-origin`
