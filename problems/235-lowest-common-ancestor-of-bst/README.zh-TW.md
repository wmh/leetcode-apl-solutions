# 235. Lowest Common Ancestor of BST

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目235] Find LCA in BST....

## 💡 APL 解法

```apl
LowestCommonAncestor ← {
    ⍝ Find split point
    ⊃⍸(⍺≤⍵)∧(⍵≤⍺)
}
```

## 📝 解釋

Uses BST property to find split point....

## ⏱️ 複雜度分析

- **時間複雜度**: `O(log n)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #235](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
