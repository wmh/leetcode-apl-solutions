# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

On vous donne un tableau prices où prices[i] est le prix d'une action donnée le i-ème jour. Vous voulez maximiser votre profit en choisissant un seul jour pour acheter une action et en choisissant un jour différent dans le futur pour vendre cette action. Renvoyez le profit maximum que vous pouvez réaliser de cette transaction. Si vous ne pouvez réaliser aucun profit, renvoyez 0.

## 💡 Solution APL

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}
```

## 📝 Explication

APL solution for Best Time to Buy and Sell Stock. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses scan (\) to compute running operations: +\ is running sum, ×\ is running product, ⌈\ is running max, ⌊\ is running min. Implementation uses APL's array-oriented primitives for concise expression.

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
