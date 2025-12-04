# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben die Wurzel eines Binärbaums, gib seine maximale Tiefe zurück. Die maximale Tiefe eines Binärbaums ist die Anzahl der Knoten entlang des längsten Pfades vom Wurzelknoten bis zum entferntesten Blattknoten.

## 💡 APL-Lösung

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}
```

## 📝 Erklärung

APL solution for Maximum Depth of Binary Tree. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(h)`

---

## 📚 Ressourcen

- [LeetCode Problem #104](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
