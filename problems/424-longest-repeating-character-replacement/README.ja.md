# 424. Longest Repeating Character Replacement

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟡 難易度: Medium

## 問題

[問題424] Find length of longest substring with same letter ...

## 💡 APL 解法

```apl
CharacterReplacement ← {
    k←⍺ ⋄ maxLen←0
    {maxLen⌈←≢⍵}¨⊆⍵
    maxLen
}
```

## 📝 説明

Slides window and counts character frequencies....

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #424](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
