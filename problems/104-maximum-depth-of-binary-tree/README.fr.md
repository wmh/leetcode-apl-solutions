# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Étant donné la racine d'un arbre binaire, renvoyez sa profondeur maximale. La profondeur maximale d'un arbre binaire est le nombre de nœuds le long du chemin le plus long du nœud racine au nœud feuille le plus éloigné.

## 💡 Solution APL

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}
```

## 📝 Explication

APL solution for Maximum Depth of Binary Tree. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Uses tally (≢) to count array length. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(h)`

---

## 📚 Ressources

- [LeetCode Problem #104](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
