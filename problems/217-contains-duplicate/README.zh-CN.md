# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給定一個整數數組 nums，如果任何值在數組中出現至少兩次，則返回 true；如果每個元素都不同，則返回 false。

## 💡 APL 解法

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}
```

## 📝 解释

Contains Duplicate 的 APL 解决方案。使用 unique (∪) 去除重复元素。使用 tally (≢) 计算数组长度。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
