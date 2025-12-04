# 94. Binary Tree Inorder Traversal

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben die Wurzel eines Binärbaums, gib die Inorder-Traversierung seiner Knotenwerte zurück.

## 💡 APL-Lösung

```apl
Inorder ← {0=≢⍵:⍬ ⋄ (∇⍵[1]),⍵[0],∇⍵[2]}

⍝ Example: (1 ⍬ (2 (3 ⍬ ⍬) ⍬)) → 1 3 2
```

## 📝 Erklärung

Rekursiv: durchlaufe links, besuche Wurzel, durchlaufe rechts. Basisfall gibt leer für null-Knoten zurück.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(h)`

---

## 📚 Ressourcen

- [LeetCode Problem #94](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
