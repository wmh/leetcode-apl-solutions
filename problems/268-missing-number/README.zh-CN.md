# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給定一個包含 n 個不同數字的數組 nums，範圍是 [0, n]，返回範圍內缺失的唯一數字。

## 💡 APL 解法

```apl
MissingNumber ← {⊃(⍳1+⌈/⍵)~⍵}
```

## 📝 解释

Missing Number 的 APL 解决方案。使用归约 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 iota (⍳) 生成索引范围或查找元素位置。使用封闭 (⊂) 包装元素或展开 (⊃) 解包/提取。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
