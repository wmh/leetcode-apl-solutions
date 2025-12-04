# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

給你一棵二元樹的根節點 root，翻轉這棵二元樹，並返回其根節點。

## 💡 APL 解法

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⌽∇¨⍵}
```

## 📝 解釋

遞迴交換左右子節點。基本情況：空樹返回空。遞迴情況：保持根節點，通過先遞迴右子節點再遞迴左子節點來交換子節點。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(h)`

---

## 📚 資源

- [LeetCode Problem #226](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
