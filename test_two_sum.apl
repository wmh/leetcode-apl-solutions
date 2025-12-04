⍝ Two Sum - Single line version for GNU APL
TwoSum ← {((2↑⍸((⍵∘.+⍵)=⍺)∧∘.≠⍨⍳≢⍵))-1}

⍝ Test cases
⎕←9 TwoSum 2 7 11 15
⎕←6 TwoSum 3 2 4
⎕←6 TwoSum 3 3
