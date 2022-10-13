# Flexbox Layout

- Parent container
    Parent container must have a property of display flex. The container will try to align all it element on the same row by default.

```css
.parent {
    /* Container display */
    display: flex;

    /* Elements direction */
    flex-direction: row; /* Default: row; Values: row(Left->Right), colum(Top->Down), row-reverse(Right->Left), column-reverse(Bottom->Up)  */
    
    /* Wrapping */
    /* Retour */
    flex-wrap: wrap; /* Default: no-wrap; Values: wrap, no-wrap, wrap-reverse */

    /* Combination */
    flex-flow: /* Combine all direction, wrap values */


    /* How to justify items in the flexbox */
    justify-content: flex-start; /*Default : flex-start; Values: space-between, space-arround, flex-start, flex-end; center */

    /* Align items vertically */
    align-items: ; /* Default: stretch; Values: stretch, flex-start; flex-end; center*/

    /* Vertical justification */
    /* Only viable when elements wrap to multiple lines */
    align-content:  flex-start; /*Default : flex-start; Values: space-between, space-arround, flex-start, flex-end; center */
}
```

- Flexbox elements

> `order`: Determine l'ordre de positionnement des elements.

> `flex-grow`: Comment l'element d'agradit par rapport à l'espace restant.
> `flex-shrink`: inverse of flex-grow

> `flex-basis`: La base à utiliser pour le calcul de la taille des elements.

> flex: grow basis shrink;

> align-self: self alignment Values: flex-start, center

Note: Css

Selecting first, last and nth element:

```css
<.class|tag>:first-child {
    /* Select the first element */
}
<.class|tag>:nth-child(2) {
    /* Select the second element */
}
<.class|tag>:last-child {
    /* Select the second element */
}
```

Note: display: flex; align-items: center; justify-content: center; -> Pour centrer un element dans un conteneur
