# 128. Longest Consecutive Sequence

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目128] Find the length of the longest consecutive element...

## 💡 APL 解法

```apl
LongestConsecutive ← {
    ⍝ Find longest run
    sorted ← ∪⍵[⍋⍵]
    max ← ⌈/1,+/¨2=/¨1↓¨⊆sorted
    max
}
```

## 📝 解釋

Longest Consecutive Sequence 的 APL 解決方案。使用等級 (⍋/⍒) 排序 - 返回將對陣列排序的索引。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 unique (∪) 去除重複元素。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*log(n))`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #128](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
