# 79. Word Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

Find word in board

## 💡 Solution APL

```apl
Exist ← {∨/⍺∊¨,⍵}
```

## 📝 Explication

APL solution for Word Search. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(m*n*4^k)`
- **Complexité Spatiale**: `O(k)`

---

## 📚 Ressources

- [LeetCode Problem #79](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
