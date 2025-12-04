# 322. Coin Change

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟡 Schwierigkeit: Medium

## Problem

Min coins for amount

## 💡 APL-Lösung

```apl
CoinChange ← {⌊⍵÷⌊/⍺}
```

## 📝 Erklärung

APL solution for Coin Change. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(amount*n)`
- **Raumkomplexität**: `O(amount)`

---

## 📚 Ressourcen

- [LeetCode Problem #322](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
