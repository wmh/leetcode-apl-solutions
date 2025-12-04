# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

給你 n 個非負整數 a1，a2，...，an，每個數代表坐標中的一個點 (i, ai)。在坐標內畫 n 條垂直線，垂直線 i 的兩個端點分別為 (i, ai) 和 (i, 0)。找出其中的兩條線，使得它們與 x 軸共同構成的容器可以容納最多的水。返回容器可以儲存的最大水量。

## 💡 APL 解法

```apl
MaxArea ← {⌈/,((⍵∘.⌊⍵)×(⍳≢⍵)∘.-⍳≢⍵)}
```

## 📝 解釋

Container With Most Water 的 APL 解決方案。使用外積 (∘.) 創建所有配對組合的矩陣。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 tally (≢) 計算陣列長度。使用 iota (⍳) 生成索引範圍或查找元素位置。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n²)`
- **空間複雜度**: `O(n²)`

---

## 📚 資源

- [LeetCode Problem #11](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
