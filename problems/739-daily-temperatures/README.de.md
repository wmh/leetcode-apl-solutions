# 739. Daily Temperatures

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 739] Find how many days until warmer temperature....

## 💡 APL-Lösung

```apl
DailyTemperatures ← {
    n←≢⍵
    result←n⍴0
    {result[⍵]←⊃⍸⍵<⍵↓⍵}¨⍳n
    result
}
```

## 📝 Erklärung

For each day, finds next warmer day....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n²)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #739](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
