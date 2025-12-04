# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Du erhältst eine große Ganzzahl, die als Integer-Array digits dargestellt wird, wobei jedes digits[i] die i-te Ziffer der Ganzzahl ist. Die Ziffern sind von der höchstwertigen zur niedrigstwertigen in Links-Rechts-Reihenfolge geordnet. Die große Ganzzahl enthält keine führenden Nullen. Erhöhe die große Ganzzahl um eins und gib das resultierende Array von Ziffern zurück.

## 💡 APL-Lösung

```apl
PlusOne ← {10⊥1+10⊥⍣¯1⊢⍵}
```

## 📝 Erklärung

APL solution for Plus One. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
