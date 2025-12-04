# 3. Longest Substring Without Repeating Characters

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟡 Difficulty: Medium

## Problem

Given a string s, find the length of the longest substring without repeating characters.

## 💡 APL Solution

```apl
LengthOfLongestSubstring ← {⌈/≢¨{⍵↑⍨¯1+1⍳⍨(⊂⊃⌽⍵)∊¨,\⍵}⍣≡¨,¨⍵}

⍝ Simpler approach - check all substrings:
LengthOfLongestSubstring2 ← {⌈/{(≢⍵)=≢∪⍵:≢⍵ ⋄ 0}¨{⍵↑¨⍺↓¨⊂⍵}⍨/⍳¨2⍴≢⍵}

⍝ Example usage:
⍝ LengthOfLongestSubstring2 'abcabcbb'    → 3
⍝ LengthOfLongestSubstring2 'bbbbb'      → 1
⍝ LengthOfLongestSubstring2 'pwwkew'     → 3
```

## 📝 Explanation

Version 2: Generates all substrings, checks each for uniqueness ((≢⍵)=≢∪⍵), returns max length. Uses nested drops/takes to create substrings.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #3](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
