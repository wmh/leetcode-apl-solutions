# 🧠 LeetCode APL Solutions

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: APL](https://img.shields.io/badge/Language-APL-blue.svg)](https://aplwiki.com/)
[![Problems: 100+](https://img.shields.io/badge/Problems-100+-green.svg)](https://leetcode.com/)
[![AI Generated](https://img.shields.io/badge/AI-Generated-purple.svg)](./AI_GENERATED.md)

> Solving LeetCode's top 100+ classic problems using APL (A Programming Language) - one of the most esoteric and powerful array programming languages.

> **⚠️ AI-Generated Content**: This project was created with significant AI assistance. See [AI_GENERATED.md](./AI_GENERATED.md) for details.

> **🚨 IMPORTANT**: APL code has **NOT been validated** in an actual interpreter. The solutions may contain syntax errors or incorrect implementations. **[See Validation Status](VALIDATION_STATUS.md)** for details. Do not use for production or interviews without testing!

**🌍 Languages**: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Deutsch](./README.de.md) | [Français](./README.fr.md)

## 📋 Table of Contents

- [About This Project](#-about-this-project)
- [Problem Coverage](#-problem-coverage)
- [Problem List](#-problem-list) ⭐
- [Multi-Language Support](#-multi-language-support)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [How to Use](#-how-to-use)
- [Contributing](#-contributing) 📝
- [Resources](#-resources)
- [License](#-license)

## 🔥 Quick Links

- 🚨 **[⚠️ VALIDATION STATUS](VALIDATION_STATUS.md)** - **READ THIS FIRST!**
- 📢 **[Honest Disclosure](HONEST_DISCLOSURE.md)** - Important information about code quality
- 📚 **[View All Problems](PROBLEMS_INDEX.md)** - Complete problem index
- 📖 **[How to Add Problems](HOW_TO_ADD_PROBLEMS.md)** - Contribution guide
- 📁 **[Project Structure](PROJECT_STRUCTURE.md)** - Detailed structure overview
- 🚀 **[Quick Start (中文)](QUICK_START.zh-CN.md)** - Chinese quick start guide

## 🎯 About This Project

This project showcases solutions to LeetCode's most popular problems implemented in **APL (A Programming Language)**, a unique language known for:

- **Extreme Conciseness**: Express complex algorithms in just a few characters
- **Array-Oriented**: Native support for powerful array operations
- **Mathematical Notation**: Uses special Unicode symbols (⍵, ⍺, ⌽, ⊥, ∇, etc.)
- **High Learning Curve**: Considered one of the most difficult languages to master

### Why APL?

APL challenges conventional programming paradigms and offers:
- A completely different way of thinking about algorithms
- Elegant solutions that often reveal the mathematical essence of problems
- A rich set of primitive operations for array manipulation
- Historical significance as one of the earliest high-level languages

## 📊 Problem Coverage

| Difficulty | Count | Percentage |
|------------|-------|------------|
| 🟢 Easy    | 40+   | ~35%       |
| 🟡 Medium  | 50+   | ~50%       |
| 🔴 Hard    | 15+   | ~15%       |
| **Total**  | **100+** | **100%** |

## 📝 Problem List

### 📚 Browse All Problems

**➡️ [View Complete Problem Index](PROBLEMS_INDEX.md)** - Full list of 100+ problems with direct links

Each problem includes:
- 🌍 Full documentation in 7 languages
- 💡 APL solution with detailed explanation
- ⏱️ Time and space complexity analysis
- 🔗 Links to LeetCode and APL resources

### Featured Problems

#### [#1 - Two Sum](problems/001-two-sum/README.md) 🟢
Given an array of integers and a target, return indices of two numbers that add up to target.

```apl
TwoSum ← {
    ⍝ ⍺: target sum, ⍵: array
    indices ← ⍸⍺=+/∘.,⍨⍵
    2↑indices
}
```
**Complexity**: Time O(n²), Space O(n²)

---

#### [#136 - Single Number](problems/136-single-number/README.md) 🟢
Find the element that appears only once in an array where every other element appears twice.

```apl
SingleNumber ← {≠/⍵}
```
**Complexity**: Time O(n), Space O(1)

---

#### [#206 - Reverse Linked List](problems/206-reverse-linked-list/README.md) 🟢
Reverse a singly linked list.

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
