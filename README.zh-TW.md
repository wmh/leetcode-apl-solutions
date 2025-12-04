# 🧠 LeetCode APL 題解集

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> 使用 APL (A Programming Language) 解決 LeetCode 最經典的 100+ 道題目 - 最神秘且最強大的陣列程式語言之一。

> **⚠️ AI 生成內容**: 本專案由 AI 大量輔助建立。詳見 [AI_GENERATED.md](./AI_GENERATED.md)。APL 程式碼未在實際直譯器中測試，使用前建議驗證。

**🌍 語言**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 🎯 關於本專案

本專案展示了使用 **APL (A Programming Language)** 實現的 LeetCode 熱門題目解法。APL 是一種獨特的語言，以其以下特點而聞名：

- **極度簡潔**: 用極少的字元表達複雜的演算法
- **面向陣列**: 原生支援強大的陣列操作
- **數學符號**: 使用特殊的 Unicode 符號（⍵, ⍺, ⌽, ⊥, ∇ 等）
- **學習曲線陡峭**: 被認為是最難掌握的程式語言之一

### 為什麼選擇 APL？

APL 挑戰傳統程式設計範式，提供：
- 一種完全不同的演算法思維方式
- 優雅的解決方案，往往揭示問題的數學本質
- 豐富的陣列操作原語集
- 作為最早的高階語言之一的歷史意義

## 🌍 多語系支援

網站支援 7 種語言：
- 🇹🇼 **繁體中文**
- 🇨🇳 **簡體中文**
- 🇬🇧 **英語**
- 🇯🇵 **日語**
- 🇪🇸 **西班牙語**
- 🇩🇪 **德語**
- 🇫🇷 **法語**

語言偏好會自動儲存在瀏覽器中。

## 📂 專案結構

```
leetcode-apl-solutions/
├── index.html              # 主應用程式
├── i18n.js                 # 國際化配置（7種語言）
├── js/
│   └── app.js             # 主應用邏輯
├── problems/               # 題目檔案目錄
│   ├── index.json         # 題目索引
│   ├── 001-two-sum.json   # 第1題
│   ├── 136-single-number.json
│   ├── 206-reverse-list.json
│   └── ...                # 更多題目檔案
├── README.md              # 英文文檔
├── README.zh-TW.md        # 繁中文檔
├── README.zh-CN.md        # 簡中文檔
├── README.ja.md           # 日文文檔
└── .github/
    └── workflows/
        └── pages.yml      # GitHub Pages 部署

```

## 🚀 功能特點

- ✅ **100+ 經典題目**: 全面覆蓋 LeetCode 最重要的題目
- ✅ **APL 解法**: 使用 APL 強大的陣列操作實現的獨特解法
- ✅ **詳細解釋**: 每個解法都包含複雜度分析和詳細說明
- ✅ **7 種語言**: 支援繁中、簡中、英文、日文、西班牙文、德文、法文
- ✅ **模組化設計**: 每個題目獨立的 JSON 檔案
- ✅ **實時搜尋**: 快速通過編號或名稱查找題目
- ✅ **難度篩選**: 按簡單、中等、困難篩選
- ✅ **響應式設計**: 在桌面和行動裝置上完美執行
- ✅ **深色程式碼主題**: 語法高亮的 APL 程式碼

## 📖 題目檔案格式

每個題目都是一個獨立的 JSON 檔案，包含：

```json
{
  "number": 1,
  "title": "Two Sum",
  "difficulty": "easy",
  "description": {
    "en": "English description",
    "zh-TW": "繁體中文描述",
    "zh-CN": "简体中文描述",
    "ja": "日本語の説明",
    "es": "Descripción en español",
    "de": "Deutsche Beschreibung",
    "fr": "Description française"
  },
  "aplSolution": "APL code here",
  "explanation": {
    "en": "English explanation",
    "zh-TW": "繁體中文說明",
    ...
  },
  "timeComplexity": "O(n)",
  "spaceComplexity": "O(1)"
}
```

## 💻 本地開發

1. 複製儲存庫:
```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions
```

2. 啟動本地伺服器:
```bash
# 使用 Python
python -m http.server 8000

# 或使用 Node.js
npx http-server

# 然後訪問 http://localhost:8000
```

3. 在瀏覽器中開啟 `index.html`

## 📝 新增題目

1. 在 `problems/` 目錄下建立新的 JSON 檔案，例如 `problems/100-example.json`

2. 按照格式填寫題目資料（參考現有題目）

3. 更新 `problems/index.json`，新增題目索引：
```json
{
  "number": 100,
  "file": "100-example.json"
}
```

4. 確保所有 7 種語言的翻譯都已完成

## 🤝 貢獻

歡迎貢獻！你可以通過以下方式幫助：

1. **新增更多題目**: 用 APL 實現更多 LeetCode 題目
2. **改進解法**: 最佳化現有的 APL 解法
3. **完善翻譯**: 補充或改進各語言翻譯
4. **修復錯誤**: 報告並修復發現的問題
5. **文件**: 增強題目解釋和說明

### 貢獻步驟

1. Fork 本儲存庫
2. 建立你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m '新增某個特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

## 📚 學習資源

### 學習 APL
- [APL Wiki](https://aplwiki.com/) - 全面的 APL 文檔
- [Dyalog APL 教學](https://tutorial.dyalog.com/) - 官方 Dyalog 教學
- [APL Cart](https://aplcart.info/) - 可搜尋的 APL 習語
- [Try APL](https://tryapl.org/) - 線上 APL 解釋器
- [APL 視訊教學](https://www.youtube.com/c/Dyalog) - YouTube 教學影片

### LeetCode
- [LeetCode 題庫](https://leetcode.com/problemset/all/) - 官方題目列表
- [LeetCode 熱門面試題](https://leetcode.com/problem-list/top-interview-questions/)

## 🌐 部署到 GitHub Pages

本專案已配置自動部署到 GitHub Pages：

1. 推送程式碼到 `main` 分支
2. GitHub Actions 會自動建置和部署
3. 訪問 `https://wmh.github.io/leetcode-apl-solutions/`

## 📜 許可證

本專案採用 MIT 許可證 - 詳見 [LICENSE](LICENSE) 檔案。

## 🙏 致謝

- **Kenneth E. Iverson** - APL 的創造者
- **LeetCode** - 提供優秀的演算法題目
- **Dyalog Ltd** - 維護和開發 APL
- **APL 社群** - 保持這門美麗語言的活力
- **所有貢獻者** - 感謝每一個貢獻者的付出

## 📧 聯絡方式

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [回報問題或建議](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ Star 歷史

如果你覺得這個專案有幫助，請考慮給它一個星標！⭐

---

**用 ❤️ 和大量的 ⍵, ⍺, ⌽, 和 ∇ 製作**

*"APL 是一個錯誤，但被完美地執行了。它是未來的語言，卻用著過去的程式設計技術。"* - Edsger W. Dijkstra

儘管有批評，APL 仍然是陣列操作最優雅和最強大的語言之一！🎯
