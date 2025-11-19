"""
Notion API Functions
"""

import os
import requests
from typing import Optional, Dict, List

# Get credentials from environment
NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")

def _get_headers():
    """Get Notion API headers"""
    return {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

BASE_URL = "https://api.notion.com/v1"

def query_database(database_id: str, filter_obj: Optional[Dict] = None, 
                   sorts: Optional[List] = None, page_size: int = 100) -> Dict:
    """Query a Notion database"""
    url = f"{BASE_URL}/databases/{database_id}/query"
    
    data = {"page_size": page_size}
    if filter_obj:
        data["filter"] = filter_obj
    if sorts:
        data["sorts"] = sorts
    
    response = requests.post(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"Notion API Error {response.status_code}: {response.text}"}
    
    return response.json()

def create_page(parent: Dict, properties: Dict, children: Optional[List] = None) -> Dict:
    """Create a Notion page"""
    url = f"{BASE_URL}/pages"
    
    data = {
        "parent": parent,
        "properties": properties
    }
    
    if children:
        data["children"] = children
    
    response = requests.post(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"Notion API Error {response.status_code}: {response.text}"}
    
    return response.json()

def update_page(page_id: str, properties: Dict) -> Dict:
    """Update a Notion page"""
    url = f"{BASE_URL}/pages/{page_id}"
    
    data = {"properties": properties}
    
    response = requests.patch(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"Notion API Error {response.status_code}: {response.text}"}
    
    return response.json()

def get_page(page_id: str) -> Dict:
    """Get a Notion page"""
    url = f"{BASE_URL}/pages/{page_id}"
    
    response = requests.get(url, headers=_get_headers())
    
    if response.status_code >= 400:
        return {"error": f"Notion API Error {response.status_code}: {response.text}"}
    
    return response.json()

def append_blocks(block_id: str, children: List[Dict]) -> Dict:
    """Append blocks to a Notion page"""
    url = f"{BASE_URL}/blocks/{block_id}/children"
    
    data = {"children": children}
    
    response = requests.patch(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"Notion API Error {response.status_code}: {response.text}"}
    
    return response.json()
