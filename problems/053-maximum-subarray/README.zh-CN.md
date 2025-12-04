# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 难度: Medium

## 题目

給定一個整數數組 nums，找到一個具有最大和的連續子數組（子數組最少包含一個元素），返回其最大和。

## 💡 APL 解法

```apl
MaxSubArray ← {⌈/+\0⌈⍵-+\0,⍨⌊\+\⍵}

⍝ Simpler Kadane's algorithm:
MaxSubArray2 ← {⌈/{⌈/+\⍵}¨↓∘.,⍨⍳≢⍵}

⍝ Most readable:
MaxSubArray3 ← {⌈/⌈\0,+\⍵}

⍝ Example usage:
⍝ MaxSubArray3 ¯2 1 ¯3 4 ¯1 2 1 ¯5 4    → 6
⍝ MaxSubArray3 1                        → 1
⍝ MaxSubArray3 5 4 ¯1 7 8               → 23
```

## 📝 解释

使用 Kadane 算法。版本 3 最簡單：累積和與運行最大值 (⌈\)，前置 0 以處理全負數數組。取運行最大和的最大值。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
