⍝ Test Two Sum
TwoSum ← {((2↑⍸((⍵∘.+⍵)=⍺)∧∘.≠⍨⍳≢⍵))-1}
⎕←'Result:'
⎕←9 TwoSum 2 7 11 15
