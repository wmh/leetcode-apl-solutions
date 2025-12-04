# 238. Product of Array Except Self

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目238] Return an array where each element is the product ...

## 💡 APL 解法

```apl
ProductExceptSelf ← {
    ⍝ Multiply all except current
    n ← ≢⍵
    result ← ×/¨⍵~¨⍵
    result
}
```

## 📝 解釋

Product of Array Except Self 的 APL 解決方案。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 tally (≢) 計算陣列長度。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n²)`
- **空間複雜度**: `O(n)`

---

## 📚 資源

- [LeetCode Problem #238](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
