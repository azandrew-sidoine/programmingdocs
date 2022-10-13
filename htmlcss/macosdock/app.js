/**
 *
 * @param {number} val
 * @param {number} min
 * @param {number} max
 * @returns {number}
 */
function minmax(val, min, max) {
  return Math.max(min, Math.min(val, max));
}

/**
 * Generate element scaling based on the distance
 *
 * @param {number} val
 * @returns {number}
 */
function scaling(val) {
  return minmax(-0.2 * Math.pow(val, 2) + 1.05, 0, 1);
}

/**
 *
 * @param {number} i
 * @param {number} mousePosition
 * @param {number} scale
 */
function calculateScale(i, mousePosition, scale) {
  let center = i + 0.5;
  let distanceFromPointer = mousePosition - center;
  return scaling(distanceFromPointer) * scale;
}

/**
 * @param {number} index
 * @param {number} direction Position de l'icone (0: center, -1: right, 1: left)
 * @param {number} offset
 */
const scaleFromDirection =
  (index, direction, offset) =>
  /**
   *
   * @param {HTMLElement} icon
   * @param {number} mousePosition
   * @param {number} iconSize
   * @param {number} scale
   * @returns
   */
  (icon, mousePosition, iconSize, scale) => {
    if (typeof icon === "undefined" || icon === null) {
      return;
    }
    const _scale = calculateScale(index, mousePosition, scale);
    icon.style.setProperty(
      "transform",
      `translateX(${offset}px) scale(${_scale + 1})`
    );
    icon.style.setProperty(
      "transform-origin",
      `${TRANSFORM_ORIGIN[direction.toString()]} bottom`
    );
    return _scale * iconSize;
  };

/**
 * Applies translation and scaling to icons
 *
 * @param {HTMLElement[]} icons
 * @param {number} mousePosition
 * @param {number|undefined} iconSize
 * @param {number} scale
 */
function translateScaleIcons(icons, mousePosition, iconSize, scale) {
  if (!Array.isArray(icons)) {
    return;
  }
  const index = Math.floor(mousePosition);
  const centerOffset = mousePosition - index - 0.5;
  let baseOffset = scaleFromDirection(index, 0, -centerOffset * iconSize)(
    icons[index],
    mousePosition,
    iconSize,
    scale
  );
  let offset = baseOffset * (0.5 - centerOffset);
  for (let i = index + 1; i < icons.length; i++) {
    offset += scaleFromDirection(i, 1, offset)(
      icons[i],
      mousePosition,
      iconSize,
      scale
    );
  }
  offset = baseOffset * (0.5 + centerOffset);
  for (let i = index - 1; i >= 0; i--) {
    offset += scaleFromDirection(i, -1, -offset)(
      icons[i],
      mousePosition,
      iconSize,
      scale
    );
  }
}

const DEFAULT_OFFSET = 16;

// TODO : Change to enumeration
const TRANSFORM_ORIGIN = {
  "-1": "right",
  0: "center",
  1: "left",
};

/**
 * @property {HTMLElement[]} icons
 * @property {number} iconSize
 * @property {number} mousePosition
 */
class Dock {
  /**
   *
   * @param {HTMLElement} el
   * @param {HTMLElement[]} children
   * @param {number|null} scale
   */
  constructor(el, children, scale = null) {
    this.scale = scale || 1;
    this.icons = Array.from(children);
    this.iconSize = this.icons[0].offsetWidth;
    this.bindMouseMoveHandler(el, this.icons, this.iconSize, this.scale);
  }

  /**
   *
   * @param {HTMLElement} el
   * @param {HTMLElement[]} icons
   * @param {number} iconSize
   * @param {number} scale
   */
  bindMouseMoveHandler(el, icons, iconSize, scale) {
    /**
     * @param {MouseEvent} e
     */
    el.addEventListener("mousemove", (e) => {
      const mousePosition = minmax(
        (e.clientX - el.offsetLeft) / this.iconSize,
        0,
        this.icons.length
      );
      translateScaleIcons(icons, mousePosition, iconSize, scale);
    });

    el.addEventListener("mouveenter", (e) => {
      el.classList.add("animated");
      let timeout = setTimeout(() => {
        el.classList.remove("animated");
        clearTimeout(timeout);
      }, 100);
    });

    el.addEventListener("mouseleave", (e) => {
      // el.classList.add("animated");
      icons.forEach((icon) => {
        icon.style.removeProperty("transform");
        icon.style.removeProperty("transform-origin");
      });
    });
  }
}

let root = document.querySelector(".dock");
new Dock(root, root.children);
