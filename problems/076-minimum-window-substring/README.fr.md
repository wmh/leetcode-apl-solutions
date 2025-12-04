# 76. Minimum Window Substring

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🔴 Difficulté: Hard

## Problème

[Problème 76] Find minimum window in s which contains all charac...

## 💡 Solution APL

```apl
MinWindow ← {
    ⍝ Sliding window with character count
    windows ← {⍵↑⍨⊃⍸(∧/⍺∊⍵)⍵}
    ⊃⌊/≢¨windows
}
```

## 📝 Explication

Maintains character counts in sliding window....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*m)`
- **Complexité Spatiale**: `O(m)`

---

## 📚 Ressources

- [LeetCode Problem #76](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
