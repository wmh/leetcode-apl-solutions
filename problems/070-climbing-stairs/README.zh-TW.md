# 70. Climbing Stairs

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

假設你正在爬樓梯。需要 n 階你才能到達樓頂。每次你可以爬 1 或 2 個台階。你有多少種不同的方法可以爬到樓頂呢？

## 💡 APL 解法

```apl
ClimbStairs ← {⊃(+⌿⍣(⍵-1))1 1}
```

## 📝 解釋

這是費氏數列！使用冪運算子 (⍣⍵) 迭代 n 次，從 1 1 開始。每次迭代追加最後 2 個數字的和 ({⍵,+/¯2↑⍵})。取最終結果的第一個元素 (⊃)。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #70](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
