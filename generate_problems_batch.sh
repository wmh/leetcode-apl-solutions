#!/bin/bash

# Script to create multiple problem files

# Array of problem data: number|title|difficulty
problems=(
    "70|Climbing Stairs|easy"
    "121|Best Time to Buy and Sell Stock|easy"
    "53|Maximum Subarray|medium"
    "283|Move Zeroes|easy"
    "448|Find All Numbers Disappeared in Array|easy"
    "226|Invert Binary Tree|easy"
    "234|Palindrome Linked List|easy"
    "338|Counting Bits|easy"
    "101|Symmetric Tree|easy"
    "104|Maximum Depth of Binary Tree|easy"
)

# Create sample problems
for problem_data in "${problems[@]}"; do
    IFS='|' read -r num title diff <<< "$problem_data"
    filename=$(printf "%03d" $num)
    filename="${filename}-$(echo $title | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | head -c 30).json"
    
    echo "Creating: problems/$filename"
done

echo "Done! Remember to manually create the JSON files based on the structure."
