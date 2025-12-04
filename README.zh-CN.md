# 🧠 LeetCode APL 题解集

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> 使用 APL (A Programming Language) 解决 LeetCode 最经典的 100+ 道题目 - 最神秘且最强大的数组编程语言之一。

> **⚠️ AI 生成内容**: 本项目由 AI 大量辅助创建。详见 [AI_GENERATED.md](./AI_GENERATED.md)。

> **🚨 重要提醒**: APL 代码**尚未在实际解释器中验证**。解决方案可能包含语法错误或不正确的实现。**[查看验证状态](VALIDATION_STATUS.md)** 了解详情。请勿在生产环境或面试中使用未经测试的代码！

**🌍 语言**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 🔥 快速链接

- 🚨 **[⚠️ 驗證狀態](VALIDATION_STATUS.md)** - **請先閱讀！**
- 📢 **[誠實聲明](HONEST_DISCLOSURE.md)** - 關於代碼質量的重要信息
- 📚 **[查看所有题目](PROBLEMS_INDEX.zh-CN.md)** - 完整题目索引
- 📖 **[如何添加题目](HOW_TO_ADD_PROBLEMS.md)** - 贡献指南
- 📁 **[项目结构](PROJECT_STRUCTURE.md)** - 详细结构说明
- 🚀 **[快速开始](QUICK_START.zh-CN.md)** - 快速上手指南

## 🎯 关于本项目

本项目展示了使用 **APL (A Programming Language)** 实现的 LeetCode 热门题目解法。APL 是一种独特的语言，以其以下特点而闻名：

- **极度简洁**: 用极少的字符表达复杂的算法
- **面向数组**: 原生支持强大的数组操作
- **数学符号**: 使用特殊的 Unicode 符号（⍵, ⍺, ⌽, ⊥, ∇ 等）
- **学习曲线陡峭**: 被认为是最难掌握的编程语言之一

### 为什么选择 APL？

APL 挑战传统编程范式，提供：
- 一种完全不同的算法思维方式
- 优雅的解决方案，往往揭示问题的数学本质
- 丰富的数组操作原语集
- 作为最早的高级语言之一的历史意义

## 📊 题目覆盖

| 难度 | 数量 | 百分比 |
|------|------|--------|
| 🟢 简单  | 40+  | ~35%   |
| 🟡 中等  | 50+  | ~50%   |
| 🔴 困难  | 15+  | ~15%   |
| **总计** | **100+** | **100%** |

## 📝 题目列表

### 📚 浏览所有题目

**➡️ [查看完整题目索引](PROBLEMS_INDEX.zh-CN.md)** - 100+ 题目完整列表，可直接访问

每道题目包含：
- 🌍 7 种语言的完整文档
- 💡 详细解释的 APL 解法
- ⏱️ 时间和空间复杂度分析
- 🔗 LeetCode 和 APL 资源链接

## 🌍 多语言支持

本仓库提供 7 种语言的文档：

| 语言 | README |
|------|--------|
| 🇬🇧 English | [README.md](README.md) |
| 🇹🇼 繁體中文 | [README.zh-TW.md](README.zh-TW.md) |
| 🇨🇳 简体中文 | [README.zh-CN.md](README.zh-CN.md) |
| 🇯🇵 日本語 | [README.ja.md](README.ja.md) |
| 🇪🇸 Español | [README.es.md](README.es.md) |
| 🇩🇪 Deutsch | [README.de.md](README.de.md) |
| 🇫🇷 Français | [README.fr.md](README.fr.md) |

`problems/` 目录中的每个题目文件也包含所有 7 种语言的描述和解释。

## 🚀 功能特点

- ✅ **100+ 经典题目**: 全面覆盖 LeetCode 最重要的题目
- ✅ **APL 解法**: 使用 APL 强大的数组操作实现的独特解法
- ✅ **详细解释**: 每个解法都包含复杂度分析和详细说明
- ✅ **多语言界面**: 可在中文、英文和日文之间切换
- ✅ **实时搜索**: 快速通过编号或名称查找题目
- ✅ **响应式设计**: 在桌面和移动设备上完美运行
- ✅ **深色代码主题**: 语法高亮的 APL 代码，提高可读性

## 📖 示例解法

### 题目 1: 两数之和

```apl
TwoSum ← {
    ⍝ ⍺: 目标和, ⍵: 数组
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}

⍝ 使用示例
target ← 9
nums ← 2 7 11 15
result ← target TwoSum nums  ⍝ 返回: 0 1
```

**解释**: 使用外积 `∘.` 生成所有可能的数对和，然后使用 `⍸` 找到匹配的索引。

- **时间复杂度**: O(n²)
- **空间复杂度**: O(n²)

### 题目 136: 只出现一次的数字

