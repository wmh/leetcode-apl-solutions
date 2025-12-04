# 215. Kth Largest Element

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟡 Difficulté: Medium

## Problème

[Problème 215] Find kth largest element in array....

## 💡 Solution APL

```apl
FindKthLargest ← {
    k←⍺
    sorted←⍵[⍒⍵]
    sorted[k-1]
}
```

## 📝 Explication

Sorts in descending order and returns kth....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*log(n))`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #215](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
