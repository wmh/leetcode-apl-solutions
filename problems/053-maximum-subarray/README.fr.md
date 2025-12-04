# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

Étant donné un tableau d'entiers nums, trouvez le sous-tableau avec la plus grande somme et renvoyez sa somme.

## 💡 Solution APL

```apl
MaxSubArray ← {⌈/+\0⌈⍵}
```

## 📝 Explication

Utilise l'algorithme de Kadane. La version 3 est la plus simple : somme cumulative avec maximum courant (⌈\), préfixe 0 pour gérer les tableaux tous négatifs. Prend le maximum des sommes maximales courantes.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(1)`

---

## 📚 Ressources

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
