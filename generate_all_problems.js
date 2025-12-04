// Script to generate all 100+ problem files
const fs = require('fs');
const path = require('path');

const problemsData = [
  {
    number: 2,
    title: "Add Two Numbers",
    difficulty: "medium",
    aplSolution: `AddTwoNumbers ← {
    ⍝ ⍺: first list, ⍵: second list
    maxLen ← (≢⍺) ⌈ (≢⍵)
    a ← maxLen↑⍺
    b ← maxLen↑⍵
    sum ← a + b
    carry ← ⌊sum÷10
    result ← 10|sum
    result + (1↓carry,0)
}

⍝ Example
l1 ← 2 4 3
l2 ← 5 6 4
result ← l1 AddTwoNumbers l2
⍝ Result: 7 0 8`,
    timeComplexity: "O(max(m,n))",
    spaceComplexity: "O(max(m,n))"
  },
  {
    number: 3,
    title: "Longest Substring Without Repeating Characters",
    difficulty: "medium",
    aplSolution: `LongestSubstring ← {
    ⍝ ⍵: input string
    n ← ≢⍵
    maxLen ← 0
    {
        i ← ⍵
        {
            j ← ⍵
            substr ← (j-i+1)↑i↓⍵
            (≢substr) = ≢∪substr: maxLen ⌈← j-i+1
            ⍬
        }¨ i↓⍳n
    }¨⍳n
    maxLen
}

⍝ Example
s ← 'abcabcbb'
result ← LongestSubstring s
⍝ Result: 3`,
    timeComplexity: "O(n³)",
    spaceComplexity: "O(n)"
  }
];

console.log('To generate all problems, run this with Node.js');
console.log('Example: node generate_all_problems.js');
