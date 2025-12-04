# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Du erhältst die Köpfe von zwei sortierten verknüpften Listen list1 und list2. Verschmelze die zwei Listen zu einer sortierten Liste. Die Liste sollte durch Zusammenfügen der Knoten der ersten zwei Listen erstellt werden. Gib den Kopf der verschmolzenen verknüpften Liste zurück.

## 💡 APL-Lösung

```apl
MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}
```

## 📝 Erklärung

APL solution for Merge Two Sorted Lists. Uses grade (⍋/⍒) for sorting - returns indices that would sort the array. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O((n+m)*log(n+m))`
- **Raumkomplexität**: `O(n+m)`

---

## 📚 Ressourcen

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
