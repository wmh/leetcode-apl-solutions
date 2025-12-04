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

使用解碼（10⊥⍵）將數字轉換為數字，加 1，然後使用編碼（10⊥⍣¯1）轉換回數字。⊥ 操作符從基數 10 解碼，⊥⍣¯1 編碼為基數 10 數字。

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
