# 295. Find Median from Data Stream

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🔴 Schwierigkeit: Hard

## Problem

[Problem 295] Find median from data stream....

## 💡 APL-Lösung

```apl
FindMedian ← {
    sorted←⍵[⍋⍵]
    n←≢sorted
    2|n:sorted[⌊n÷2]
    +⌿sorted[(n÷2)+¯1 0]÷2
}
```

## 📝 Erklärung

Maintains sorted order and computes median....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n*log(n))`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #295](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
