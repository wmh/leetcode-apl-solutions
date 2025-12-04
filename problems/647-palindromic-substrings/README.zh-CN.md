# 647. Palindromic Substrings

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目647] Count palindromic substrings....

## 💡 APL 解法

```apl
CountSubstrings ← {
    ≢{⍵/⍨⍵≡¨⌽¨⍵}substrings
}
```

## 📝 解释

Palindromic Substrings 的 APL 解决方案。使用反转 (⌽) 翻转数组元素。使用 tally (≢) 计算数组长度。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n²)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #647](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
