# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

給定一個整數陣列 nums，如果任何值在陣列中出現至少兩次，則返回 true；如果每個元素都不同，則返回 false。

## 💡 APL 解法

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}
```

## 📝 解釋

Contains Duplicate 的 APL 解決方案。使用 unique (∪) 去除重複元素。使用 tally (≢) 計算陣列長度。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #217](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
