# 78. Subsets

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

Return all possible subsets

## 💡 Solution APL

```apl
Subsets ← {↓⍉(≢⍵)⊤⍳2*≢⍵}
```

## 📝 Explication

APL solution for Subsets. Uses tally (≢) to count array length. Uses iota (⍳) to generate index ranges or find element positions. Uses transpose (⍉) to swap matrix rows and columns. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(2^n)`
- **Complexité Spatiale**: `O(2^n)`

---

## 📚 Ressources

- [LeetCode Problem #78](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
