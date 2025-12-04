# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

給定一個整數陣列 nums，找到一個具有最大和的連續子陣列（子陣列最少包含一個元素），返回其最大和。

## 💡 APL 解法

```apl
MaxSubArray ← {⌈/+\0⌈⍵}
```

## 📝 解釋

使用 Kadane 算法。版本 3 最簡單：累積和與運行最大值 (⌈\)，前置 0 以處理全負數陣列。取運行最大和的最大值。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #53](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
