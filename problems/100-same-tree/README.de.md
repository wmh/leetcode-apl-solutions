# 100. Same Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben die Wurzeln von zwei Binärbäumen p und q, schreibe eine Funktion, um zu überprüfen, ob sie gleich sind oder nicht. Zwei Binärbäume werden als gleich betrachtet, wenn sie strukturell identisch sind und die Knoten denselben Wert haben.

## 💡 APL-Lösung

```apl
SameTree ← {⍺≡⍵}

⍝ For arrays representing trees:
⍝ Example usage:
⍝ (1 2 3) SameTree (1 2 3)    → 1
⍝ (1 2) SameTree (1 ⍬ 2)     → 0
⍝ (1 2 1) SameTree (1 1 2)   → 0
```

## 📝 Erklärung

Verwendet den Übereinstimmungsoperator (≡), der 1 zurückgibt, wenn Arrays in Struktur und Werten identisch sind, andernfalls 0. Dies ist die einfachst mögliche Lösung - nur ein Symbol!

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #100](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
