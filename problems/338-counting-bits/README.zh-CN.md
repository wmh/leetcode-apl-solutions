# 338. Counting Bits

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給你一個整數 n，對於 0 <= i <= n 中的每個 i，計算其二進制表示中 1 的個數，返回一個長度為 n+1 的數組 ans 作為答案。

## 💡 APL 解法

```apl
CountBits ← {+/¨2⊥⍣¯1¨⍳⍵+1}
```

## 📝 解释

Counting Bits 的 APL 解决方案。使用归约 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 iota (⍳) 生成索引范围或查找元素位置。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*log(n))`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #338](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
