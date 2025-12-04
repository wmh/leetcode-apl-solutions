# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben ein Array nums, das n verschiedene Zahlen im Bereich [0, n] enthält, gib die einzige Zahl im Bereich zurück, die im Array fehlt.

## 💡 APL-Lösung

```apl
MissingNumber ← {⊃(⍳1+⌈/⍵)~⍵}
```

## 📝 Erklärung

Verwendet die Formel für die Summe von 0 bis n: n×(n+1)÷2. Berechnet die erwartete Summe minus die tatsächliche Summe. Das Ergebnis ist die fehlende Zahl. (≢⍵) gibt n, also berechnen wir n×(n+1)÷2 - (+/⍵), wobei +/⍵ die Summe der Elemente ist.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
