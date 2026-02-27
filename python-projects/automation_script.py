#!/usr/bin/env python3
"""
File: automation_script.py
Description: Automation script for file management and system tasks
Author: Atharva
Date: 2025-01-18
"""

import os
import shutil
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


class FileManager:
    """Handles file and directory operations"""
    
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.operations_log: List[Dict] = []
        
    def scan_directory(self, extensions: Optional[List[str]] = None) -> List[Path]:
        """Scan directory for files with specific extensions"""
        files = []
        for item in self.root_dir.rglob('*'):
            if item.is_file():
                if extensions is None or item.suffix in extensions:
                    files.append(item)
        return files
    
    def calculate_checksum(self, file_path: Path) -> str:
        """Calculate MD5 checksum of a file"""
        hash_md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def duplicate_finder(self) -> Dict[str, List[Path]]:
        """Find duplicate files based on checksum"""
        checksums: Dict[str, List[Path]] = {}
        files = self.scan_directory()
        
        for file_path in files:
            checksum = self.calculate_checksum(file_path)
            if checksum not in checksums:
                checksums[checksum] = []
            checksums[checksum].append(file_path)
        
        return {k: v for k, v in checksums.items() if len(v) > 1}
    
    def organize_by_extension(self) -> None:
        """Organize files into folders by extension"""
        files = self.scan_directory()
        
        for file_path in files:
            ext = file_path.suffix[1:] or 'no_extension'
            dest_dir = self.root_dir / ext
            
            if not dest_dir.exists():
                dest_dir.mkdir(parents=True)
            
            dest_path = dest_dir / file_path.name
            shutil.move(str(file_path), str(dest_path))
            
            self.operations_log.append({
                'operation': 'organize',
                'source': str(file_path),
                'destination': str(dest_path),
                'timestamp': datetime.now().isoformat()
            })
    
    def backup_files(self, destination: str) -> int:
        """Backup files to destination folder"""
        dest_path = Path(destination)
        files = self.scan_directory()
        backed_up = 0
        
        for file_path in files:
            rel_path = file_path.relative_to(self.root_dir)
            dest_file = dest_path / rel_path
            
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, dest_file)
            backed_up += 1
            
            self.operations_log.append({
                'operation': 'backup',
                'source': str(file_path),
                'destination': str(dest_file),
                'timestamp': datetime.now().isoformat()
            })
        
        return backed_up


class SystemMonitor:
    """Monitor system resources and processes"""
    
    @staticmethod
    def get_disk_usage() -> Dict[str, int]:
        """Get disk usage statistics"""
        usage = shutil.disk_usage('/')
        return {
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': int((usage.used / usage.total) * 100)
        }
    
    @staticmethod
    def get_directory_size(path: str) -> int:
        """Calculate total size of directory"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.exists(filepath):
                    total_size += os.path.getsize(filepath)
        return total_size
    
    @staticmethod
    def format_size(size_bytes: int) -> str:
        """Format bytes to human readable size"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"


def main():
    """Main entry point"""
    manager = FileManager("./test_directory")
    
    print("Scanning directory...")
    files = manager.scan_directory()
    print(f"Found {len(files)} files")
    
    print("\nDisk Usage:")
    usage = SystemMonitor.get_disk_usage()
    print(f"Total: {SystemMonitor.format_size(usage['total'])}")
    print(f"Used: {SystemMonitor.format_size(usage['used'])}")
    print(f"Free: {SystemMonitor.format_size(usage['free'])}")
    print(f"Usage: {usage['percent']}%")


if __name__ == "__main__":
    main()

