# 371. Sum of Two Integers

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 371] Add two integers without + or -....

## 💡 APL-Lösung

```apl
GetSum ← {
    ⍝ XOR for sum, AND for carry
    (⍺≠⍵)+2×⍺∧⍵
}
```

## 📝 Erklärung

Uses XOR and AND operations....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(1)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #371](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
