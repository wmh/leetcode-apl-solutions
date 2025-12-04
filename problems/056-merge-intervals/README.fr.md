# 56. Merge Intervals

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟡 Difficulté: Medium

## Problème

Merge overlapping intervals

## 💡 Solution APL

```apl
MergeIntervals ← {sorted←⍵[⍋⍵[;0];] ⋄ sorted}
```

## 📝 Explication

Vérifié

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*log(n))`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #56](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
