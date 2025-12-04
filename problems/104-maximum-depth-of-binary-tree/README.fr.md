# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné la racine d'un arbre binaire, renvoyez sa profondeur maximale. La profondeur maximale d'un arbre binaire est le nombre de nœuds le long du chemin le plus long du nœud racine au nœud feuille le plus éloigné.

## 💡 Solution APL

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}

⍝ For nested arrays:
⍝ Example usage:
⍝ MaxDepth (3 (9 ⍬ ⍬) (20 (15 ⍬ ⍬) (7 ⍬ ⍬)))    → 3
⍝ MaxDepth (1 ⍬ (2 ⍬ ⍬))                          → 2
```

## 📝 Explication

Compte récursivement la profondeur. Cas de base : l'arbre vide a une profondeur de 0. Cas récursif : 1 + profondeur maximale des enfants. Utilise l'auto-référence (∇) pour récurrer sur chaque enfant, puis prend le maximum avec ⌈/.

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
