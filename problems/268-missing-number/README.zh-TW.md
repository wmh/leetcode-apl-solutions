# 268. Missing Number

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

給定一個包含 n 個不同數字的陣列 nums，範圍是 [0, n]，返回範圍內缺失的唯一數字。

## 💡 APL 解法

```apl
MissingNumber ← {⊃(⍳1+⌈/⍵)~⍵}
```

## 📝 解釋

使用 0 到 n 的和公式：n×(n+1)÷2。計算期望和減去實際和。結果就是缺失的數字。(≢⍵) 給出 n，所以我們計算 n×(n+1)÷2 - (+/⍵)，其中 +/⍵ 是元素的和。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #268](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
