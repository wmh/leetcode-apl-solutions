# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

如果在將所有大寫字符轉換為小寫字符並移除所有非字母數字字符之後，短語正著讀和反著讀都一樣，則該短語是一個回文串。字母數字字符包括字母和數字。給你一個字符串 s，如果它是回文串，返回 true；否則，返回 false。

## 💡 APL 解法

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D,⎕C⎕A)/⍵ ⋄ s≡⌽s}

⍝ Example usage:
⍝ IsPalindrome 'A man, a plan, a canal: Panama'    → 1
⍝ IsPalindrome 'race a car'                        → 0
⍝ IsPalindrome ' '                                 → 1
```

## 📝 解释

過濾以僅保留字母數字字符：大寫 (⎕A)、數字 (⎕D) 和小寫 (⎕C⎕A)。然後檢查過濾後的字符串是否與其反轉匹配 (s≡⌽s)。

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
