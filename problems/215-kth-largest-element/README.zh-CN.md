# 215. Kth Largest Element

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目215] Find kth largest element in array....

## 💡 APL 解法

```apl
FindKthLargest ← {⊃⍵[⍒⍵]⌷⍨⍺}
```

## 📝 解释

Kth Largest Element 的 APL 解决方案。使用等级 (⍋/⍒) 排序 - 返回将对数组排序的索引。使用封闭 (⊂) 包装元素或展开 (⊃) 解包/提取。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*log(n))`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #215](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
