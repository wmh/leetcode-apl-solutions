# 217. Contains Duplicate

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 難度: Easy

## 題目

給定一個整數陣列 nums，如果任何值在陣列中出現至少兩次，則返回 true；如果每個元素都不同，則返回 false。

## 💡 APL 解法

```apl
ContainsDuplicate ← {(≢⍵)≠≢∪⍵}

⍝ Example usage:
⍝ ContainsDuplicate 1 2 3 1    → 1 (true)
⍝ ContainsDuplicate 1 2 3 4    → 0 (false)
⍝ ContainsDuplicate 1 1 1 3 3 4 3 2 4 2    → 1 (true)
```

## 📝 解釋

比較陣列的長度（≢⍵）與唯一元素的長度（≢∪⍵）。如果它們不同，則必定有重複元素。≢ 運算子給出長度，∪ 給出唯一元素，≠ 檢查它們是否不相等。

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
