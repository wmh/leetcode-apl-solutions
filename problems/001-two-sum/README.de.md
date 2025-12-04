# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben ein Array von Ganzzahlen nums und eine Ganzzahl target, gib die Indizes der zwei Zahlen zurück, die sich zu target addieren. Du kannst annehmen, dass jede Eingabe genau eine Lösung hat, und du darfst dasselbe Element nicht zweimal verwenden. Du kannst die Antwort in beliebiger Reihenfolge zurückgeben.

## 💡 APL-Lösung

```apl
TwoSum ← {(⊃⍸⍺=+/∘.,⍨⍵)}
```

## 📝 Erklärung

APL solution for Two Sum. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses where (⍸) to find indices of true/non-zero elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n²)`
- **Raumkomplexität**: `O(n²)`

---

## 📚 Ressourcen

- [LeetCode Problem #1](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
