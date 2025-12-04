# 875. Koko Eating Bananas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

[Problème 875] Find minimum eating speed to finish all bananas in...

## 💡 Solution APL

```apl
MinEatingSpeed ← {
    h←⍺
    speeds←1+⍳⌈/⍵
    ⊃speeds/⍨h≥+/⌈⍵÷⍤1⊢speeds
}
```

## 📝 Explication

Binary search on eating speed....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*log(max))`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #875](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
