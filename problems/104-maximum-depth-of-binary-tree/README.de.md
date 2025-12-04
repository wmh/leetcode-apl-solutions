# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben die Wurzel eines Binärbaums, gib seine maximale Tiefe zurück. Die maximale Tiefe eines Binärbaums ist die Anzahl der Knoten entlang des längsten Pfades vom Wurzelknoten bis zum entferntesten Blattknoten.

## 💡 APL-Lösung

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}

⍝ For nested arrays:
⍝ Example usage:
⍝ MaxDepth (3 (9 ⍬ ⍬) (20 (15 ⍬ ⍬) (7 ⍬ ⍬)))    → 3
⍝ MaxDepth (1 ⍬ (2 ⍬ ⍬))                          → 2
```

## 📝 Erklärung

Zählt rekursiv die Tiefe. Basisfall: leerer Baum hat Tiefe 0. Rekursiver Fall: 1 + maximale Tiefe der Kinder. Verwendet Selbstreferenz (∇), um über jedes Kind zu rekurrieren, dann nimmt das Maximum mit ⌈/.

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
