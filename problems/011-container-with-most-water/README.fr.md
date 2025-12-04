# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

## 🟡 Difficulté: Medium

## Problème

On vous donne un tableau d'entiers height de longueur n. Il y a n lignes verticales dessinées de telle sorte que les deux extrémités de la i-ème ligne sont (i, 0) et (i, height[i]). Trouvez deux lignes qui, avec l'axe des x, forment un conteneur tel que le conteneur contienne le plus d'eau. Renvoyez la quantité maximale d'eau qu'un conteneur peut stocker.

## 💡 Solution APL

```apl
MaxArea ← {⌈/,((⍵∘.⌊⍵)×(⍳≢⍵)∘.-⍳≢⍵)}
```

## 📝 Explication

Crée le produit extérieur des hauteurs (∘.⌊) pour obtenir les hauteurs minimales pour toutes les paires. Multiplie par les distances ((⍳n)∘.-⍳n) pour obtenir les surfaces. Prend le maximum.

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n²)`
- **Complexité Spatiale**: `O(n²)`

---

## 📚 Ressources

- [LeetCode Problem #11](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
