# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

On vous donne un tableau prices où prices[i] est le prix d'une action donnée le i-ème jour. Vous voulez maximiser votre profit en choisissant un seul jour pour acheter une action et en choisissant un jour différent dans le futur pour vendre cette action. Renvoyez le profit maximum que vous pouvez réaliser de cette transaction. Si vous ne pouvez réaliser aucun profit, renvoyez 0.

## 💡 Solution APL

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}

⍝ Example usage:
⍝ MaxProfit 7 1 5 3 6 4    → 5
⍝ MaxProfit 7 6 4 3 1      → 0
```

## 📝 Explication

Suit le minimum courant avec scan (⌊\⍵). Soustrait le minimum de chaque prix (⍵-⌊\⍵) pour obtenir le profit à chaque point. Prend le maximum avec ⌈/ et compare avec 0 pour gérer le cas sans profit.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #121](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
