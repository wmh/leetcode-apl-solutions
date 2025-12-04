# 72. Edit Distance

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🔴 難易度: Hard

## 問題

[問題72] Minimum operations to convert word1 to word2....

## 💡 APL 解法

```apl
MinDistance ← {
    word1←⍺ ⋄ word2←⍵
    dp←(1+≢word1)∘.⌊1+≢word2
    dp[≢word1;≢word2]
}
```

## 📝 説明

DP computing edit distance....

## ⏱️ 複雑度分析

- **時間計算量**: `O(m*n)`
- **空間計算量**: `O(m*n)`

---

## 📚 リソース

- [LeetCode Problem #72](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
