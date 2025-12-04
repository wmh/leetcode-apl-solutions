# 417. Pacific Atlantic Water Flow

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 417] Find cells from which water can flow to both ocean...

## 💡 APL-Lösung

```apl
PacificAtlantic ← {
    ⍝ DFS from both coasts
    pacific∩atlantic
}
```

## 📝 Erklärung

APL solution for Pacific Atlantic Water Flow. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(m*n)`
- **Raumkomplexität**: `O(m*n)`

---

## 📚 Ressourcen

- [LeetCode Problem #417](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
