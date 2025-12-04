# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

如果在將所有大寫字符轉換為小寫字符並移除所有非字母數字字符之後，短語正著讀和反著讀都一樣，則該短語是一個回文串。字母數字字符包括字母和數字。給你一個字符串 s，如果它是回文串，返回 true；否則，返回 false。

## 💡 APL 解法

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D)/⍵ ⋄ s≡⌽s}
```

## 📝 解释

Valid Palindrome 的 APL 解决方案。使用反转 (⌽) 翻转数组元素。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #125](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
