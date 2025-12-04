# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

## 🟢 Schwierigkeit: Easy

## Problem

Ein Satz ist ein Palindrom, wenn er nach dem Umwandeln aller Großbuchstaben in Kleinbuchstaben und dem Entfernen aller nicht-alphanumerischen Zeichen vorwärts und rückwärts gleich gelesen wird. Alphanumerische Zeichen umfassen Buchstaben und Zahlen. Gegeben eine Zeichenkette s, gib true zurück, wenn es ein Palindrom ist, andernfalls false.

## 💡 APL-Lösung

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D)/⍵ ⋄ s≡⌽s}
```

## 📝 Erklärung

APL solution for Valid Palindrome. Uses reverse (⌽) to flip array elements. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #125](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
