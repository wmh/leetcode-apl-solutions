# 739. Daily Temperatures

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目739] Find how many days until warmer temperature....

## 💡 APL 解法

```apl
DailyTemperatures ← {
    n←≢⍵
    result←n⍴0
    {result[⍵]←⊃⍸⍵<⍵↓⍵}¨⍳n
    result
}
```

## 📝 解释

Daily Temperatures 的 APL 解决方案。使用 where (⍸) 查找真值/非零元素的索引。使用 tally (≢) 计算数组长度。使用 iota (⍳) 生成索引范围或查找元素位置。使用封闭 (⊂) 包装元素或展开 (⊃) 解包/提取。实现使用 APL 的面向数组原语进行简洁表达。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n²)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #739](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
