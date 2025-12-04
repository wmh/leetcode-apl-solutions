# 🧠 LeetCode APL Solutions

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 173](https://img.shields.io/badge/Problems-173-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](https://en.wikipedia.org/wiki/Artificial_intelligence)

> LeetCode problems solved in APL (A Programming Language)

## ⚠️ AI-Generated Content Notice

**This project was created with AI assistance.** All APL solutions and explanations in this repository were generated using artificial intelligence. While efforts have been made to ensure code quality:

- Solutions may contain errors or non-optimal approaches
- Code has not been extensively tested in production APL interpreters
- Explanations are based on code analysis and may not reflect APL best practices
- This is primarily an educational/experimental project

**Use at your own discretion. Contributions and corrections are welcome!**

---

**🌍 Languages**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 📚 Problems

**[View All 173 Problems](PROBLEMS_INDEX.md)**

- 🟢 Easy: 70+
- 🟡 Medium: 50+  
- 🔴 Hard: 10+

## 🚀 Quick Start

```bash
# Install APL
brew install gnu-apl  # macOS
apt install gnu-apl   # Linux

# Browse solutions
cd problems/001-two-sum
cat 001-two-sum.json
```

## 📖 Documentation

- [Problem Index](PROBLEMS_INDEX.md)
- [How to Add Problems](HOW_TO_ADD_PROBLEMS.md)
- [Project Structure](PROJECT_STRUCTURE.md)

```apl
ReverseList ← {⌽⍵}
```
**Complexity**: Time O(n), Space O(1)

---

### 📂 Repository Structure

```
problems/
├── 001-two-sum/
│   ├── README.md           # English
│   ├── README.zh-CN.md     # 简体中文
│   ├── README.zh-TW.md     # 繁體中文
│   ├── README.ja.md        # 日本語
│   ├── README.es.md        # Español
│   ├── README.de.md        # Deutsch
│   └── README.fr.md        # Français
├── 136-single-number/
│   └── ... (7 language files)
└── 206-reverse-linked-list/
    └── ... (7 language files)
```

## 🌍 Multi-Language Support

This repository provides documentation in 7 languages:

| Language | README |
|----------|--------|
| 🇬🇧 English | [README.md](README.md) |
| 🇹🇼 繁體中文 | [README.zh-TW.md](README.zh-TW.md) |
| 🇨🇳 简体中文 | [README.zh-CN.md](README.zh-CN.md) |
| 🇯🇵 日本語 | [README.ja.md](README.ja.md) |
| 🇪🇸 Español | [README.es.md](README.es.md) |
| 🇩🇪 Deutsch | [README.de.md](README.de.md) |
| 🇫🇷 Français | [README.fr.md](README.fr.md) |

Each problem file in the `problems/` directory also includes descriptions and explanations in all 7 languages.

## 🚀 Features

- ✅ **100+ Classic Problems**: Comprehensive coverage of LeetCode's most important problems
- ✅ **APL Solutions**: Unique implementations using APL's powerful array operations
- ✅ **Detailed Explanations**: Each solution includes complexity analysis and explanations
- ✅ **7 Languages**: Full documentation in English, 繁中, 简中, 日本語, Español, Deutsch, Français
- ✅ **Modular Structure**: Each problem in its own JSON file for easy navigation
- ✅ **Educational Focus**: Learn array programming through practical examples
- ✅ **Open Source**: MIT licensed, contributions welcome

## 📖 Example Solutions

### Problem 1: Two Sum

```apl
TwoSum ← {
    ⍝ ⍺: target sum, ⍵: array
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}

⍝ Usage
target ← 9
nums ← 2 7 11 15
result ← target TwoSum nums  ⍝ Returns: 0 1
```

**Explanation**: Uses outer product `∘.` to generate all possible pair sums, then `⍸` to find matching indices.

- **Time Complexity**: O(n²)
- **Space Complexity**: O(n²)

### Problem 136: Single Number

```apl
SingleNumber ← {≠/⍵}

⍝ Usage
nums ← 4 1 2 1 2
result ← SingleNumber nums  ⍝ Returns: 4
```

**Explanation**: XOR reduce - APL's `≠` is XOR, `/` is reduce. Elegant one-liner leveraging XOR properties.

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Problem 206: Reverse Linked List

```apl
ReverseList ← {⌽⍵}

⍝ Usage
list ← 1 2 3 4 5
result ← ReverseList list  ⍝ Returns: 5 4 3 2 1
```

**Explanation**: `⌽` is APL's reverse operator - the simplest possible solution!

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## 🛠️ Technology Stack

- **Language**: APL (A Programming Language)
- **Documentation**: Pure Markdown (Static)
- **Format**: JSON data + Markdown READMEs
- **i18n**: 7 languages (English, 简中, 繁中, 日本語, Español, Deutsch, Français)
- **Hosting**: GitHub (static files)

## 📂 Project Structure

```
leetcode-apl-solutions/
├── problems/                    # All problem solutions
│   ├── 001-two-sum/            # Each problem in its own directory
│   │   ├── README.md           # 7 language versions
│   │   ├── README.zh-CN.md
│   │   └── ...
│   ├── 136-single-number/
│   ├── 206-reverse-linked-list/
│   └── index.json              # Problem metadata
├── PROBLEMS_INDEX.md           # Complete problem list (7 languages)
├── PROBLEMS_INDEX.zh-CN.md
├── README.md                   # Main documentation (7 languages)
├── README.zh-CN.md
└── generate_static_readmes.py  # Generator script
```

## 💻 How to Use

### 🌐 Browse on GitHub

Simply browse this repository on GitHub! No server needed - everything is static Markdown files.

1. **Start here**: [PROBLEMS_INDEX.md](PROBLEMS_INDEX.md) - Complete list of all problems
2. **Click any problem** to view its full solution with explanation
3. **Switch languages** using the navigation bar at the top of each page

### 📥 Clone Locally

```bash
git clone https://github.com/wmh/leetcode-apl-solutions.git
cd leetcode-apl-solutions

# View complete problem list
cat PROBLEMS_INDEX.md

# Browse a specific problem
cat problems/001-two-sum/README.md

# View in Chinese
cat problems/001-two-sum/README.zh-CN.md
```

### 🔧 Try the APL Solutions

To actually run the APL code, you'll need an APL interpreter:

1. **Online** (easiest): Visit [TryAPL.org](https://tryapl.org/)
2. **Dyalog APL**: Download from [dyalog.com](https://www.dyalog.com/download-zone.htm)
3. **GNU APL**: 
   - Linux: `apt install gnu-apl`
   - macOS: `brew install gnu-apl`

### 🔄 Generate More Problems

Use the included generator script to create new problem READMEs:

```bash
# Add your problem data to problems/*.json
# Then regenerate all READMEs
python3 generate_static_readmes.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add More Problems**: Implement additional LeetCode problems in APL
2. **Improve Solutions**: Optimize existing APL solutions
3. **Fix Bugs**: Report and fix any issues you find
4. **Translations**: Help improve language translations
5. **Documentation**: Enhance problem explanations

### 📘 Contribution Guide

**See [HOW_TO_ADD_PROBLEMS.md](HOW_TO_ADD_PROBLEMS.md)** for detailed instructions on adding new problems.

Quick steps:
1. Create a JSON file in `problems/` with your solution
2. Run `python3 generate_static_readmes.py`
3. Commit and push your changes

### Contribution Steps

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

### Learn APL
- [APL Wiki](https://aplwiki.com/) - Comprehensive APL documentation
- [Dyalog APL Tutorial](https://tutorial.dyalog.com/) - Official Dyalog tutorial
- [APL Cart](https://aplcart.info/) - Searchable APL idioms
- [Try APL](https://tryapl.org/) - Online APL interpreter

### LeetCode
- [LeetCode Problems](https://leetcode.com/problemset/all/) - Official problem list
- [LeetCode Top Interview Questions](https://leetcode.com/problem-list/top-interview-questions/)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kenneth E. Iverson** - Creator of APL
- **LeetCode** - For providing excellent algorithmic problems
- **Dyalog Ltd** - For maintaining and developing APL
- **APL Community** - For keeping this beautiful language alive

## 📧 Contact

- GitHub: [@wmh](https://github.com/wmh)
- Issues: [Report issues or suggestions](https://github.com/wmh/leetcode-apl-solutions/issues)

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

---

**Made with ❤️ and lots of ⍵, ⍺, ⌽, and ∇**

*"APL is a mistake, carried through to perfection. It is the language of the future for the programming techniques of the past: it creates a new generation of coding bums."* - Edsger W. Dijkstra

*"APL is like a perfect diamond: flawless, beautifully symmetrical, but you can't do anything with it."* - Unknown

Despite the criticisms, APL remains one of the most elegant and powerful languages for array manipulation! 🎯
