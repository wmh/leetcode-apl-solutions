# 739. Daily Temperatures

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

[Problème 739] Find how many days until warmer temperature....

## 💡 Solution APL

```apl
DailyTemperatures ← {
    n←≢⍵
    result←n⍴0
    {result[⍵]←⊃⍸⍵<⍵↓⍵}¨⍳n
    result
}
```

## 📝 Explication

For each day, finds next warmer day....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n²)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #739](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
