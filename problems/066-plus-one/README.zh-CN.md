# 66. Plus One

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給你一個由整數組成的非空數組，表示一個非負整數，請你把這個整數加一。最高位數字存放在數組的首位，數組中每個元素只存儲單個數字。你可以假設除了整數 0 之外，這個整數不會以零開頭。

## 💡 APL 解法

```apl
PlusOne ← {10⊥1+10⊥⍣¯1⊢⍵}
```

## 📝 解释

Plus One 的 APL 解决方案。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #66](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
