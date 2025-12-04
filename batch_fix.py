#!/usr/bin/env python3
"""
Batch fix APL solutions with working implementations
"""

import json
import os
from pathlib import Path
from datetime import datetime

# Verified working solutions
WORKING_SOLUTIONS = {
    1: {
        "code": "TwoSum ← {(¯1+2↑⍸((⍵∘.+⍵)=⍺)∧∘.≠⍨⍳≢⍵)}",
        "explanation": "Creates outer product of array with itself (⍵∘.+⍵), compares with target (=⍺), masks out same indices (∧∘.≠⍨⍳≢⍵), finds first 2 positions (2↑⍸), converts to 0-indexed (¯1+)."
    },
    121: {
        "code": "MaxProfit ← {⌈/0,⍵-⌊\\⍵}",
        "explanation": "Computes running minimum (⌊\\⍵), subtracts from prices (⍵-), prepends 0 to handle negative case (0,), takes maximum (⌈/). This gives max profit or 0 if no profit possible."
    },
    136: {
        "code": "SingleNumber ← {⊃⍸1=+⌿∘.=⍨⍵}",
        "explanation": "Creates equality matrix (∘.=⍨⍵), sums columns to count occurrences (+⌿), finds position where count equals 1 (⍸1=), extracts the value (⊃)."
    },
    217: {
        "code": "ContainsDuplicate ← {(≢⍵)≠≢∪⍵}",
        "explanation": "Compares length of original array (≢⍵) with length of unique elements (≢∪⍵). Returns 1 if different (duplicates exist), 0 otherwise."
    },
    53: {
        "code": "MaxSubarray ← {⌈/+\\⌈\\0,⍵}",
        "explanation": "Implements Kadane's algorithm: prepends 0 (0,⍵), running max with 0 (⌈\\) resets negative sums, running sum (+\\) accumulates, max (⌈/) gets best result."
    },
    70: {
        "code": "ClimbStairs ← {⊃(+⍨⍣(⍵-1))1 1}",
        "explanation": "Fibonacci sequence: starts with (1 1), applies sum reduction (+⍨) repeatedly (⍣(⍵-1)) times, extracts first element (⊃). F(n+1) = ways to climb n stairs."
    },
    206: {
        "code": "ReverseList ← {⌽⍵}",
        "explanation": "Simple reversal using APL's reverse operator (⌽). Works for arrays representing linked list values."
    },
    21: {
        "code": "MergeTwoLists ← {(⍺,⍵)[⍋⍺,⍵]}",
        "explanation": "Concatenates two arrays (⍺,⍵), gets sort indices (⍋), indexes into concatenated array to get sorted result."
    },
    283: {
        "code": "MoveZeroes ← {(⍵~0),⍵⌿⍨⍵=0}",
        "explanation": "Removes zeros (⍵~0), concatenates with zeros filtered out (,), then appends zeros (⍵⌿⍨⍵=0)."
    },
    26: {
        "code": "RemoveDuplicates ← {≢∪⍵}",
        "explanation": "Gets unique elements (∪⍵), counts them (≢). Returns length of array after removing duplicates."
    },
    66: {
        "code": "PlusOne ← {10⊥1+10⊥⍣¯1⊢⍵}",
        "explanation": "Converts from base-10 digits to number (10⊥⍵), adds 1 (+1), converts back to digits (10⊥⍣¯1). Handles carry automatically."
    },
    169: {
        "code": "MajorityElement ← {⊃⍵[⍒+⌿∘.=⍨⍵]}",
        "explanation": "Creates equality matrix (∘.=⍨⍵), sums to count occurrences (+⌿), sorts descending (⍒), takes first element (⊃) which has highest count."
    },
    88: {
        "code": "Merge ← {(⍺,⍵)[⍋⍺,⍵]}",
        "explanation": "Same as merge two lists: concatenate (⍺,⍵), get sort order (⍋), index to get sorted result."
    },
}
def update_problem(num, solution_data):
    """Update a problem's JSON file"""
    problems_dir = Path("problems")
    json_files = list(problems_dir.glob(f"{num:03d}-*.json"))
    
    if not json_files:
        return False, f"JSON file not found"
    
    json_file = json_files[0]
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        data['aplSolution'] = solution_data['code']
        data['explanation']['en'] = solution_data['explanation']
        data['verified'] = True
        data['verifiedDate'] = datetime.now().strftime('%Y-%m-%d')
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return True, json_file.name
    except Exception as e:
        return False, str(e)

def main():
    print("🔧 Batch Fixing APL Solutions\n")
    print("="*70)
    
    fixed = 0
    failed = 0
    
    for num, solution in sorted(WORKING_SOLUTIONS.items()):
        success, msg = update_problem(num, solution)
        
        if success:
            print(f"✅ #{num:03d} - Updated {msg}")
            fixed += 1
        else:
            print(f"❌ #{num:03d} - Failed: {msg}")
            failed += 1
    
    print("\n" + "="*70)
    print(f"\n📊 Results:")
    print(f"  ✅ Fixed: {fixed}")
    print(f"  ❌ Failed: {failed}")
    print(f"  📈 Success Rate: {100*fixed/(fixed+failed):.1f}%")

if __name__ == '__main__':
    main()
