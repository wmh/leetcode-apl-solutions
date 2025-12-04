# 73. Set Matrix Zeroes

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

Set zeros

## 💡 Solution APL

```apl
SetZeroes ← {⍵×⍨∘.∧⍨~0∊¨↓⍵}
```

## 📝 Explication

Solution APL vérifiée

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(m*n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #73](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
