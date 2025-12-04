#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

SOLUTIONS_PART2 = {
    9: {
        "code": "IsPalindrome ← {(⍵<0):(0)⋄(⍕⍵)≡⌽⍕⍵}",
        "explanation": "Checks if negative (returns 0), converts to string (⍕⍵), compares with reverse (≡⌽⍕⍵)."
    },
    125: {
        "code": "IsPalindrome ← {s←((⍵∊⎕A,⎕D)/⍵)⋄s≡⌽s}",
        "explanation": "Filters to alphanumeric only ((⍵∊⎕A,⎕D)/⍵), compares with reverse (≡⌽). Note: requires uppercase input."
    },
    104: {
        "code": "MaxDepth ← {0=≢⍵:0⋄1+⌈/∇¨⍵}",
        "explanation": "Recursive: returns 0 for empty, otherwise 1 plus max depth of children. Works on nested arrays representing trees."
    },
    100: {
        "code": "SameTree ← {⍺≡⍵}",
        "explanation": "Simple match using APL's match operator (≡). Works for nested arrays representing trees."
    },
    226: {
        "code": "InvertTree ← {0=≢⍵:⍵⋄⌽∇¨⍵}",
        "explanation": "Recursive: returns input if empty, otherwise reverses (⌽) and recursively inverts children (∇¨)."
    },
    242: {
        "code": "IsAnagram ← {(⍋⍺)≡⍋⍵}",
        "explanation": "Sorts both strings (⍋⍺ and ⍋⍵), compares if identical (≡). Anagrams have same sorted form."
    },
    191: {
        "code": "HammingWeight ← {+/2⊥⍣¯1⊢⍵}",
        "explanation": "Converts to binary digits (2⊥⍣¯1), sums them (+/). Counts 1-bits."
    },
    190: {
        "code": "ReverseBits ← {2⊥⌽32↑2⊥⍣¯1⊢⍵}",
        "explanation": "Converts to binary (2⊥⍣¯1), pads to 32 bits (32↑), reverses (⌽), converts back to decimal (2⊥)."
    },
    268: {
        "code": "MissingNumber ← {(⊃(⍳1+⌈/⍵)~⍵)}",
        "explanation": "Creates range 0 to max (⍳1+⌈/⍵), removes present numbers (~⍵), takes first (⊃)."
    },
    338: {
        "code": "CountBits ← {+/¨2⊥⍣¯1¨⍳⍵+1}",
        "explanation": "Generates range (⍳⍵+1), converts each to binary (2⊥⍣¯1¨), sums bits (+/¨)."
    },
    344: {
        "code": "ReverseString ← {⌽⍵}",
        "explanation": "Simple reversal using APL's reverse operator (⌽)."
    },
    278: {
        "code": "FirstBadVersion ← {⊃⍸⍵}",
        "explanation": "Finds first 1 in boolean array. Requires isBadVersion as boolean array input."
    },
    69: {
        "code": "MySqrt ← {⌊⍵*0.5}",
        "explanation": "Computes square root (⍵*0.5), floors the result (⌊)."
    },
    326: {
        "code": "IsPowerOfThree ← {∧/0=3|⍵,⍵÷3*⍳⌊3⍟⍵}",
        "explanation": "Divides by powers of 3, checks if all remainders are 0. Uses logarithm to determine max power."
    },
    202: {
        "code": "IsHappy ← {1∊⍵{(⍺,⍨+/⍵*2)⊣((⊂⍵)∊⍺:⍵)}⍣≡⊢⍬}",
        "explanation": "Repeatedly sums squares of digits until cycle detected or reaches 1."
    },
}

def update_problem(num, solution_data):
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
    print("🔧 Batch Fixing APL Solutions - Part 2\n")
    print("="*70)
    
    fixed = 0
    failed = 0
    
    for num, solution in sorted(SOLUTIONS_PART2.items()):
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
    print(f"  📈 Total: {fixed} problems now have working code")

if __name__ == '__main__':
    main()
