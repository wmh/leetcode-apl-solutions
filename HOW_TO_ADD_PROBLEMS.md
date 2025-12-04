# 📝 How to Add New Problems

This guide explains how to add new LeetCode problems to this repository.

## Quick Start

1. Create a JSON file for your problem
2. Run the generator script
3. Commit your changes

## Step-by-Step Guide

### 1. Create Problem JSON File

Create a new JSON file in the `problems/` directory following this naming convention:
```
problems/XXX-problem-name.json
```

Where `XXX` is the 3-digit problem number (e.g., `001`, `042`, `347`).

### 2. JSON File Structure

Use this template for your problem:

```json
{
  "number": 1,
  "title": "Two Sum",
  "difficulty": "easy",
  "description": {
    "en": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
    "zh-CN": "给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数。",
    "zh-TW": "給定一個整數陣列 nums 和一個整數目標值 target，請你在該陣列中找出和為目標值 target 的那兩個整數。",
    "ja": "整数配列 nums と整数 target が与えられたとき、合計が target になる 2 つの数値のインデックスを返します。",
    "es": "Dado un array de enteros nums y un entero target, devuelve los índices de los dos números que suman target.",
    "de": "Gegeben ein Array von Ganzzahlen nums und eine Ganzzahl target, gib die Indizes der zwei Zahlen zurück.",
    "fr": "Étant donné un tableau d'entiers nums et un entier target, renvoyez les indices des deux nombres."
  },
  "aplSolution": "TwoSum ← {\n    ⍝ ⍺: target sum, ⍵: array\n    indices ← ⍸⍺=+/∘.,⍨⍵\n    2↑indices\n}",
  "explanation": {
    "en": "Uses outer product operator ∘. to generate all possible pair sums.",
    "zh-CN": "使用外积操作符 ∘. 生成所有可能的数对和。",
    "zh-TW": "使用外積運算子 ∘. 生成所有可能的數對和。",
    "ja": "外積演算子 ∘. を使用してすべての可能なペア和を生成します。",
    "es": "Utiliza el operador de producto exterior ∘. para generar todas las sumas posibles.",
    "de": "Verwendet den äußeren Produktoperator ∘. um alle möglichen Paarsummen zu generieren.",
    "fr": "Utilise l'opérateur de produit extérieur ∘. pour générer toutes les sommes possibles."
  },
  "timeComplexity": "O(n²)",
  "spaceComplexity": "O(n²)"
}
```

### 3. Required Fields

- `number`: Problem number (integer)
- `title`: Problem title in English (string)
- `difficulty`: One of: "easy", "medium", "hard" (string)
- `description`: Object with descriptions in 7 languages
- `aplSolution`: APL code solution (string, use `\n` for line breaks)
- `explanation`: Object with explanations in 7 languages
- `timeComplexity`: Big O notation (string)
- `spaceComplexity`: Big O notation (string)

### 4. Update Index

Add your problem to `problems/index.json`:

```json
[
  {
    "number": 1,
    "file": "001-two-sum.json"
  },
  {
    "number": 2,
    "file": "002-add-two-numbers.json"
  }
]
```

Keep the list sorted by problem number.

### 5. Generate README Files

Run the generator script:

```bash
python3 generate_static_readmes.py
```

This will:
- Create a directory for your problem: `problems/XXX-problem-name/`
- Generate 7 language README files in that directory
- Update all `PROBLEMS_INDEX.*.md` files

### 6. Verify Your Changes

Check that the following were created:
- `problems/XXX-problem-name/README.md` (and 6 other language files)
- Your problem appears in all `PROBLEMS_INDEX.*.md` files

### 7. Commit Your Changes

```bash
git add problems/XXX-problem-name.json
git add problems/XXX-problem-name/
git add problems/index.json
git add PROBLEMS_INDEX*.md
git commit -m "Add problem #XXX: Problem Name"
git push
```

## Tips for Writing APL Solutions

### 1. Keep It Concise
APL is known for brevity. Try to capture the essence of the algorithm.

### 2. Add Comments
Use `⍝` for comments to explain your solution:
```apl
⍝ This is a comment
solution ← {⍵+1}  ⍝ Increment by one
```

### 3. Show Examples
Include usage examples in your solution:
```apl
MyFunction ← {
    ⍝ Implementation
}

⍝ Example usage
input ← 1 2 3 4 5
result ← MyFunction input
⍝ Result: 2 4 6 8 10
```

### 4. Test Your Code
If possible, test your APL code at [TryAPL.org](https://tryapl.org/) before submitting.

### 5. APL Symbols Reference
Common symbols you might need:
- `⍵` - right argument (omega)
- `⍺` - left argument (alpha)
- `⌽` - reverse
- `⍸` - where (indices where true)
- `∘.` - outer product
- `/` - reduce
- `⊂` - enclose
- `⊃` - disclose/pick
- `∇` - del (recursive call)

## Translation Tips

### English Description
- Clear and concise
- Follow LeetCode's style
- Include constraints if important

### Other Languages
- Use DeepL, Google Translate, or ChatGPT for initial translations
- Have native speakers review if possible
- Keep technical terms consistent (e.g., "array" → "数组/陣列/配列")

## Common Difficulty Classifications

### Easy (简单/簡單/簡単)
- Two Sum, Reverse Linked List, Valid Palindrome
- Usually O(n) or O(log n) solutions
- Straightforward logic

### Medium (中等/中等/中級)
- 3Sum, Maximum Subarray, Word Search
- May require O(n²) or dynamic programming
- More complex logic

### Hard (困难/困難/ハード)
- Trapping Rain Water, Median of Two Sorted Arrays
- Often O(n²) or worse, or complex algorithms
- Requires advanced techniques

## Example: Adding Problem #42

1. Create `problems/042-trapping-rain-water.json`
2. Write your APL solution
3. Add translations for all 7 languages
4. Update `problems/index.json`
5. Run `python3 generate_static_readmes.py`
6. Commit and push!

## Need Help?

- Check existing problems for examples
- Review the JSON schema above
- Open an issue on GitHub
- Test APL code at [TryAPL.org](https://tryapl.org/)

---

**Happy problem solving! 🎉**
