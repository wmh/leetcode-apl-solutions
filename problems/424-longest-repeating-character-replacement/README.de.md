# 424. Longest Repeating Character Replacement

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 424] Find length of longest substring with same letter ...

## 💡 APL-Lösung

```apl
CharacterReplacement ← {
    k←⍺ ⋄ maxLen←0
    {maxLen⌈←≢⍵}¨⊆⍵
    maxLen
}
```

## 📝 Erklärung

Slides window and counts character frequencies....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #424](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
