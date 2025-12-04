# 567. Permutation in String

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 567] Check if s2 contains a permutation of s1....

## 💡 APL-Lösung

```apl
CheckInclusion ← {
    (≢⍺)≤≢⍵:∨/{(∧/⍺∊⍵)∧∧/⍵∊⍺}¨(≢⍺)↑¨(≢⍵)↓¨⊂⍵
    0
}
```

## 📝 Erklärung

Checks each substring of length |s1| for character match....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n*m)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #567](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
