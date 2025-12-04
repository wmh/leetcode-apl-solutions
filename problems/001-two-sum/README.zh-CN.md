# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回题目列表](../../README.zh-CN.md)

---

> ⚠️ **未驗證代碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 难度: Easy

## 题目

給定一個整數數組 nums 和一個整數目標值 target，請你在該數組中找出和為目標值 target 的那兩個整數，並返回它們的數組下標。你可以假設每種輸入只會對應一個答案。但是，數組中同一個元素在答案裡不能重複出現。你可以按任意順序返回答案。

## 💡 APL 解法

```apl
TwoSum ← {target←⍺ ⋄ arr←⍵ ⋄ sums←arr∘.+arr ⋄ mask←(sums=target)∧(∘.≠⍨⍳≢arr) ⋄ 2↑⍸mask}

⍝ Example usage:
⍝ 9 TwoSum 2 7 11 15    → 0 1
⍝ 6 TwoSum 3 2 4        → 1 2
⍝ 6 TwoSum 3 3          → 0 1
```

## 📝 解释

創建數組與自身的外積 (∘.+) 以獲得所有可能的和。使用掩碼排除相同索引的配對 (∘.≠⍨⍳≢arr)。用 ⍸ 找到和等於目標的位置。用 2↑ 取前 2 個索引。

## ⏱️ 复杂度分析

- **时间复杂度**: `O(n²)`
- **空间复杂度**: `O(n²)`

---

## 📚 资源

- [LeetCode Problem #1](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-CN.md)
