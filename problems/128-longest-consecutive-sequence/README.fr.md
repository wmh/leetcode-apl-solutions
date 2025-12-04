# 128. Longest Consecutive Sequence

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

[Problème 128] Find the length of the longest consecutive element...

## 💡 Solution APL

```apl
LongestConsecutive ← {
    ⍝ Find longest run
    sorted ← ∪⍵[⍋⍵]
    max ← ⌈/1,+/¨2=/¨1↓¨⊆sorted
    max
}
```

## 📝 Explication

Sorts unique elements and finds longest consecutive run....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*log(n))`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #128](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
