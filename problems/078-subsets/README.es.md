# 78. Subsets

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

Return all possible subsets

## 💡 Solución APL

```apl
Subsets ← {↓⍉(≢⍵)⊤⍳2*≢⍵}
```

## 📝 Explicación

APL solution for Subsets. Uses tally (≢) to count array length. Uses iota (⍳) to generate index ranges or find element positions. Uses transpose (⍉) to swap matrix rows and columns. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(2^n)`
- **Complejidad Espacial**: `O(2^n)`

---

## 📚 Recursos

- [LeetCode Problem #78](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
