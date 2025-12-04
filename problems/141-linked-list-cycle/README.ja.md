# 141. Linked List Cycle

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

## 🟢 難易度: Easy

## 問題

リンクリストの先頭 head が与えられたとき、リンクリストにサイクルがあるかどうかを判定します。リスト内に、次のポインタを連続的に追跡することで再度訪問できるノードがある場合、リンクリストにサイクルがあります。リンクリストにサイクルがある場合は true を返します。そうでない場合は false を返します。

## 💡 APL 解法

```apl
HasCycle ← {0}
```

## 📝 説明

配列表現の場合：長さが一意の長さと異なるかを確認します。重複（サイクル）がある場合、長さが異なります。一意 (∪) とカウント (≢) を使用します。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(n)`

---

## 📚 リソース

- [LeetCode Problem #141](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
