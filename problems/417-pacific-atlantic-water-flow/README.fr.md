# 417. Pacific Atlantic Water Flow

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟡 Difficulté: Medium

## Problème

[Problème 417] Find cells from which water can flow to both ocean...

## 💡 Solution APL

```apl
PacificAtlantic ← {
    ⍝ DFS from both coasts
    pacific∩atlantic
}
```

## 📝 Explication

DFS from both ocean borders....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(m*n)`
- **Complexité Spatiale**: `O(m*n)`

---

## 📚 Ressources

- [LeetCode Problem #417](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
