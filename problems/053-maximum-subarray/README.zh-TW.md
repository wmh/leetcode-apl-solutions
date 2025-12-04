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

Maximum Subarray 的 APL 解決方案。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用掃描 (\) 計算運行操作：+\ 是運行和，×\ 是運行積，⌈\ 是運行最大值，⌊\ 是運行最小值。實現使用 APL 的面向陣列原語進行簡潔表達。

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
