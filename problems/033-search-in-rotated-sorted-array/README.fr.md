# 33. Search in Rotated Sorted Array

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟡 Difficulté: Medium

## Problème

[Problème 33] Search for target in rotated sorted array....

## 💡 Solution APL

```apl
Search ← {
    pivot←⊃⍸⍵≠⌊/⍵
    target←⍺
    (target∊⍵)×⊃⍸target=⍵
}
```

## 📝 Explication

Finds pivot point and searches in correct half....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(log n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #33](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
