# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben ein nicht-leeres Array von Ganzzahlen nums, erscheint jedes Element zweimal außer einem. Finde dieses eine. Du musst eine Lösung mit linearer Zeitkomplexität implementieren und nur konstanten zusätzlichen Speicherplatz verwenden.

## 💡 APL-Lösung

```apl
SingleNumber ← {⊃⍸1=+⌿∘.=⍨⍵}
```

## 📝 Erklärung

Verwendet XOR-Reduktion (≠/). XOR hat die Eigenschaft, dass a⊕a=0 und a⊕0=a, sodass sich doppelte Zahlen aufheben und nur die einzelne Zahl übrig bleibt. Der ≠-Operator ist XOR in APL, und / ist der Reduktionsoperator, der XOR zwischen allen Elementen anwendet.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
