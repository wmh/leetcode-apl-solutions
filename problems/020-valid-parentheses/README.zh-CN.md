# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給定一個只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判斷字符串是否有效。有效字符串需滿足：左括號必須用相同類型的右括號閉合。左括號必須以正確的順序閉合。每個右括號都有一個對應的相同類型的左括號。

## 💡 APL 解法

```apl
IsValid ← {0=+/(⍵='(')-⍵=')'}
```

## 📝 解释

Valid Parentheses 的 APL 解决方案。使用归约 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
