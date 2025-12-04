# 202. Happy Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

編寫一個算法來判斷一個數 n 是不是快樂數。「快樂數」定義為：對於一個正整數，每一次將該數替換為它每個位置上的數字的平方和。然後重複這個過程直到這個數變為 1，也可能是無限循環但始終變不到 1。如果這個過程結果為 1，那麼這個數就是快樂數。如果 n 是快樂數就返回 true；不是，則返回 false。

## 💡 APL 解法

```apl
IsHappy ← {1∊⍵}
```

## 📝 解释

Happy Number 的 APL 解决方案。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(log n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #202](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
