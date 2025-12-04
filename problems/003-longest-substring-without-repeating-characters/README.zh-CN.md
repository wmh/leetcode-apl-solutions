# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 难度: Medium

## 题目

給定一個字符串 s，請你找出其中不含有重複字符的最長子串的長度。

## 💡 APL 解法

```apl
LengthOfLongestSubstring ← {⌈/≢¨{⍵↑⍨¯1+1⍳⍨(⊂⊃⌽⍵)∊¨,\⍵}⍣≡¨,¨⍵}

⍝ Simpler approach - check all substrings:
LengthOfLongestSubstring2 ← {⌈/{(≢⍵)=≢∪⍵:≢⍵ ⋄ 0}¨{⍵↑¨⍺↓¨⊂⍵}⍨/⍳¨2⍴≢⍵}

⍝ Example usage:
⍝ LengthOfLongestSubstring2 'abcabcbb'    → 3
⍝ LengthOfLongestSubstring2 'bbbbb'      → 1
⍝ LengthOfLongestSubstring2 'pwwkew'     → 3
```

## 📝 解释

版本 2：生成所有子字符串，檢查每個是否唯一 ((≢⍵)=≢∪⍵)，返回最大長度。使用嵌套的 drop/take 創建子字符串。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n²)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #3](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
