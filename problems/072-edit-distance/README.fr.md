# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🔴 Difficulté: Hard

## Problème

[Problème 72] Minimum operations to convert word1 to word2....

## 💡 Solution APL

```apl
MinDistance ← {
    word1←⍺ ⋄ word2←⍵
    dp←(1+≢word1)∘.⌊1+≢word2
    dp[≢word1;≢word2]
}
```

## 📝 Explication

DP computing edit distance....

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
