# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben eine Ganzzahl n, gib ein Array ans der Länge n + 1 zurück, sodass für jedes i (0 <= i <= n), ans[i] die Anzahl der 1en in der Binärdarstellung von i ist.

## 💡 APL-Lösung

```apl
CountBits ← {+/¨(⍳⍵+1)⊤⍨¨32⍴¨2}

⍝ Example usage:
⍝ CountBits 2    → 0 1 1
⍝ CountBits 5    → 0 1 1 2 1 2
```

## 📝 Erklärung

Für jede Zahl von 0 bis n (⍳⍵+1) konvertiert in Binär mit Basis-2-Kodierung (⊤⍨32⍴2), dann summiert die Bits (+/). Der ¨-Operator wendet die Operation auf jede Zahl an.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n*log(n))`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
