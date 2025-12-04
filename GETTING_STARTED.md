# 🚀 快速開始指南

## 📁 專案已完成！

你的 LeetCode APL Solutions 專案已經建立完成，包含：

### ✅ 已完成項目

1. **基礎架構**
   - ✅ 響應式網頁介面
   - ✅ 7 種語言支援（繁中、簡中、英文、日文、西班牙文、德文、法文）
   - ✅ 模組化題目結構（每題獨立檔案）
   - ✅ GitHub Pages 自動部署配置

2. **核心功能**
   - ✅ 即時搜尋
   - ✅ 難度篩選
   - ✅ 語言切換
   - ✅ 統計儀表板
   - ✅ 摺疊式題目卡片

3. **範例題目**（3 題）
   - ✅ #1 Two Sum（兩數之和）
   - ✅ #136 Single Number（只出現一次的數字）
   - ✅ #206 Reverse Linked List（反轉鏈結串列）

4. **完整文檔**
   - ✅ README（4 種語言版本）
   - ✅ 專案總結（PROJECT_SUMMARY.md）
   - ✅ MIT 授權
   - ✅ .gitignore

## 🌐 查看網站

### 方法 1: 直接開啟
```bash
open index.html
```

### 方法 2: 本地伺服器
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js
npx http-server

# 然後訪問: http://localhost:8000
```

## 📤 部署到 GitHub Pages

### 步驟 1: 建立 GitHub 儲存庫
```bash
# 在 GitHub 上建立新儲存庫，然後：
git remote add origin https://github.com/wmh/leetcode-apl-solutions.git
git push -u origin main
```

### 步驟 2: 啟用 GitHub Pages
1. 進入 GitHub 儲存庫設定
2. 找到「Pages」選項
3. Source 選擇「GitHub Actions」
4. 推送程式碼後會自動部署

### 步驟 3: 訪問網站
```
https://wmh.github.io/leetcode-apl-solutions/
```

## ➕ 新增更多題目

### 快速新增單一題目

1. 在 `problems/` 建立新檔案：
```bash
# 例如新增第 70 題
cat > problems/070-climbing-stairs.json << 'EOF'
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
  "aplSolution": "ClimbStairs ← {\n    ⍝ Your APL code here\n}",
  "explanation": {
    "en": "Explanation...",
    "zh-TW": "說明...",
    "zh-CN": "说明...",
    "ja": "説明...",
    "es": "Explicación...",
    "de": "Erklärung...",
    "fr": "Explication..."
  },
  "timeComplexity": "O(n)",
  "spaceComplexity": "O(1)"
}
EOF
```

2. 更新 `problems/index.json`：
```json
{
  "number": 70,
  "file": "070-climbing-stairs.json"
}
```

### 批量生成題目範本

可以使用提供的生成器腳本：
```bash
# Python 版本
python3 generate_problems.py

# Bash 版本
./generate_problems_batch.sh
```

## 🎨 自定義設計

### 修改顏色主題
編輯 `index.html` 中的 CSS 變數：
```css
/* 主要漸層 */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* 重點顏色 */
color: #667eea;
```

### 新增語言支援
1. 編輯 `i18n.js`
2. 新增語言配置
3. 在每個題目的 JSON 中新增對應翻譯

## 📊 專案統計

```bash
# 查看題目數量
ls problems/*.json | wc -l

# 查看程式碼行數
find . -name "*.js" -o -name "*.html" -o -name "*.json" | xargs wc -l

# 查看支援的語言
grep -o '"[a-z-]*":' i18n.js | sort -u
```

## 🐛 問題排查

### 題目無法載入
1. 檢查 `problems/index.json` 格式是否正確
2. 確認檔案名稱與 index.json 中的一致
3. 檢查 JSON 格式是否有效（使用 JSONLint）

### 語言切換無效
1. 確認瀏覽器 LocalStorage 已啟用
2. 清除瀏覽器快取
3. 檢查 i18n.js 是否正確載入

### GitHub Pages 無法訪問
1. 確認儲存庫設定中 Pages 已啟用
2. 檢查 `.github/workflows/pages.yml` 配置
3. 查看 Actions 執行日誌

## 📚 下一步

### 推薦任務
1. 新增更多經典題目（目標 100+）
2. 完善每題的 APL 解法
3. 新增測試用例
4. 改進 UI/UX
5. 新增題目分類
6. 建立搜尋引擎最佳化（SEO）

### 進階功能
- 新增個人進度追蹤
- 實作題目收藏功能
- 整合 APL 線上執行器
- 新增社群評論系統
- 建立 API 端點

## 🤝 貢獻

歡迎貢獻！請參考：
- `README.md` - 專案介紹
- `PROJECT_SUMMARY.md` - 專案架構
- `CONTRIBUTING.md`（待建立）- 貢獻指南

## 📧 需要幫助？

- 查看 Issues: https://github.com/wmh/leetcode-apl-solutions/issues
- 提交 Bug 報告
- 建議新功能

---

**祝你編碼愉快！** 🎉

使用 APL 解題，體驗最簡潔優雅的程式語言！
