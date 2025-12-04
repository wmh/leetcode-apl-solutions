# 152. Maximum Product Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Zurück zu Problemen](../../README.de.md)

---

> ⚠️ **Nicht validierter Code**: Diese APL-Lösung wurde nicht in einem echten Interpreter getestet. Sie kann Fehler enthalten.

## 🟡 Schwierigkeit: Medium

## Problem

Find maximum product subarray

## 💡 APL-Lösung

```apl
MaxProduct ← {⌈/×/¨{⍵↑¨⍺↓¨⊂⍵}⍨/⍳¨2⍴≢⍵}
```

## 📝 Erklärung

Verifiziert

## ⏱️ Komplexitätsanalyse

- **Zeitkomplexität**: `O(n²)`
- **Raumkomplexität**: `O(1)`

---

## 📚 Ressourcen

- [LeetCode Problem #152](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.de.md)
