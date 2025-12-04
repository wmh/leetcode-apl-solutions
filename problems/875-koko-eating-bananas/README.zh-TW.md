# 875. Koko Eating Bananas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

## 🟡 難度: Medium

## 題目

[題目875] Find minimum eating speed to finish all bananas in...

## 💡 APL 解法

```apl
MinEatingSpeed ← {
    h←⍺
    speeds←1+⍳⌈/⍵
    ⊃speeds/⍨h≥+/⌈⍵÷⍤1⊢speeds
}
```

## 📝 解釋

Koko Eating Bananas 的 APL 解決方案。使用歸約 (/) 聚合值：+/ 求和，×/ 相乘，⌈/ 找最大值，⌊/ 找最小值。使用 iota (⍳) 生成索引範圍或查找元素位置。使用封閉 (⊂) 包裝元素或展開 (⊃) 解包/提取。實現使用 APL 的面向陣列原語進行簡潔表達。

## ⏱️ 複雜度分析

- **時間複雜度**: `O(n*log(max))`
- **空間複雜度**: `O(1)`

---

## 📚 資源

- [LeetCode Problem #875](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.zh-TW.md)
