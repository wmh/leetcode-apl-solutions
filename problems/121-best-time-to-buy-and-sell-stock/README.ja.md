# 121. Best Time to Buy and Sell Stock

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

[⬅️ 問題リストに戻る](../../README.ja.md)

---

> ⚠️ **未検証コード**：この APL ソリューションは実際のインタープリタでテストされていません。エラーが含まれている可能性があります。

## 🟢 難易度: Easy

## 問題

配列 prices が与えられます。prices[i] は i 日目の株価を表します。1 日を選んで株を買い、将来の別の日に株を売ることで利益を最大化したいと考えています。この取引から達成できる最大利益を返します。利益が得られない場合は 0 を返します。

## 💡 APL 解法

```apl
MaxProfit ← {⌈/0,⍵-⌊\⍵}

⍝ Example usage:
⍝ MaxProfit 7 1 5 3 6 4    → 5
⍝ MaxProfit 7 6 4 3 1      → 0
```

## 📝 説明

スキャン (⌊\⍵) で実行中の最小値を追跡します。各価格から最小値を引いて (⍵-⌊\⍵) 各ポイントでの利益を取得します。⌈/ で最大値を取り、0 と比較して利益なしのケースを処理します。

## ⏱️ 複雑度分析

- **時間計算量**: `O(n)`
- **空間計算量**: `O(1)`

---

## 📚 リソース

- [LeetCode Problem #121](https://leetcode.com/problems/)
- [APL Wiki](https://aplwiki.com/)
- [Try APL Online](https://tryapl.org/)

---

**Made with ❤️ using APL** • [View All Problems](../../README.ja.md)
