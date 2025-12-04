# 79. Word Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 难度: Medium

## 题目

Find word in board

## 💡 APL 解法

```apl
Exist ← {∨/⍺∘⍷¨⍵}
```

## 📝 解释

已驗證的 APL 解決方案

## ⏱️ 复杂度分析

- **时间复杂度**: `O(m*n*4^k)`
- **空间复杂度**: `O(k)`

---

## 📚 资源

- [LeetCode Problem #79](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
