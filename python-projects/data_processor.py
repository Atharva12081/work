#!/usr/bin/env python3
"""
File: data_processor.py
Description: Data processing utility for handling various data formats
Author: Atharva
Date: 2025-01-15
"""

import json
import csv
import os
from typing import Dict, List, Any, Optional


class DataProcessor:
    """Main class for data processing operations"""
    
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.data: List[Dict[str, Any]] = []
        
    def load_json(self) -> bool:
        """Load data from JSON file"""
        try:
            with open(self.input_file, 'r') as f:
                self.data = json.load(f)
            return True
        except FileNotFoundError:
            print(f"Error: File {self.input_file} not found")
            return False
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.input_file}")
            return False
    
    def load_csv(self) -> bool:
        """Load data from CSV file"""
        try:
            with open(self.input_file, 'r') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
            return True
        except FileNotFoundError:
            print(f"Error: File {self.input_file} not found")
            return False
    
    def save_json(self) -> bool:
        """Save data to JSON file"""
        try:
            with open(self.output_file, 'w') as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def filter_data(self, key: str, value: Any) -> List[Dict[str, Any]]:
        """Filter data based on key-value pair"""
        return [item for item in self.data if item.get(key) == value]
    
    def transform_data(self, transform_func) -> None:
        """Apply transformation function to all data items"""
        self.data = [transform_func(item) for item in self.data]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Calculate basic statistics for the data"""
        if not self.data:
            return {"count": 0}
        
        numeric_fields = {}
        for item in self.data:
            for key, value in item.items():
                if isinstance(value, (int, float)):
                    if key not in numeric_fields:
                        numeric_fields[key] = []
                    numeric_fields[key].append(value)
        
        stats = {"count": len(self.data)}
        for field, values in numeric_fields.items():
            stats[field] = {
                "sum": sum(values),
                "avg": sum(values) / len(values),
                "min": min(values),
                "max": max(values)
            }
        
        return stats


def main():
    """Main entry point for the data processor"""
    processor = DataProcessor("input.json", "output.json")
    
    if processor.load_json():
        print(f"Loaded {len(processor.data)} records")
        stats = processor.get_statistics()
        print(f"Statistics: {stats}")
        processor.save_json()
        print("Data processing complete")


if __name__ == "__main__":
    main()

