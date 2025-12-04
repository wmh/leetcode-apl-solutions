# 94. Binary Tree Inorder Traversal

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné la racine d'un arbre binaire, renvoyez la traversée en ordre de ses valeurs de nœuds.

## 💡 Solution APL

```apl
Inorder ← {0=≢⍵:⍬ ⋄ (∇⍵[1]),⍵[0],∇⍵[2]}

⍝ Example: (1 ⍬ (2 (3 ⍬ ⍬) ⍬)) → 1 3 2
```

## 📝 Explication

Récursif : parcourt à gauche, visite la racine, parcourt à droite. Le cas de base renvoie vide pour les nœuds nuls.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(h)`

---

## 📚 Ressources

- [LeetCode Problem #94](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
