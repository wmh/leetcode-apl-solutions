# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ Back to Problems](../../README.md)

---

> ⚠️ **Unvalidated Code**: This APL solution has not been tested in an actual interpreter. It may contain errors.

## 🟢 Difficulty: Easy

## Problem

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## 💡 APL Solution

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}

⍝ Example usage:
⍝ MaxProfit 7 1 5 3 6 4    → 5
⍝ MaxProfit 7 6 4 3 1      → 0
```

## 📝 Explanation

Tracks running minimum with scan (⌊\⍵). Subtracts minimum from each price (⍵-⌊\⍵) to get profit at each point. Takes maximum with ⌈/ and compares with 0 to handle no-profit case.

## ⏱️ Complexity Analysis

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

## 📚 Resources

- [LeetCode Problem #121](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.md)
