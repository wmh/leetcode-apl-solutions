# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

將兩個升序鏈表合併為一個新的升序鏈表並返回。新鏈表是通過拼接給定的兩個鏈表的所有節點組成的。

## 💡 APL 解法

```apl
MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}
```

## 📝 解释

Merge Two Sorted Lists 的 APL 解决方案。使用等级 (⍋/⍒) 排序 - 返回将对数组排序的索引。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O((n+m)*log(n+m))`
- **空间复杂度**: `O(n+m)`

---

## 📚 资源

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
