# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給你一棵二叉樹的根節點 root，翻轉這棵二叉樹，並返回其根節點。

## 💡 APL 解法

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⍵[0],(∇⍵[2]),∇⍵[1]}

⍝ For nested representation:
⍝ Example usage:
⍝ InvertTree (4 (2 (1 ⍬ ⍬) (3 ⍬ ⍬)) (7 (6 ⍬ ⍬) (9 ⍬ ⍬)))
⍝ → (4 (7 (9 ⍬ ⍬) (6 ⍬ ⍬)) (2 (3 ⍬ ⍬) (1 ⍬ ⍬)))
```

## 📝 解释

遞歸交換左右子節點。基本情況：空樹返回空。遞歸情況：保持根節點，通過先遞歸右子節點再遞歸左子節點來交換子節點。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(h)`

---

## 📚 资源

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
