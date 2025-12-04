# 🚀 快速开始

欢迎使用 LeetCode APL 解法集！本指南将帮助你快速上手。

## 📚 浏览题目

### 方式 1: 在 GitHub 上浏览（推荐）

1. **查看完整题目列表**
   - 访问 [PROBLEMS_INDEX.zh-CN.md](PROBLEMS_INDEX.zh-CN.md)
   - 浏览所有可用题目

2. **点击感兴趣的题目**
   - 每个题目都有独立的页面
   - 包含详细的 APL 解法和解释

3. **切换语言**
   - 每个页面顶部有 7 种语言选择
   - 点击即可切换

### 方式 2: 克隆到本地

```bash
# 克隆仓库
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions

# 使用你喜欢的 Markdown 阅读器
# 例如 VS Code, Typora, 或命令行工具
```

## 💡 理解 APL 解法

### APL 基础符号

| 符号 | 说明 | 示例 |
|------|------|------|
| `⍵` | 右参数 (omega) | `{⍵+1}` 表示加 1 |
| `⍺` | 左参数 (alpha) | `{⍺+⍵}` 表示相加 |
| `⌽` | 反转 | `⌽1 2 3` → `3 2 1` |
| `≠` | 异或 (XOR) | `1≠1` → `0` |
| `/` | 归约 | `+/1 2 3` → `6` |
| `⍸` | 找位置 | `⍸1 0 1` → `0 2` |

### 示例：两数之和

```apl
TwoSum ← {
    ⍝ ⍺: 目标和, ⍵: 数组
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}

⍝ 使用
9 TwoSum 2 7 11 15  ⍝ 结果: 0 1
```

**解释**:
- `∘.,⍨⍵` - 创建数组与自身的外积
- `+/` - 对每对求和
- `⍺=` - 找出等于目标的位置
- `⍸` - 获取这些位置的索引
- `2↑` - 取前两个元素

## 🔧 运行 APL 代码

### 在线运行（最简单）

1. 访问 [TryAPL.org](https://tryapl.org/)
2. 复制题目中的 APL 代码
3. 粘贴到在线编辑器
4. 按 `Ctrl+Enter` 运行

### 安装 APL 解释器

#### Dyalog APL（推荐）
```bash
# 从官网下载并安装
# https://www.dyalog.com/download-zone.htm
```

#### GNU APL
```bash
# macOS
brew install gnu-apl

# Ubuntu/Debian
sudo apt install gnu-apl

# 运行
apl
```

## 📝 题目结构

每道题目包含：

### 1. 题目描述
- 问题陈述
- 输入输出说明
- 约束条件

### 2. APL 解法
```apl
⍝ 完整的可运行代码
⍝ 包含注释说明
```

### 3. 解释
- 算法思路
- APL 特性说明
- 为什么这样写

### 4. 复杂度分析
- **时间复杂度**: O(n)
- **空间复杂度**: O(1)

### 5. 资源链接
- LeetCode 原题
- APL Wiki 文档
- 在线练习环境

## 🎯 推荐学习路径

### 第 1 周: 熟悉 APL 基础
1. 阅读 [APL Wiki](https://aplwiki.com/)
2. 在 [TryAPL.org](https://tryapl.org/) 练习基本操作
3. 学习常用符号（⍵, ⍺, ⌽, /）

### 第 2 周: 简单题目
从简单难度开始：
- [#1 - Two Sum](problems/001-two-sum/README.zh-CN.md)
- [#136 - Single Number](problems/136-single-number/README.zh-CN.md)
- [#206 - Reverse Linked List](problems/206-reverse-linked-list/README.zh-CN.md)

### 第 3-4 周: 中等题目
尝试更复杂的算法：
- 动态规划题目
- 数组操作题目
- 字符串处理题目

### 第 5+ 周: 困难题目
挑战高难度问题：
- 图算法
- 高级数据结构
- 优化问题

## 💬 常见问题

### Q: APL 代码为什么这么短？
A: APL 是为数组操作设计的，很多复杂操作都有内置的简洁表达方式。

### Q: 需要特殊键盘输入 APL 符号吗？
A: 不需要！大多数 APL 编辑器都支持键盘映射：
- Dyalog APL: 按 `` ` `` 然后按字母
- 在线编辑器: 右侧有符号面板

### Q: APL 实用吗？
A: APL 更多是学习工具，帮助理解算法的数学本质。在金融、科学计算领域有应用。

### Q: 代码有测试吗？
A: 这些是教育性质的示例代码。使用前建议在 APL 解释器中测试验证。

## 🤝 参与贡献

想要添加新题目？

1. 阅读 [HOW_TO_ADD_PROBLEMS.md](HOW_TO_ADD_PROBLEMS.md)
2. 创建题目的 JSON 文件
3. 运行生成脚本
4. 提交 Pull Request

## 📚 额外资源

### APL 学习
- [APL Wiki](https://aplwiki.com/) - 全面的文档
- [Dyalog 教程](https://tutorial.dyalog.com/) - 官方教程
- [APL Cart](https://aplcart.info/) - 代码片段搜索
- [Try APL](https://tryapl.org/) - 在线编辑器

### LeetCode 资源
- [LeetCode 中国](https://leetcode.cn/)
- [LeetCode 国际](https://leetcode.com/)
- [热门面试题](https://leetcode.cn/problemset/hot-100/)

### 社区
- [r/apljk](https://reddit.com/r/apljk) - APL Reddit 社区
- [APL Orchard](https://chat.stackexchange.com/rooms/52405/the-apl-orchard) - Stack Exchange 聊天室

## ⭐ 支持项目

如果觉得这个项目有帮助，请：
- 给仓库点个 Star ⭐
- 分享给其他人
- 提交你的 APL 解法
- 报告问题或建议

---

**开始你的 APL 学习之旅！** 🎉

从 [题目索引](PROBLEMS_INDEX.zh-CN.md) 选择一道题目开始吧！
