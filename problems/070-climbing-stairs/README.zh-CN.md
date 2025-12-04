# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

假設你正在爬樓梯。需要 n 階你才能到達樓頂。每次你可以爬 1 或 2 個臺階。你有多少種不同的方法可以爬到樓頂呢？

## 💡 APL 解法

```apl
ClimbStairs ← {⊃(+⌿⍣(⍵-1))1 1}
```

## 📝 解释

這是斐波那契數列！使用冪運算符 (⍣⍵) 迭代 n 次，從 1 1 開始。每次迭代追加最後 2 個數字的和 ({⍵,+/¯2↑⍵})。取最終結果的第一個元素 (⊃)。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
