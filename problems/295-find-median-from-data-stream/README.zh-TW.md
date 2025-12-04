# 295. Find Median from Data Stream

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🔴 難度: Hard

## 題目

[題目295] Find median from data stream....

## 💡 APL 解法

```apl
FindMedian ← {
    sorted←⍵[⍋⍵]
    n←≢sorted
    2|n:sorted[⌊n÷2]
    +⌿sorted[(n÷2)+¯1 0]÷2
}
```

## 📝 解釋

Maintains sorted order and computes median....

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*log(n))`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #295](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
