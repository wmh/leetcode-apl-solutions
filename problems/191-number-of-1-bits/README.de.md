# 191. Number of 1 Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Schreibe eine Funktion, die die binäre Darstellung einer positiven Ganzzahl nimmt und die Anzahl der gesetzten Bits zurückgibt (auch als Hamming-Gewicht bekannt).

## 💡 APL-Lösung

```apl
HammingWeight ← {+/⍵⊤⍨32⍴2}

⍝ Example usage:
⍝ HammingWeight 11    → 3  (binary: 1011)
⍝ HammingWeight 128   → 1  (binary: 10000000)
⍝ HammingWeight 2147483645 → 30
```

## 📝 Erklärung

Konvertiert die Zahl in 32-Bit-Binär mit Kodierung (⊤⍨32⍴2), dann summiert die Bits mit +/. Der Kodierungsoperator ⊤ konvertiert zur angegebenen Basis.

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
