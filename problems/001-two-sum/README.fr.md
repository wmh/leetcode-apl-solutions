# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné un tableau d'entiers nums et un entier target, renvoyez les indices des deux nombres qui totalisent target. Vous pouvez supposer que chaque entrée aurait exactement une solution, et vous ne pouvez pas utiliser le même élément deux fois. Vous pouvez renvoyer la réponse dans n'importe quel ordre.

## 💡 Solution APL

```apl
TwoSum ← {target←⍺ ⋄ arr←⍵ ⋄ sums←arr∘.+arr ⋄ mask←(sums=target)∧(∘.≠⍨⍳≢arr) ⋄ 2↑⍸mask}

⍝ Example usage:
⍝ 9 TwoSum 2 7 11 15    → 0 1
⍝ 6 TwoSum 3 2 4        → 1 2
⍝ 6 TwoSum 3 3          → 0 1
```

## 📝 Explication

Crée le produit extérieur (∘.+) du tableau avec lui-même pour obtenir toutes les sommes possibles. Utilise un masque pour exclure les paires du même index (∘.≠⍨⍳≢arr). Trouve les positions où la somme est égale à la cible avec ⍸. Prend les 2 premiers indices avec 2↑.

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
