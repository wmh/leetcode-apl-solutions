# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟢 難度: Easy

## 題目

給定一個整數陣列 nums 和一個整數目標值 target，請你在該陣列中找出和為目標值 target 的那兩個整數，並返回它們的陣列下標。你可以假設每種輸入只會對應一個答案。但是，陣列中同一個元素在答案裡不能重複出現。你可以按任意順序返回答案。

## 💡 APL 解法

```apl
TwoSum ← {target←⍺ ⋄ arr←⍵ ⋄ sums←arr∘.+arr ⋄ mask←(sums=target)∧(∘.≠⍨⍳≢arr) ⋄ 2↑⍸mask}

⍝ Example usage:
⍝ 9 TwoSum 2 7 11 15    → 0 1
⍝ 6 TwoSum 3 2 4        → 1 2
⍝ 6 TwoSum 3 3          → 0 1
```

## 📝 解釋

創建陣列與自身的外積 (∘.+) 以獲得所有可能的和。使用遮罩排除相同索引的配對 (∘.≠⍨⍳≢arr)。用 ⍸ 找到和等於目標的位置。用 2↑ 取前 2 個索引。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n²)`
- **空間複雜度**: `O(n²)`

---

## 📚 資源

- [LeetCode Problem #1](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
