# 128. Longest Consecutive Sequence

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

[問題128] Find the length of the longest consecutive element...

## 💡 APL 解法

```apl
LongestConsecutive ← {
    ⍝ Find longest run
    sorted ← ∪⍵[⍋⍵]
    max ← ⌈/1,+/¨2=/¨1↓¨⊆sorted
    max
}
```

## 📝 説明

Sorts unique elements and finds longest consecutive run....

## ⏱️ 複雑度分析

- **時間計算量**: `O(n*log(n))`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #128](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
