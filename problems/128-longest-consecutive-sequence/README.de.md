# 128. Longest Consecutive Sequence

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 128] Find the length of the longest consecutive element...

## 💡 APL-Lösung

```apl
LongestConsecutive ← {
    ⍝ Find longest run
    sorted ← ∪⍵[⍋⍵]
    max ← ⌈/1,+/¨2=/¨1↓¨⊆sorted
    max
}
```

## 📝 Erklärung

Sorts unique elements and finds longest consecutive run....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n*log(n))`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #128](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
