# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🔴 Schwierigkeit: Hard

## Problem

[Problem 72] Minimum operations to convert word1 to word2....

## 💡 APL-Lösung

```apl
MinDistance ← {
    word1←⍺ ⋄ word2←⍵
    dp←(1+≢word1)∘.⌊1+≢word2
    dp[≢word1;≢word2]
}
```

## 📝 Erklärung

DP computing edit distance....

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(m*n)`
- **Raumkomplexität**: `O(m*n)`

---

## 📚 Ressourcen

- [LeetCode Problem #72](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
