# 53. Maximum Subarray

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

給定一個整數數組 nums，找到一個具有最大和的連續子數組（子數組最少包含一個元素），返回其最大和。

## 💡 APL 解法

```apl
MaxSubArray ← {⌈/+\0⌈⍵}
```

## 📝 解释

Maximum Subarray 的 APL 解决方案。使用归约 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用扫描 (\) 计算运行操作：+\ 是运行和，×\ 是运行积，⌈\ 是运行最大值，⌊\ 是运行最小值。实现使用 APL 的面向数组原语进行简洁表达。

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
