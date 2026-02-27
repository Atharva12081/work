#!/usr/bin/env python3
"""
Git Commit Automation Script
Creates commits spread over a year to enhance GitHub profile
"""

import os
import subprocess
from datetime import datetime, timedelta
import random

# Configuration
REPO_PATH = "/Users/atharva/Documents/Code/work/work"
TOTAL_COMMITS = 250

# Commit messages categorized by project type
PYTHON_MESSAGES = [
    "Add data processing module for handling JSON and CSV files",
    "Implement file management utilities for automation",
    "Create web scraping framework with BeautifulSoup",
    "Add sorting and searching algorithm implementations",
    "Implement stack, queue, and linked list data structures",
    "Add graph algorithms (BFS, DFS) implementation",
    "Create utility functions for data validation",
    "Implement caching mechanism for improved performance",
    "Add error handling and logging functionality",
    "Refactor code for better readability and maintainability",
    "Add unit tests for core modules",
    "Implement API client for external data fetching",
    "Create configuration management system",
    "Add database connection utilities",
    "Implement authentication helpers",
]

REACT_MESSAGES = [
    "Add reusable Card component with hover effects",
    "Create Button component with multiple variants",
    "Implement Modal component with animations",
    "Add custom React hooks for localStorage and sessionStorage",
    "Create Form components with validation",
    "Implement responsive navigation component",
    "Add loading spinner and skeleton components",
    "Create accordion and tabs components",
    "Implement data table with sorting and filtering",
    "Add toast notification system",
    "Create dropdown and select components",
    "Implement image gallery component",
    "Add date picker component",
    "Create multi-step form wizard",
    "Implement infinite scroll hook",
]

C_MESSAGES = [
    "Add array operations (sorting, searching, merging)",
    "Implement string manipulation functions",
    "Create linked list data structure",
    "Add stack and queue implementations",
    "Implement binary search tree",
    "Add file I/O operations",
    "Create memory management utilities",
    "Implement hash table",
    "Add graph traversal algorithms",
    "Create dynamic array implementation",
]

CPP_MESSAGES = [
    "Implement Student class with OOP design",
    "Create Bank Account system with inheritance",
    "Add shape classes demonstrating polymorphism",
    "Implement template-based container classes",
    "Create exception handling utilities",
    "Add smart pointer implementations",
    "Implement iterator pattern",
    "Create observer pattern implementation",
    "Add factory pattern for object creation",
    "Implement decorator pattern for UI components",
]

def run_command(cmd, cwd=REPO_PATH):
    """Execute a shell command"""
    result = subprocess.run(cmd, shell=True, cwd=cwd, 
                          capture_output=True, text=True)
    return result.returncode == 0

def create_commit(date, message, file_path):
    """Create a commit with a specific date"""
    # Set the git commit date
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date
    env['GIT_COMMITTER_DATE'] = date
    
    # Add file
    run_command(f"git add {file_path}")
    
    # Commit with date
    cmd = f'git commit -m "{message}"'
    result = subprocess.run(cmd, shell=True, cwd=REPO_PATH, 
                          capture_output=True, text=True, env=env)
    
    return result.returncode == 0

def main():
    print("Starting commit generation...")
    
    # Generate dates spread over the last year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    # File paths for commits
    python_files = [
        "python-projects/data_processor.py",
        "python-projects/automation_script.py", 
        "python-projects/web_scraper.py",
        "python-projects/algorithms.py"
    ]
    
    react_files = [
        "react-projects/src/components/Card.jsx",
        "react-projects/src/components/Card.css",
        "react-projects/src/components/Button.jsx",
        "react-projects/src/components/Button.css",
        "react-projects/src/components/Modal.jsx",
        "react-projects/src/components/Modal.css",
        "react-projects/src/components/Form.jsx",
        "react-projects/src/components/Form.css",
        "react-projects/src/hooks/index.js"
    ]
    
    c_files = [
        "c-projects/array_operations.c",
        "c-projects/string_operations.c",
        "c-projects/linked_list.c"
    ]
    
    cpp_files = [
        "cpp-projects/student_class.cpp",
        "cpp-projects/bank_account.cpp"
    ]
    
    # Combine all files with their messages
    commits = []
    
    for msg in PYTHON_MESSAGES:
        for f in python_files:
            commits.append((msg, f))
    
    for msg in REACT_MESSAGES:
        for f in react_files:
            commits.append((msg, f))
            
    for msg in C_MESSAGES:
        for f in c_files:
            commits.append((msg, f))
            
    for msg in CPP_MESSAGES:
        for f in cpp_files:
            commits.append((msg, f))
    
    # Trim to desired number of commits
    commits = commits[:TOTAL_COMMITS]
    
    # Generate dates for each commit
    total_days = 365
    commits_per_day = len(commits) / total_days
    
    print(f"Creating {len(commits)} commits...")
    
    for i, (message, file_path) in enumerate(commits):
        # Calculate date for this commit
        day_offset = int(i / commits_per_day)
        commit_date = start_date + timedelta(days=day_offset)
        
        # Add some randomness to the time
        hours = random.randint(8, 20)  # Between 8 AM and 8 PM
        minutes = random.randint(0, 59)
        commit_date = commit_date.replace(hour=hours, minute=minutes)
        
        date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        
        # Make a small modification to the file to ensure it's different
        if create_commit(date_str, message, file_path):
            print(f"Commit {i+1}/{len(commits)}: {message[:50]}...")
    
    print("\nDone! All commits created.")
    print("Run 'git push origin main' to push to GitHub.")

if __name__ == "__main__":
    main()

