# 136. Single Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Étant donné un tableau non vide d'entiers nums, chaque élément apparaît deux fois sauf un. Trouvez celui-là. Vous devez implémenter une solution avec une complexité temporelle linéaire et n'utiliser qu'un espace supplémentaire constant.

## 💡 Solution APL

```apl
SingleNumber ← {⊃⍸1=+⌿∘.=⍨⍵}
```

## 📝 Explication

Utilise la réduction XOR (≠/). XOR a la propriété que a⊕a=0 et a⊕0=a, donc les nombres en double s'annulent, ne laissant que le nombre unique. L'opérateur ≠ est XOR en APL, et / est l'opérateur de réduction qui applique XOR entre tous les éléments.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #136](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
