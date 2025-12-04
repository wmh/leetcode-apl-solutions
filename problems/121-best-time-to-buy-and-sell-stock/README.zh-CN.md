# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟢 难度: Easy

## 题目

給定一個數組 prices，它的第 i 個元素 prices[i] 表示一支給定股票第 i 天的價格。你只能選擇某一天買入這只股票，並選擇在未來的某一個不同的日子賣出該股票。設計一個算法來計算你所能獲取的最大利潤。返回你可以從這筆交易中獲取的最大利潤。如果你不能獲取任何利潤，返回 0。

## 💡 APL 解法

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}
```

## 📝 解释

Best Time to Buy and Sell Stock 的 APL 解决方案。使用归约 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用扫描 (\) 计算运行操作：+\ 是运行和，×\ 是运行积，⌈\ 是运行最大值，⌊\ 是运行最小值。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #121](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
