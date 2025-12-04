# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Dado un array no vacío de enteros nums, cada elemento aparece dos veces excepto uno. Encuentra ese único. Debes implementar una solución con complejidad de tiempo lineal y usar solo espacio extra constante.

## 💡 Solución APL

```apl
SingleNumber ← {≠/⍵}

⍝ Example usage:
⍝ SingleNumber 4 1 2 1 2    → 4
⍝ SingleNumber 2 2 1        → 1
⍝ SingleNumber 1            → 1
```

## 📝 Explicación

Utiliza reducción XOR (≠/). XOR tiene la propiedad de que a⊕a=0 y a⊕0=a, por lo que los números duplicados se cancelan, dejando solo el número único. El operador ≠ es XOR en APL, y / es el operador de reducción que aplica XOR entre todos los elementos.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(1)`

---

## 📚 Recursos

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
