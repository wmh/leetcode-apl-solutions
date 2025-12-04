# 853. Car Fleet

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟡 難易度: Medium

## 問題

[問題853] Count number of car fleets that will arrive at des...

## 💡 APL 解法

```apl
CarFleet ← {
    sorted←⍵[⍒⍵[;1]]
    times←(⍺-sorted[;1])÷sorted[;2]
    1+≢⍸times>⌈\times
}
```

## 📝 説明

Sorts by position and calculates arrival times....

## ⏱️ 複雑度分析

- **時間計算量**: `O(n*log(n))`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #853](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
