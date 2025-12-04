# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

Gegeben eine Zeichenkette s, finde die Länge der längsten Teilzeichenkette ohne sich wiederholende Zeichen.

## 💡 APL-Lösung

```apl
LengthOfLongestSubstring ← {⌈/≢¨{⍵↑⍨¯1+1⍳⍨(⊂⊃⌽⍵)∊¨,\⍵}⍣≡¨,¨⍵}

⍝ Simpler approach - check all substrings:
LengthOfLongestSubstring2 ← {⌈/{(≢⍵)=≢∪⍵:≢⍵ ⋄ 0}¨{⍵↑¨⍺↓¨⊂⍵}⍨/⍳¨2⍴≢⍵}

⍝ Example usage:
⍝ LengthOfLongestSubstring2 'abcabcbb'    → 3
⍝ LengthOfLongestSubstring2 'bbbbb'      → 1
⍝ LengthOfLongestSubstring2 'pwwkew'     → 3
```

## 📝 Erklärung

Version 2: Generiert alle Teilzeichenketten, prüft jede auf Eindeutigkeit ((≢⍵)=≢∪⍵), gibt maximale Länge zurück. Verwendet verschachtelte Drops/Takes, um Teilzeichenketten zu erstellen.

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n²)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #3](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
