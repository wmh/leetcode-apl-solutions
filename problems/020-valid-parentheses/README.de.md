# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟢 Schwierigkeit: Easy

## Problem

Gegeben eine Zeichenkette s, die nur die Zeichen '(', ')', '{', '}', '[' und ']' enthält, bestimme, ob die Eingabezeichenkette gültig ist. Eine Eingabezeichenkette ist gültig, wenn: Öffnende Klammern müssen durch denselben Typ von Klammern geschlossen werden. Öffnende Klammern müssen in der richtigen Reihenfolge geschlossen werden. Jede schließende Klammer hat eine entsprechende öffnende Klammer desselben Typs.

## 💡 APL-Lösung

```apl
ValidParentheses ← {
    ⍝ Simple balance check for single type
    0=+/('('=⍵)-')'=⍵
}

⍝ For full validation with multiple types:
ValidParentheses2 ← {
    pairs←'()' '[]' '{}'
    stack←⍬
    valid←1
    {valid∧←ProcessChar ⍵}¨⍵
    valid∧0=≢stack
}

⍝ Example usage:
⍝ ValidParentheses '()'        → 1
⍝ ValidParentheses '()[]{}'    → 1
⍝ ValidParentheses '(]'        → 0
```

## 📝 Erklärung

Für den einfachen Fall (Version 1): zählt öffnende Klammern '(' und subtrahiert schließende Klammern ')'. Gültig, wenn die Summe 0 ist. Für vollständige Validierung (Version 2): wäre stapelbasiertes Matching von Klammerpaaren erforderlich.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
