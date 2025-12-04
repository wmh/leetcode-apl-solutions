# 435. Non-overlapping Intervals

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

## 🟡 难度: Medium

## 题目

[题目435] Minimum removals to make non-overlapping....

## 💡 APL 解法

```apl
EraseOverlapIntervals ← {
    sorted←⍵[⍋⍵[;1]]
    count←0
    count
}
```

## 📝 解释

Greedy selection by end time....

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n*log(n))`
- **空间复杂度**: `O(1)`

---

## 📚 资源

- [LeetCode Problem #435](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
