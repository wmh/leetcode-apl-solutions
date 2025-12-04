# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Ein Satz ist ein Palindrom, wenn er nach dem Umwandeln aller Großbuchstaben in Kleinbuchstaben und dem Entfernen aller nicht-alphanumerischen Zeichen vorwärts und rückwärts gleich gelesen wird. Alphanumerische Zeichen umfassen Buchstaben und Zahlen. Gegeben eine Zeichenkette s, gib true zurück, wenn es ein Palindrom ist, andernfalls false.

## 💡 APL-Lösung

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D,⎕C⎕A)/⍵ ⋄ s≡⌽s}

⍝ Example usage:
⍝ IsPalindrome 'A man, a plan, a canal: Panama'    → 1
⍝ IsPalindrome 'race a car'                        → 0
⍝ IsPalindrome ' '                                 → 1
```

## 📝 Erklärung

Filtert, um nur alphanumerische Zeichen zu behalten: Großbuchstaben (⎕A), Ziffern (⎕D) und Kleinbuchstaben (⎕C⎕A). Überprüft dann, ob die gefilterte Zeichenkette mit ihrer Umkehrung übereinstimmt (s≡⌽s).

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
