# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🔴 Difficulté: Hard

## Problème

[Problème 72] Minimum operations to convert word1 to word2....

## 💡 Solution APL

```apl
MinDistance ← {+/≠⌿⍺ ⍵}
```

## 📝 Explication

APL solution for Edit Distance. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(m*n)`
- **Complexité Spatiale**: `O(m*n)`

---

## 📚 Ressources

- [LeetCode Problem #72](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
