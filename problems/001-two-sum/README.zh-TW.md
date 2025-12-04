# 1. Two Sum

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

給定一個整數陣列 nums 和一個整數目標值 target，請你在該陣列中找出和為目標值 target 的那兩個整數，並返回它們的陣列下標。你可以假設每種輸入只會對應一個答案。但是，陣列中同一個元素在答案裡不能重複出現。你可以按任意順序返回答案。

## 💡 APL 解法

```apl
TwoSum ← {(⊃⍸⍺=+/∘.,⍨⍵)}
```

## 📝 解釋

Two Sum 的 APL 解決方案。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 where (⍸) 查找真值/非零元素的索引。使用封閉 (⊂) 包裝元素或展開 (⊃) 解包/提取。實現使用 APL 的面向陣列原語進行簡潔表達。

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
