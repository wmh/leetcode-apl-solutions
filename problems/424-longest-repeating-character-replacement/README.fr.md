# 424. Longest Repeating Character Replacement

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

[Problème 424] Find length of longest substring with same letter ...

## 💡 Solution APL

```apl
CharacterReplacement ← {
    k←⍺ ⋄ maxLen←0
    {maxLen⌈←≢⍵}¨⊆⍵
    maxLen
}
```

## 📝 Explication

APL solution for Longest Repeating Character Replacement. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #424](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
