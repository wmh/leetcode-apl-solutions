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

對於 0 到 n 的每個數字 (⍳⍵+1)，使用基數 2 編碼轉換為二進制 (⊤⍨32⍴2)，然後對位求和 (+/)。¨ 操作符將操作應用於每個數字。

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
