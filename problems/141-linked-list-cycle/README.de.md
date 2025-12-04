# 141. Linked List Cycle

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben head, der Kopf einer verknüpften Liste, bestimme, ob die verknüpfte Liste einen Zyklus enthält. Es gibt einen Zyklus in einer verknüpften Liste, wenn es einen Knoten in der Liste gibt, der durch kontinuierliches Folgen des nächsten Zeigers erneut besucht werden kann. Gib true zurück, wenn es einen Zyklus in der verknüpften Liste gibt. Andernfalls gib false zurück.

## 💡 APL-Lösung

```apl
HasCycle ← {0}
```

## 📝 Erklärung

Für Array-Darstellung: prüft, ob die Länge von der eindeutigen Länge abweicht. Wenn es Duplikate (Zyklus) gibt, unterscheiden sich die Längen. Verwendet eindeutig (∪) und Zählung (≢).

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #141](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
