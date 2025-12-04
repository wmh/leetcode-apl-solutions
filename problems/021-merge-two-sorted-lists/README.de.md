# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Du erhältst die Köpfe von zwei sortierten verknüpften Listen list1 und list2. Verschmelze die zwei Listen zu einer sortierten Liste. Die Liste sollte durch Zusammenfügen der Knoten der ersten zwei Listen erstellt werden. Gib den Kopf der verschmolzenen verknüpften Liste zurück.

## 💡 APL-Lösung

```apl
MergeTwoLists ← {⍺[⍋⍺,⍵],⍵[⍋⍺,⍵]}

⍝ Simpler version:
MergeTwoLists2 ← {(⍺,⍵)[⍋⍺,⍵]}

⍝ Example usage:
⍝ 1 2 4 MergeTwoLists2 1 3 4    → 1 1 2 3 4 4
⍝ ⍬ MergeTwoLists2 0            → 0
⍝ ⍬ MergeTwoLists2 ⍬            → ⍬
```

## 📝 Erklärung

Verkettet beide Listen (⍺,⍵) und sortiert dann nach aufsteigendem Grad (⍋). Aufsteigender Grad gibt Indizes zurück, die das Array sortieren würden. Version 2 ist sauberer: verketten und dann nach sortierten Positionen indizieren.

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
