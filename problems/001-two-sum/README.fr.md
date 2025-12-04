# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Étant donné un tableau d'entiers nums et un entier target, renvoyez les indices des deux nombres qui totalisent target. Vous pouvez supposer que chaque entrée aurait exactement une solution, et vous ne pouvez pas utiliser le même élément deux fois. Vous pouvez renvoyer la réponse dans n'importe quel ordre.

## 💡 Solution APL

```apl
TwoSum ← {(⊃⍸⍺=+/∘.,⍨⍵)}
```

## 📝 Explication

APL solution for Two Sum. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses where (⍸) to find indices of true/non-zero elements. Uses enclose (⊂) to wrap elements or disclose (⊃) to unwrap/extract. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n²)`
- **Complexité Spatiale**: `O(n²)`

---

## 📚 Ressources

- [LeetCode Problem #1](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
