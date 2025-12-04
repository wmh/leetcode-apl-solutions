# 48. Rotate Image

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

Rotate NxN matrix 90 degrees clockwise

## 💡 APL 解法

```apl
Rotate ← {⌽⍉⍵}
```

## 📝 解释

Rotate Image 的 APL 解决方案。使用反转 (⌽) 翻转数组元素。使用转置 (⍉) 交换矩阵行和列。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n²)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #48](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
