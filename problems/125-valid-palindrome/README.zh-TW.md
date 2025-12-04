# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

如果在將所有大寫字元轉換為小寫字元並移除所有非字母數字字元之後，短語正著讀和反著讀都一樣，則該短語是一個迴文串。字母數字字元包括字母和數字。給你一個字串 s，如果它是迴文串，返回 true；否則，返回 false。

## 💡 APL 解法

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D)/⍵ ⋄ s≡⌽s}
```

## 📝 解釋

Valid Palindrome 的 APL 解決方案。使用反轉 (⌽) 翻轉陣列元素。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #125](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
