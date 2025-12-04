# 141. Linked List Cycle

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給你一個鏈表的頭節點 head，判斷鏈表中是否有環。如果鏈表中有某個節點，可以通過連續跟蹤 next 指針再次到達，則鏈表中存在環。如果鏈表中存在環，則返回 true。否則，返回 false。

## 💡 APL 解法

```apl
HasCycle ← {(≢⍵)≠≢∪⍵}

⍝ For array representation: check for duplicates
⍝ Example usage:
⍝ HasCycle 3 2 0 ¯4    → 0 (no cycle)
⍝ HasCycle 1 2 1       → 1 (has cycle - 1 repeats)
```

## 📝 解释

對於數組表示：檢查長度是否與唯一長度不同。如果有重複（循環），長度會不同。使用唯一 (∪) 和計數 (≢)。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n)`
- **空间复杂度**: `O(n)`

---

## 📚 资源

- [LeetCode Problem #141](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
