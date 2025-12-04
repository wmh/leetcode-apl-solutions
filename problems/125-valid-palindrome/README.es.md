# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟢 Dificultad: Easy

## Problema

Una frase es un palíndromo si, después de convertir todas las letras mayúsculas en minúsculas y eliminar todos los caracteres no alfanuméricos, se lee igual hacia adelante y hacia atrás. Los caracteres alfanuméricos incluyen letras y números. Dada una cadena s, devuelve true si es un palíndromo, o false en caso contrario.

## 💡 Solución APL

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D)/⍵ ⋄ s≡⌽s}
```

## 📝 Explicación

APL solution for Valid Palindrome. Uses reverse (⌽) to flip array elements. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #125](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
