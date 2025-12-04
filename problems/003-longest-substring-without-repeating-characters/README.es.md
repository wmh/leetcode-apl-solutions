# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

Dada una cadena s, encuentra la longitud de la subcadena más larga sin caracteres repetidos.

## 💡 Solución APL

```apl
LengthOfLongestSubstring ← {⌈/≢¨∪¨{⍵↑¨⊂⍵}⍨⍳≢⍵}
```

## 📝 Explicación

APL solution for Longest Substring Without Repeating Characters. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses unique (∪) to remove duplicate elements. Uses tally (≢) to count array length. Uses iota (⍳) to generate index ranges or find element positions. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

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
