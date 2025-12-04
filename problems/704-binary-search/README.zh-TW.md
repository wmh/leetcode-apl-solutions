# 704. Binary Search

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟢 難度: Easy

## 題目

[題目704] Search for target value in sorted array....

## 💡 APL 解法

```apl
BinarySearch ← {
    target←⍺
    (target∊⍵)×⊃⍸target=⍵
}
```

## 📝 解釋

Binary Search 的 APL 解決方案。使用 where (⍸) 查找真值/非零元素的索引。使用封閉 (⊂) 包裝元素或展開 (⊃) 解包/提取。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(log n)`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #704](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
