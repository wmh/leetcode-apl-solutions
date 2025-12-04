# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

> ⚠️ **Código no validado**: Esta solución APL no ha sido probada en un intérprete real. Puede contener errores.

## 🟡 Dificultad: Medium

## Problema

Dada una cadena s, encuentra la longitud de la subcadena más larga sin caracteres repetidos.

## 💡 Solución APL

```apl
LengthOfLongestSubstring ← {⌈/≢¨{⍵↑⍨¯1+1⍳⍨(⊂⊃⌽⍵)∊¨,\⍵}⍣≡¨,¨⍵}

⍝ Simpler approach - check all substrings:
LengthOfLongestSubstring2 ← {⌈/{(≢⍵)=≢∪⍵:≢⍵ ⋄ 0}¨{⍵↑¨⍺↓¨⊂⍵}⍨/⍳¨2⍴≢⍵}

⍝ Example usage:
⍝ LengthOfLongestSubstring2 'abcabcbb'    → 3
⍝ LengthOfLongestSubstring2 'bbbbb'      → 1
⍝ LengthOfLongestSubstring2 'pwwkew'     → 3
```

## 📝 Explicación

Versión 2: Genera todas las subcadenas, verifica cada una para unicidad ((≢⍵)=≢∪⍵), devuelve la longitud máxima. Usa drops/takes anidados para crear subcadenas.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n²)`
- **Complejidad Espacial**: `O(n)`

---

## 📚 Recursos

- [LeetCode Problem #3](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
