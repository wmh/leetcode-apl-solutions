# 226. Invert Binary Tree

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給你一棵二叉樹的根節點 root，翻轉這棵二叉樹，並返回其根節點。

## 💡 APL 解法

```apl
InvertTree ← {0=≢⍵:⍵ ⋄ ⌽∇¨⍵}
```

## 📝 解释

Invert Binary Tree 的 APL 解决方案。使用反转 (⌽) 翻转数组元素。使用 tally (≢) 计算数组长度。实现使用 APL 的面向数组原语进行简洁表达。

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
