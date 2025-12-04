# 853. Car Fleet

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目853] Count number of car fleets that will arrive at des...

## 💡 APL 解法

```apl
CarFleet ← {
    sorted←⍵[⍒⍵[;1]]
    times←(⍺-sorted[;1])÷sorted[;2]
    1+≢⍸times>⌈\times
}
```

## 📝 解释

Car Fleet 的 APL 解决方案。使用等级 (⍋/⍒) 排序 - 返回将对数组排序的索引。使用扫描 (\) 计算运行操作：+\ 是运行和，×\ 是运行积，⌈\ 是运行最大值，⌊\ 是运行最小值。使用 where (⍸) 查找真值/非零元素的索引。使用 tally (≢) 计算数组长度。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*log(n))`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #853](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
