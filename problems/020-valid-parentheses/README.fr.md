# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟢 Difficulté: Easy

## Problème

Étant donné une chaîne s contenant uniquement les caractères '(', ')', '{', '}', '[' et ']', déterminez si la chaîne d'entrée est valide. Une chaîne d'entrée est valide si : Les crochets ouvrants doivent être fermés par le même type de crochets. Les crochets ouvrants doivent être fermés dans le bon ordre. Chaque crochet fermant a un crochet ouvrant correspondant du même type.

## 💡 Solution APL

```apl
IsValid ← {0=+/(⍵='(')-⍵=')'}
```

## 📝 Explication

APL solution for Valid Parentheses. Uses reduction (/) to aggregate values: +/ sums, ×/ multiplies, ⌈/ finds max, ⌊/ finds min. Implementation uses APL's array-oriented primitives for concise expression.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
