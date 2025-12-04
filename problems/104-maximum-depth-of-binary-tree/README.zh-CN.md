# 104. Maximum Depth of Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給定一個二叉樹的根節點 root，返回它的最大深度。二叉樹的最大深度是指從根節點到最遠葉子節點的最長路徑上的節點數。

## 💡 APL 解法

```apl
MaxDepth ← {0=≢⍵:0 ⋄ 1+⌈/∇¨⍵}
```

## 📝 解释

遞歸計算深度。基本情況：空樹深度為 0。遞歸情況：1 + 子節點的最大深度。使用自引用 (∇) 遞歸每個子節點，然後用 ⌈/ 取最大值。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(h)`

---

## 📚 资源

- [LeetCode Problem #104](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
