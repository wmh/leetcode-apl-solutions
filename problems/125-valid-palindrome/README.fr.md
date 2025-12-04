# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Une phrase est un palindrome si, après avoir converti toutes les lettres majuscules en minuscules et supprimé tous les caractères non alphanumériques, elle se lit de la même manière vers l'avant et vers l'arrière. Les caractères alphanumériques incluent les lettres et les chiffres. Étant donné une chaîne s, renvoyez true si c'est un palindrome, ou false sinon.

## 💡 Solution APL

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D,⎕C⎕A)/⍵ ⋄ s≡⌽s}

⍝ Example usage:
⍝ IsPalindrome 'A man, a plan, a canal: Panama'    → 1
⍝ IsPalindrome 'race a car'                        → 0
⍝ IsPalindrome ' '                                 → 1
```

## 📝 Explication

Filtre pour ne garder que les caractères alphanumériques : majuscules (⎕A), chiffres (⎕D) et minuscules (⎕C⎕A). Vérifie ensuite si la chaîne filtrée correspond à son inverse (s≡⌽s).

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #125](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
