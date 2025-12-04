# 131. Palindrome Partitioning

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

[Problem 131] Partition string into palindromic substrings....

## 💡 APL-Lösung

```apl
Partition ← {
    ∪{⍵/⍨∧/⍵≡¨⌽¨⍵}¨partitions
}
```

## 📝 Erklärung

Generates partitions and filters palindromes....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n*2^n)`
- **Raumkomplexität**: `O(n)`

---

## 📚 Ressourcen

- [LeetCode Problem #131](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
