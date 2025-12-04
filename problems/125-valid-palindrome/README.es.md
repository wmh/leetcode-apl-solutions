# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟢 Dificultad: Easy

## Problema

Una frase es un palíndromo si, después de convertir todas las letras mayúsculas en minúsculas y eliminar todos los caracteres no alfanuméricos, se lee igual hacia adelante y hacia atrás. Los caracteres alfanuméricos incluyen letras y números. Dada una cadena s, devuelve true si es un palíndromo, o false en caso contrario.

## 💡 Solución APL

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D,⎕C⎕A)/⍵ ⋄ s≡⌽s}

⍝ Example usage:
⍝ IsPalindrome 'A man, a plan, a canal: Panama'    → 1
⍝ IsPalindrome 'race a car'                        → 0
⍝ IsPalindrome ' '                                 → 1
```

## 📝 Explicación

Filtra para mantener solo caracteres alfanuméricos: mayúsculas (⎕A), dígitos (⎕D) y minúsculas (⎕C⎕A). Luego verifica si la cadena filtrada coincide con su reverso (s≡⌽s).

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
