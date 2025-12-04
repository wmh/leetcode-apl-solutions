# 417. Pacific Atlantic Water Flow

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目417] Find cells from which water can flow to both ocean...

## 💡 APL 解法

```apl
PacificAtlantic ← {
    ⍝ DFS from both coasts
    pacific∩atlantic
}
```

## 📝 解釋

DFS from both ocean borders....

## ⏱️ 複雜度分析

- **時間複雜度**: `O(m*n)`
- **空間複雜度**: `O(m*n)`

---

## 📚 資源

- [LeetCode Problem #417](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
