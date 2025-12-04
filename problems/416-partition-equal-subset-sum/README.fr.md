# 416. Partition Equal Subset Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Retour aux Problèmes](../../README.fr.md)

---

> ⚠️ **Code non validé**: Cette solution APL n'a pas été testée dans un interpréteur réel. Elle peut contenir des erreurs.

## 🟡 Difficulté: Medium

## Problème

[Problème 416] Determine if array can be partitioned into two sub...

## 💡 Solution APL

```apl
CanPartition ← {
    target←(+/⍵)÷2
    2|+/⍵:0
    target∊+/¨subsets
}
```

## 📝 Explication

Checks if subset sum equals half of total....

## ⏱️ Analyse de Complexité

- **Complexité Temporelle**: `O(n*sum)`
- **Complexité Spatiale**: `O(sum)`

---

## 📚 Ressources

- [LeetCode Problem #416](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.fr.md)
