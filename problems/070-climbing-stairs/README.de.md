# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Du kletterst eine Treppe hoch. Es dauert n Schritte, um die Spitze zu erreichen. Jedes Mal kannst du entweder 1 oder 2 Stufen klettern. Auf wie viele verschiedene Arten kannst du die Spitze erreichen?

## 💡 APL-Lösung

```apl
ClimbStairs ← {⊃(+⌿⍣(⍵-1))1 1}
```

## 📝 Erklärung

Dies ist die Fibonacci-Folge! Iteriert n-mal mit dem Potenzoperator (⍣⍵), beginnend mit 1 1. Jede Iteration fügt die Summe der letzten 2 Zahlen hinzu ({⍵,+/¯2↑⍵}). Nimmt das erste Element (⊃) des Endergebnisses.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
