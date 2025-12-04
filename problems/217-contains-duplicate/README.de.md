# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben ein Integer-Array nums, gib true zurück, wenn ein Wert mindestens zweimal im Array erscheint, und gib false zurück, wenn jedes Element eindeutig ist.

## 💡 APL-Lösung

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}
```

## 📝 Erklärung

Vergleicht die Länge des Arrays (≢⍵) mit der Länge der eindeutigen Elemente (≢∪⍵). Wenn sie sich unterscheiden, müssen Duplikate vorhanden sein. Der ≢-Operator gibt die Länge, ∪ gibt eindeutige Elemente und ≠ prüft, ob sie nicht gleich sind.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
