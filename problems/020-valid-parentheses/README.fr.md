# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟢 Difficulté: Easy

## Problème

Étant donné une chaîne s contenant uniquement les caractères '(', ')', '{', '}', '[' et ']', déterminez si la chaîne d'entrée est valide. Une chaîne d'entrée est valide si : Les crochets ouvrants doivent être fermés par le même type de crochets. Les crochets ouvrants doivent être fermés dans le bon ordre. Chaque crochet fermant a un crochet ouvrant correspondant du même type.

## 💡 Solution APL

```apl
ValidParentheses ← {
    ⍝ Simple balance check for single type
    0=+/('('=⍵)-')'=⍵
}

⍝ For full validation with multiple types:
ValidParentheses2 ← {
    pairs←'()' '[]' '{}'
    stack←⍬
    valid←1
    {valid∧←ProcessChar ⍵}¨⍵
    valid∧0=≢stack
}

⍝ Example usage:
⍝ ValidParentheses '()'        → 1
⍝ ValidParentheses '()[]{}'    → 1
⍝ ValidParentheses '(]'        → 0
```

## 📝 Explication

Pour le cas simple (version 1) : compte les parenthèses ouvrantes '(' et soustrait les parenthèses fermantes ')'. Valide si la somme est 0. Pour une validation complète (version 2) : nécessiterait une correspondance de paires de crochets basée sur une pile.

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
