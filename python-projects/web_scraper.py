#!/usr/bin/env python3
"""
File: web_scraper.py
Description: Web scraping utility for extracting data from websites
Author: Atharva
Date: 2025-01-22
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin, urlparse
import time


class WebScraper:
    """Web scraping utility class"""
    
    def __init__(self, base_url: str, delay: float = 1.0):
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.scraped_urls: List[str] = []
        
    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch HTML content from URL"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            self.scraped_urls.append(url)
            time.sleep(self.delay)
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_html(self, html: str) -> BeautifulSoup:
        """Parse HTML content with BeautifulSoup"""
        return BeautifulSoup(html, 'html.parser')
    
    def extract_links(self, html: str, base_url: str) -> List[str]:
        """Extract all links from HTML"""
        soup = self.parse_html(html)
        links = []
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            absolute_url = urljoin(base_url, href)
            links.append(absolute_url)
        
        return list(set(links))
    
    def extract_data(self, html: str, selectors: Dict[str, str]) -> Dict[str, Any]:
        """Extract data using CSS selectors"""
        soup = self.parse_html(html)
        data = {}
        
        for key, selector in selectors.items():
            elements = soup.select(selector)
            if len(elements) == 1:
                data[key] = elements[0].get_text(strip=True)
            else:
                data[key] = [el.get_text(strip=True) for el in elements]
        
        return data
    
    def scrape_table(self, html: str, table_selector: str = 'table') -> List[Dict[str, str]]:
        """Scrape data from HTML table"""
        soup = self.parse_html(html)
        table = soup.select_one(table_selector)
        
        if not table:
            return []
        
        headers = []
        header_row = table.find('tr')
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
        
        rows = []
        for row in table.find_all('tr')[1:]:
            cells = row.find_all(['td', 'th'])
            if cells:
                row_data = {}
                for i, cell in enumerate(cells):
                    header = headers[i] if i < len(headers) else f"col_{i}"
                    row_data[header] = cell.get_text(strip=True)
                rows.append(row_data)
        
        return rows
    
    def export_to_json(self, data: Any, filename: str) -> None:
        """Export data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def export_to_csv(self, data: List[Dict], filename: str) -> None:
        """Export data to CSV file"""
        if not data:
            return
            
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    def crawl(self, max_pages: int = 10) -> Dict[str, Any]:
        """Crawl multiple pages starting from base URL"""
        to_visit = [self.base_url]
        visited = set()
        all_data = []
        
        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            
            if url in visited:
                continue
            
            html = self.fetch_page(url)
            if html:
                visited.add(url)
                links = self.extract_links(html, url)
                to_visit.extend(links[:5])
                
                all_data.append({
                    'url': url,
                    'links': links,
                    'timestamp': time.time()
                })
        
        return {
            'base_url': self.base_url,
            'pages_scraped': len(visited),
            'data': all_data
        }


def main():
    """Main entry point"""
    scraper = WebScraper("https://example.com", delay=1.0)
    
    html = scraper.fetch_page("https://example.com")
    if html:
        print("Page fetched successfully")
        links = scraper.extract_links(html, "https://example.com")
        print(f"Found {len(links)} links")
        
        data = {
            'url': "https://example.com",
            'links_count': len(links)
        }
        scraper.export_to_json(data, "scraped_data.json")


if __name__ == "__main__":
    main()

