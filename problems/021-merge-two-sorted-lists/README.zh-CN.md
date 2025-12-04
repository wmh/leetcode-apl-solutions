# 21. Merge Two Sorted Lists

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

將兩個升序鏈表合併為一個新的升序鏈表並返回。新鏈表是通過拼接給定的兩個鏈表的所有節點組成的。

## 💡 APL 解法

```apl
MergeTwoLists ← {⍺[⍋⍺,⍵],⍵[⍋⍺,⍵]}

⍝ Simpler version:
MergeTwoLists2 ← {(⍺,⍵)[⍋⍺,⍵]}

⍝ Example usage:
⍝ 1 2 4 MergeTwoLists2 1 3 4    → 1 1 2 3 4 4
⍝ ⍬ MergeTwoLists2 0            → 0
⍝ ⍬ MergeTwoLists2 ⍬            → ⍬
```

## 📝 解释

連接兩個列表 (⍺,⍵) 然後按升序排序 (⍋)。升序返回將數組排序的索引。版本 2 更清晰：連接然後按排序位置索引。

## ⏱️ 复杂度分析

- **时间复杂度**: `O((n+m)*log(n+m))`
- **空间复杂度**: `O(n+m)`

---

## 📚 资源

- [LeetCode Problem #21](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
