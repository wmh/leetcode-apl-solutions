# 🧠 LeetCode APL ソリューション

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> APL (A Programming Language) を使用して LeetCode の最も古典的な 100 以上の問題を解決 - 最も難解で強力な配列プログラミング言語の 1 つ。

> **⚠️ AI 生成コンテンツ**: このプロジェクトは AI の大幅な支援により作成されました。詳細は [AI_GENERATED.md](./AI_GENERATED.md) をご覧ください。APL コードは実際のインタープリタでテストされていません。使用前の検証を推奨します。

**🌍 言語**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 🎯 このプロジェクトについて

このプロジェクトは、**APL (A Programming Language)** で実装された LeetCode の人気問題のソリューションを紹介しています。APL は、次の特徴で知られるユニークな言語です：

- **極度の簡潔さ**: 複雑なアルゴリズムを非常に少ない文字で表現
- **配列指向**: 強力な配列操作のネイティブサポート
- **数学記法**: 特殊な Unicode 記号（⍵, ⍺, ⌽, ⊥, ∇ など）を使用
- **高い学習曲線**: 習得が最も難しい言語の 1 つと考えられている

### なぜ APL なのか？

APL は従来のプログラミングパラダイムに挑戦し、以下を提供します：
- アルゴリズムについて考える完全に異なる方法
- 問題の数学的本質を明らかにする優雅なソリューション
- 配列操作のための豊富なプリミティブ操作のセット
- 最初の高級言語の 1 つとしての歴史的意義

## 📊 問題カバレッジ

| 難易度 | 数 | パーセンテージ |
|--------|-----|---------------|
| 🟢 簡単 | 40+ | ~35%          |
| 🟡 中級 | 50+ | ~50%          |
| 🔴 難しい | 15+ | ~15%        |
| **合計** | **100+** | **100%** |

## 🌍 多言語サポート

ウェブサイトは 3 つの言語をサポートしています：
- 🇨🇳 **中国語（簡体字）**
- 🇬🇧 **英語**
- 🇯🇵 **日本語**

言語設定はブラウザに自動的に保存されます。

## 🚀 機能

- ✅ **100+ 古典的な問題**: LeetCode の最も重要な問題の包括的なカバレッジ
- ✅ **APL ソリューション**: APL の強力な配列操作を使用したユニークな実装
- ✅ **詳細な説明**: 各ソリューションには計算量解析と説明が含まれています
- ✅ **多言語 UI**: 中国語、英語、日本語を切り替え可能
- ✅ **リアルタイム検索**: 番号または名前で問題をすばやく検索
- ✅ **レスポンシブデザイン**: デスクトップとモバイルデバイスで完璧に動作
- ✅ **ダークコードテーマ**: 読みやすさを向上させる構文強調表示された APL コード

## 📖 ソリューション例

### 問題 1: Two Sum

```apl
TwoSum ← {
    ⍝ ⍺: target sum, ⍵: array
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}

⍝ 使用例
target ← 9
nums ← 2 7 11 15
result ← target TwoSum nums  ⍝ 結果: 0 1
```

**説明**: 外積 `∘.` を使用してすべての可能なペア和を生成し、`⍸` を使用して一致するインデックスを見つけます。

- **時間計算量**: O(n²)
- **空間計算量**: O(n²)

### 問題 136: Single Number

```apl
SingleNumber ← {≠/⍵}

⍝ 使用例
nums ← 4 1 2 1 2
result ← SingleNumber nums  ⍝ 結果: 4
```

**説明**: XOR リデュース - APL の `≠` は XOR、`/` はリデュースです。XOR プロパティを活用したエレガントなワンライナー。

- **時間計算量**: O(n)
- **空間計算量**: O(1)

### 問題 206: Reverse Linked List

```apl
ReverseList ← {⌽⍵}

⍝ 使用例
list ← 1 2 3 4 5
result ← ReverseList list  ⍝ 結果: 5 4 3 2 1
```

**説明**: `⌽` は APL の反転演算子 - 最もシンプルなソリューション！

- **時間計算量**: O(n)
- **空間計算量**: O(1)

## 🛠️ テクノロジースタック

- **言語**: APL (A Programming Language)
- **フロントエンド**: バニラ JavaScript, HTML5, CSS3
- **スタイリング**: グラデーションテーマのカスタム CSS
- **i18n**: カスタム国際化システム
- **ホスティング**: GitHub Pages

## 🌐 ライブデモ

ライブウェブサイトを訪問: **[LeetCode APL ソリューション](https://wmh.github.io/leetcode-apl-solutions/)**

## 💻 ローカル開発

1. リポジトリをクローン:
```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions
```

2. ブラウザで `index.html` を開く:
```bash
open index.html
# または
python -m http.server 8000
# その後 http://localhost:8000 にアクセス
```

## 🤝 貢献

貢献を歓迎します！以下の方法で協力できます：

1. **問題を追加**: APL でより多くの LeetCode 問題を実装
2. **ソリューションを改善**: 既存の APL ソリューションを最適化
3. **バグ修正**: 見つけた問題を報告および修正
4. **翻訳**: 言語翻訳の改善を支援
5. **ドキュメント**: 問題の説明を強化

## 📚 リソース

### APL を学ぶ
- [APL Wiki](https://aplwiki.com/) - 包括的な APL ドキュメント
- [Dyalog APL チュートリアル](https://tutorial.dyalog.com/) - 公式 Dyalog チュートリアル
- [APL Cart](https://aplcart.info/) - 検索可能な APL イディオム
- [Try APL](https://tryapl.org/) - オンライン APL インタープリター

### LeetCode
- [LeetCode 問題](https://leetcode.com/problemset/all/) - 公式問題リスト

## 📜 ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。

## 🙏 謝辞

- **Kenneth E. Iverson** - APL の作成者
- **LeetCode** - 優れたアルゴリズム問題の提供
- **Dyalog Ltd** - APL の保守と開発
- **APL コミュニティ** - この美しい言語を維持

## 📧 連絡先

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [問題や提案を報告](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ スター履歴

このプロジェクトが役に立つと思ったら、スターを付けてください！⭐

---

**❤️ と たくさんの ⍵, ⍺, ⌽, と ∇ で作成**
