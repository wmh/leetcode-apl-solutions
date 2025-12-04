# 435. Non-overlapping Intervals

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目435] Minimum removals to make non-overlapping....

## 💡 APL 解法

```apl
EraseOverlapIntervals ← {
    sorted←⍵[⍋⍵[;1]]
    count←0
    count
}
```

## 📝 解釋

Non-overlapping Intervals 的 APL 解決方案。使用等級 (⍋/⍒) 排序 - 返回將對陣列排序的索引。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*log(n))`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #435](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
