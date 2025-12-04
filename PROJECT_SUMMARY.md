# LeetCode APL Solutions - 專案總結

## 📦 專案結構

```
leetcode-apl-solutions/
├── index.html                 # 主頁面（支援7種語言）
├── i18n.js                   # 國際化配置
├── js/
│   └── app.js                # 主應用邏輯（動態載入題目）
├── problems/                  # 題目目錄（模組化設計）
│   ├── index.json            # 題目索引（100+題）
│   ├── 001-two-sum.json      # 第1題：兩數之和
│   ├── 136-single-number.json # 第136題：只出現一次的數字
│   ├── 206-reverse-list.json # 第206題：反轉鏈結串列
│   └── ...                   # 更多題目（每題獨立檔案）
├── README.md                  # 英文說明文件
├── README.zh-TW.md           # 繁體中文說明文件
├── README.zh-CN.md           # 簡體中文說明文件
├── README.ja.md              # 日文說明文件
├── LICENSE                    # MIT 授權
├── .gitignore                # Git 忽略設定
└── .github/
    └── workflows/
        └── pages.yml         # GitHub Pages 自動部署

```

## 🌍 支援語言

1. **繁體中文** (zh-TW) - 預設語言
2. **簡體中文** (zh-CN)
3. **英文** (en)
4. **日文** (ja)
5. **西班牙文** (es)
6. **德文** (de)
7. **法文** (fr)

## ✨ 核心功能

### 1. 模組化題目設計
- 每個題目獨立一個 JSON 檔案
- 避免單一檔案過大問題
- 易於維護和擴展
- 支援動態載入

### 2. 多語言支援
- 完整的 7 種語言翻譯
- 題目描述、解法說明均支援多語言
- 自動儲存語言偏好
- 即時切換無需重新載入

### 3. 題目資料結構
```json
{
  "number": 1,
  "title": "Two Sum",
  "difficulty": "easy|medium|hard",
  "description": {
    "en": "...",
    "zh-TW": "...",
    "zh-CN": "...",
    "ja": "...",
    "es": "...",
    "de": "...",
    "fr": "..."
  },
  "aplSolution": "APL code",
  "explanation": {
    "en": "...",
    ...
  },
  "timeComplexity": "O(n)",
  "spaceComplexity": "O(1)"
}
```

### 4. 使用者介面功能
- ✅ 即時搜尋（按題號或標題）
- ✅ 難度篩選（簡單/中等/困難）
- ✅ 統計資訊顯示
- ✅ 摺疊式題目卡片
- ✅ 響應式設計（支援手機、平板、桌面）
- ✅ 深色程式碼主題
- ✅ 平滑動畫效果

## 📝 題目檔案命名規範

格式：`{number}-{slug}.json`

範例：
- `001-two-sum.json`
- `136-single-number.json`
- `206-reverse-list.json`

## 🚀 如何新增題目

### 步驟 1: 建立題目檔案
在 `problems/` 目錄下建立新檔案，例如 `problems/070-climbing-stairs.json`

### 步驟 2: 填寫題目資料
```json
{
  "number": 70,
  "title": "Climbing Stairs",
  "difficulty": "easy",
  "description": {
    "en": "You are climbing a staircase...",
    "zh-TW": "假設你正在爬樓梯...",
    "zh-CN": "假设你正在爬楼梯...",
    "ja": "階段を登っています...",
    "es": "Estás subiendo una escalera...",
    "de": "Sie klettern eine Treppe hinauf...",
    "fr": "Vous montez un escalier..."
  },
  "aplSolution": "ClimbStairs ← {...}",
  "explanation": {
    "en": "Dynamic programming approach...",
    ...
  },
  "timeComplexity": "O(n)",
  "spaceComplexity": "O(1)"
}
```

### 步驟 3: 更新索引
在 `problems/index.json` 中新增：
```json
{
  "number": 70,
  "file": "070-climbing-stairs.json"
}
```

### 步驟 4: 測試
1. 開啟 `index.html`
2. 檢查題目是否正確載入
3. 測試所有語言切換
4. 確認搜尋和篩選功能

## 🎨 設計特色

### 視覺設計
- 漸層背景（紫色系）
- 卡片式設計
- 懸浮效果
- 平滑動畫
- 深色程式碼區塊

### 互動設計
- 點擊展開/收合
- 即時搜尋回饋
- 篩選按鈕狀態
- 語言切換即時更新

## 📊 目前進度

- ✅ 基礎架構完成
- ✅ 7 種語言支援
- ✅ 3 個範例題目
- ✅ 完整文檔
- ✅ GitHub Pages 部署設定
- 🔄 待擴充至 100+ 題目

## 🔧 技術細節

### 前端技術
- 純 HTML5 / CSS3 / JavaScript
- 無需框架或建置工具
- 支援現代瀏覽器
- 離線可用（靜態檔案）

### 效能最佳化
- 按需載入題目
- 輕量級架構
- 快取語言偏好
- 最小化網路請求

### 相容性
- Chrome / Edge (最新版)
- Firefox (最新版)
- Safari 14+
- 行動裝置瀏覽器

## 🎯 下一步計劃

### 短期目標
1. 新增更多經典題目（目標：100+）
2. 補充每題的詳細解析
3. 新增測試用例展示
4. 完善 APL 語法高亮

### 中期目標
1. 新增題目分類（陣列、字串、樹等）
2. 新增難度進度追蹤
3. 新增個人收藏功能
4. 新增題目標籤系統

### 長期目標
1. 支援更多程式語言對照
2. 新增互動式 APL 執行器
3. 建立社群貢獻平台
4. 新增影片教學連結

## 📚 參考資源

- [APL Wiki](https://aplwiki.com/)
- [Dyalog APL](https://www.dyalog.com/)
- [LeetCode](https://leetcode.com/)
- [Try APL](https://tryapl.org/)

## 🤝 貢獻指南

1. Fork 專案
2. 建立功能分支
3. 新增/修改題目
4. 確保所有語言翻譯完整
5. 測試功能
6. 提交 Pull Request

## 📄 授權

MIT License - 詳見 LICENSE 檔案

---

**專案維護者**: 歡迎 Star ⭐ 和貢獻！
