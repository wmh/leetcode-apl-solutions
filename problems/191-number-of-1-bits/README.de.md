# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Schreibe eine Funktion, die die binäre Darstellung einer positiven Ganzzahl nimmt und die Anzahl der gesetzten Bits zurückgibt (auch als Hamming-Gewicht bekannt).

## 💡 APL-Lösung

```apl
HammingWeight ← {+/2⊥⍣¯1⊢⍵}
```

## 📝 Erklärung

APL solution for Number of 1 Bits. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(1)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #191](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
