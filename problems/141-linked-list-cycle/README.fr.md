# 141. Linked List Cycle

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné head, la tête d'une liste chaînée, déterminez si la liste chaînée a un cycle. Il y a un cycle dans une liste chaînée s'il existe un nœud dans la liste qui peut être visité à nouveau en suivant continuellement le pointeur suivant. Renvoyez true s'il y a un cycle dans la liste chaînée. Sinon, renvoyez false.

## 💡 Solution APL

```apl
HasCycle ← {(≢⍵)≠≢∪⍵}

⍝ For array representation: check for duplicates
⍝ Example usage:
⍝ HasCycle 3 2 0 ¯4    → 0 (no cycle)
⍝ HasCycle 1 2 1       → 1 (has cycle - 1 repeats)
```

## 📝 Explication

Pour la représentation en tableau : vérifie si la longueur diffère de la longueur unique. S'il y a des doublons (cycle), les longueurs diffèrent. Utilise unique (∪) et comptage (≢).

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #141](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
