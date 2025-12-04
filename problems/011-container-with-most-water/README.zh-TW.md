# 11. Container With Most Water

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 返回題目列表](../../README.zh-TW.md)

---

> ⚠️ **未驗證程式碼**：此 APL 解決方案尚未在實際解釋器中測試，可能包含錯誤。

## 🟡 難度: Medium

## 題目

給你 n 個非負整數 a1，a2，...，an，每個數代表坐標中的一個點 (i, ai)。在坐標內畫 n 條垂直線，垂直線 i 的兩個端點分別為 (i, ai) 和 (i, 0)。找出其中的兩條線，使得它們與 x 軸共同構成的容器可以容納最多的水。返回容器可以儲存的最大水量。

## 💡 APL 解法

```apl
MaxArea ← {⌈/,((⊃⌊/¨⍵∘.,⍵)×(⊃-/¨(⍳≢⍵)∘.,⍳≢⍵))}

⍝ Simplified:
MaxArea2 ← {n←≢⍵ ⋄ ⌈/,((⍵∘.⌊⍵)×(⍳n)∘.-⍳n)}

⍝ Example usage:
⍝ MaxArea2 1 8 6 2 5 4 8 3 7    → 49
⍝ MaxArea2 1 1                  → 1
```

## 📝 解釋

創建高度的外積 (∘.⌊) 以獲得所有配對的最小高度。乘以距離 ((⍳n)∘.-⍳n) 以獲得面積。取最大值。

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
