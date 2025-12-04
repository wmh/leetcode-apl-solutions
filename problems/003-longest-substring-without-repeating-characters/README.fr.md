# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟡 Difficulté: Medium

## Problème

Étant donné une chaîne s, trouvez la longueur de la plus longue sous-chaîne sans caractères répétitifs.

## 💡 Solution APL

```apl
LengthOfLongestSubstring ← {⌈/≢¨{⍵↑⍨¯1+1⍳⍨(⊂⊃⌽⍵)∊¨,\⍵}⍣≡¨,¨⍵}

⍝ Simpler approach - check all substrings:
LengthOfLongestSubstring2 ← {⌈/{(≢⍵)=≢∪⍵:≢⍵ ⋄ 0}¨{⍵↑¨⍺↓¨⊂⍵}⍨/⍳¨2⍴≢⍵}

⍝ Example usage:
⍝ LengthOfLongestSubstring2 'abcabcbb'    → 3
⍝ LengthOfLongestSubstring2 'bbbbb'      → 1
⍝ LengthOfLongestSubstring2 'pwwkew'     → 3
```

## 📝 Explication

Version 2 : Génère toutes les sous-chaînes, vérifie chacune pour l'unicité ((≢⍵)=≢∪⍵), renvoie la longueur maximale. Utilise des drops/takes imbriqués pour créer des sous-chaînes.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n²)`
- **Complexité Spatiale**: `O(n)`

---

## 📚 Ressources

- [LeetCode Problem #3](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