```apl
SingleNumber ← {≠/⍵}

⍝ 使用示例
nums ← 4 1 2 1 2
result ← SingleNumber nums  ⍝ 返回: 4
```

**解释**: XOR 归约 - APL 的 `≠` 是异或运算，`/` 是归约操作符。利用异或性质的优雅单行解法。

- **时间复杂度**: O(n)
- **空间复杂度**: O(1)

### 题目 206: 反转链表

```apl
ReverseList ← {⌽⍵}

⍝ 使用示例
list ← 1 2 3 4 5
result ← ReverseList list  ⍝ 返回: 5 4 3 2 1
```

**解释**: `⌽` 是 APL 的反转操作符 - 最简单的解法！

- **时间复杂度**: O(n)
- **空间复杂度**: O(1)

## 🛠️ 技术栈

- **语言**: APL (A Programming Language)
- **文档格式**: 纯 Markdown（静态）
- **数据格式**: JSON 数据 + Markdown README
- **国际化**: 7 种语言（英语、简中、繁中、日语、西班牙语、德语、法语）
- **托管**: GitHub（静态文件）

## 📂 项目结构

```
leetcode-apl-solutions/
├── problems/                    # 所有题目解法
│   ├── 001-two-sum/            # 每道题目都有独立目录
│   │   ├── README.md           # 7 种语言版本
│   │   ├── README.zh-CN.md
│   │   └── ...
│   ├── 136-single-number/
│   ├── 206-reverse-linked-list/
│   └── index.json              # 题目元数据
├── PROBLEMS_INDEX.md           # 完整题目列表（7 种语言）
├── PROBLEMS_INDEX.zh-CN.md
├── README.md                   # 主文档（7 种语言）
├── README.zh-CN.md
└── generate_static_readmes.py  # 生成器脚本
```

## 💻 如何使用

### 🌐 在 GitHub 上浏览

直接在 GitHub 上浏览本仓库！无需服务器 - 所有内容都是静态 Markdown 文件。

1. **从这里开始**: [PROBLEMS_INDEX.zh-CN.md](PROBLEMS_INDEX.zh-CN.md) - 所有题目的完整列表
2. **点击任何题目**查看包含解释的完整解法
3. **切换语言**使用每个页面顶部的导航栏

### 📥 本地克隆

```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions

# 查看完整题目列表
cat PROBLEMS_INDEX.zh-CN.md

# 浏览特定题目
cat problems/001-two-sum/README.zh-CN.md

# 查看英文版本
cat problems/001-two-sum/README.md
```

### 🔧 运行 APL 解法

要实际运行 APL 代码，你需要一个 APL 解释器：

1. **在线**（最简单）: 访问 [TryAPL.org](https://tryapl.org/)
2. **Dyalog APL**: 从 [dyalog.com](https://www.dyalog.com/download-zone.htm) 下载
3. **GNU APL**: 
   - Linux: `apt install gnu-apl`
   - macOS: `brew install gnu-apl`

### 🔄 生成更多题目

使用包含的生成器脚本创建新的题目 README：

```bash
# 将你的题目数据添加到 problems/*.json
# 然后重新生成所有 README
python3 generate_static_readmes.py
```

## 🤝 贡献

欢迎贡献！你可以通过以下方式帮助：

1. **添加更多题目**: 用 APL 实现更多 LeetCode 题目
2. **改进解法**: 优化现有的 APL 解法
3. **修复错误**: 报告并修复发现的问题
4. **翻译**: 帮助改进语言翻译
5. **文档**: 增强题目解释

### 贡献步骤

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m '添加某个特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📚 资源

### 学习 APL
- [APL Wiki](https://aplwiki.com/) - 全面的 APL 文档
- [Dyalog APL 教程](https://tutorial.dyalog.com/) - 官方 Dyalog 教程
- [APL Cart](https://aplcart.info/) - 可搜索的 APL 习语
- [Try APL](https://tryapl.org/) - 在线 APL 解释器

### LeetCode
- [LeetCode 题库](https://leetcode.cn/problemset/all/) - 官方题目列表
- [LeetCode 热门面试题](https://leetcode.cn/problem-list/top-interview-questions/)

## 📜 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- **Kenneth E. Iverson** - APL 的创造者
- **LeetCode** - 提供优秀的算法题目
- **Dyalog Ltd** - 维护和开发 APL
- **APL 社区** - 保持这门美丽语言的活力

## 📧 联系方式

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [报告问题或建议](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ Star 历史

如果你觉得这个项目有帮助，请考虑给它一个星标！⭐

---

**用 ❤️ 和大量的 ⍵, ⍺, ⌽, 和 ∇ 制作**

*"APL 是一个错误，但被完美地执行了。它是未来的语言，却用着过去的编程技术：它创造了新一代的编程废物。"* - Edsger W. Dijkstra

尽管有批评，APL 仍然是数组操作最优雅和最强大的语言之一！🎯
