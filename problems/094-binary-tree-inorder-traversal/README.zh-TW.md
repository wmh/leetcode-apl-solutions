# 94. Binary Tree Inorder Traversal

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 難度: Easy

## 題目

給定一個二元樹的根節點 root，返回它節點值的中序遍歷。

## 💡 APL 解法

```apl
Inorder ← {0=≢⍵:⍬ ⋄ (∇⍵[1]),⍵[0],∇⍵[2]}

⍝ Example: (1 ⍬ (2 (3 ⍬ ⍬) ⍬)) → 1 3 2
```

## 📝 解釋

遞迴：遍歷左子樹，訪問根，遍歷右子樹。基本情況為空節點返回空。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(h)`

---

## 📚 資源

- [LeetCode Problem #94](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
