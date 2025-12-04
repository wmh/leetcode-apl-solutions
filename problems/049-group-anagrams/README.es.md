# 49. Group Anagrams

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Volver a Problemas](../../README.es.md)

---

## 🟡 Dificultad: Medium

## Problema

Group anagrams

## 💡 Solución APL

```apl
GroupAnagrams ← {⍵⌸⍨⍋¨⍵}
```

## 📝 Explicación

APL solution for Group Anagrams. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Análisis de Complejidad

- **Complejidad Temporal**: `O(n*k*log k)`
- **Complejidad Espacial**: `O(n*k)`

---

## 📚 Recursos

- [LeetCode Problem #49](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.es.md)
