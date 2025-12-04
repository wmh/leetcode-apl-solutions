# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben die Wurzel eines Binärbaums, invertiere den Baum und gib seine Wurzel zurück.

## 💡 APL-Lösung

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⍵[0],(∇⍵[2]),∇⍵[1]}

⍝ For nested representation:
⍝ Example usage:
⍝ InvertTree (4 (2 (1 ⍬ ⍬) (3 ⍬ ⍬)) (7 (6 ⍬ ⍬) (9 ⍬ ⍬)))
⍝ → (4 (7 (9 ⍬ ⍬) (6 ⍬ ⍬)) (2 (3 ⍬ ⍬) (1 ⍬ ⍬)))
```

## 📝 Erklärung

Tauscht rekursiv linke und rechte Kinder aus. Basisfall: leerer Baum gibt leer zurück. Rekursiver Fall: behält Wurzel, tauscht Kinder durch Rekursion zuerst auf rechtes dann linkes Kind.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(h)`

---

## 📚 Ressourcen

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
