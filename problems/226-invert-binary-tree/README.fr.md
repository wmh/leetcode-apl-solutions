# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné la racine d'un arbre binaire, inversez l'arbre et renvoyez sa racine.

## 💡 Solution APL

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⍵[0],(∇⍵[2]),∇⍵[1]}

⍝ For nested representation:
⍝ Example usage:
⍝ InvertTree (4 (2 (1 ⍬ ⍬) (3 ⍬ ⍬)) (7 (6 ⍬ ⍬) (9 ⍬ ⍬)))
⍝ → (4 (7 (9 ⍬ ⍬) (6 ⍬ ⍬)) (2 (3 ⍬ ⍬) (1 ⍬ ⍬)))
```

## 📝 Explication

Échange récursivement les enfants gauche et droit. Cas de base : l'arbre vide renvoie vide. Cas récursif : garde la racine, échange les enfants en récurant d'abord sur la droite puis sur la gauche.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(h)`

---

## 📚 Ressources

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
