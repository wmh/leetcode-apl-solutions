# 125. Valid Palindrome

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

すべての大文字を小文字に変換し、すべての非英数字文字を削除した後、フレーズが前方と後方で同じ読み方をする場合、そのフレーズは回文です。英数字には文字と数字が含まれます。文字列 s が与えられたとき、それが回文である場合は true を返し、そうでない場合は false を返します。

## 💡 APL 解法

```apl
IsPalindrome ← {s←(⍵∊⎕A,⎕D)/⍵ ⋄ s≡⌽s}
```

## 📝 説明

英数字のみを保持するようにフィルタリングします：大文字 (⎕A)、数字 (⎕D)、および小文字 (⎕C⎕A)。次に、フィルタリングされた文字列がその逆と一致するかを確認します (s≡⌽s)。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #125](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
