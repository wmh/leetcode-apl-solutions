# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Du erhältst ein Array prices, wobei prices[i] der Preis einer bestimmten Aktie am i-ten Tag ist. Du möchtest deinen Gewinn maximieren, indem du einen einzelnen Tag zum Kauf einer Aktie wählst und einen anderen Tag in der Zukunft zum Verkauf dieser Aktie wählst. Gib den maximalen Gewinn zurück, den du aus dieser Transaktion erzielen kannst. Wenn du keinen Gewinn erzielen kannst, gib 0 zurück.

## 💡 APL-Lösung

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}
```

## 📝 Erklärung

Verfolgt das laufende Minimum mit Scan (⌊\⍵). Subtrahiert das Minimum von jedem Preis (⍵-⌊\⍵), um den Gewinn an jedem Punkt zu erhalten. Nimmt das Maximum mit ⌈/ und vergleicht mit 0, um den Fall ohne Gewinn zu behandeln.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #121](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
