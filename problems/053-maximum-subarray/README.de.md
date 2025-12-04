# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

Gegeben ein Integer-Array nums, finde das Teilarray mit der größten Summe und gib seine Summe zurück.

## 💡 APL-Lösung

```apl
MaxSubArray ← {⌈/+\0⌈⍵-+\0,⍨⌊\+\⍵}

⍝ Simpler Kadane's algorithm:
MaxSubArray2 ← {⌈/{⌈/+\⍵}¨↓∘.,⍨⍳≢⍵}

⍝ Most readable:
MaxSubArray3 ← {⌈/⌈\0,+\⍵}

⍝ Example usage:
⍝ MaxSubArray3 ¯2 1 ¯3 4 ¯1 2 1 ¯5 4    → 6
⍝ MaxSubArray3 1                        → 1
⍝ MaxSubArray3 5 4 ¯1 7 8               → 23
```

## 📝 Erklärung

Verwendet Kadanes Algorithmus. Version 3 ist am einfachsten: kumulative Summe mit laufendem Maximum (⌈\), voranstellen von 0, um all-negative Arrays zu behandeln. Nimmt das Maximum der laufenden maximalen Summen.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
