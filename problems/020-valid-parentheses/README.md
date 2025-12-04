# 20. Valid Parentheses

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

## 💡 APL Solution

```apl
ValidParentheses ← {
    ⍝ Simple balance check for single type
    0=+/('('=⍵)-')'=⍵
}

⍝ For full validation with multiple types:
ValidParentheses2 ← {
    pairs←'()' '[]' '{}'
    stack←⍬
    valid←1
    {valid∧←ProcessChar ⍵}¨⍵
    valid∧0=≢stack
}

⍝ Example usage:
⍝ ValidParentheses '()'        → 1
⍝ ValidParentheses '()[]{}'    → 1
⍝ ValidParentheses '(]'        → 0
```

## 📝 Explanation

For simple case (version 1): counts opening parens '(' and subtracts closing parens ')'. Valid if sum is 0. For full validation (version 2): would need stack-based matching of bracket pairs.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

---

## 📚 Resources

- [LeetCode Problem #20](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
