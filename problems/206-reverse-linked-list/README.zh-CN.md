# 206. Reverse Linked List

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給定一個單鏈表的頭節點 head，反轉該鏈表，並返回反轉後的鏈表。

## 💡 APL 解法

```apl
ReverseList ← {⌽⍵}

⍝ Example usage:
⍝ ReverseList 1 2 3 4 5    → 5 4 3 2 1
⍝ ReverseList 1 2          → 2 1
⍝ ReverseList 1            → 1
```

## 📝 解释

使用反轉操作符（⌽）。在 APL 中，⌽ 沿著向量的最後一個軸反轉元素。這是最簡單的解決方案 - 只需要一個符號！

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #206](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
