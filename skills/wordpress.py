"""
WordPress API Functions
"""

import os
import requests
from typing import Optional, Dict, List

# Get credentials from environment
WORDPRESS_URL = os.environ.get("WORDPRESS_URL", "")
WORDPRESS_USERNAME = os.environ.get("WORDPRESS_USERNAME", "")
WORDPRESS_PASSWORD = os.environ.get("WORDPRESS_PASSWORD", "")

def _get_auth():
    """Get WordPress authentication tuple"""
    return (WORDPRESS_USERNAME, WORDPRESS_PASSWORD)

def _get_base_url():
    """Get WordPress REST API base URL"""
    return f"{WORDPRESS_URL.rstrip('/')}/wp-json/wp/v2"

def create_post(title: str, content: str, status: str = "draft", **kwargs) -> Dict:
    """Create a WordPress post"""
    url = f"{_get_base_url()}/posts"
    
    data = {
        "title": title,
        "content": content,
        "status": status,
        **kwargs
    }
    
    response = requests.post(url, auth=_get_auth(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"WordPress API Error {response.status_code}: {response.text}"}
    
    return response.json()

def get_posts(per_page: int = 10, page: int = 1, status: str = "publish") -> List[Dict]:
    """Get WordPress posts"""
    url = f"{_get_base_url()}/posts"
    
    params = {
        "per_page": per_page,
        "page": page,
        "status": status
    }
    
    response = requests.get(url, auth=_get_auth(), params=params)
    
    if response.status_code >= 400:
        return {"error": f"WordPress API Error {response.status_code}: {response.text}"}
    
    return response.json()

def update_post(post_id: int, title: Optional[str] = None, 
                content: Optional[str] = None, **kwargs) -> Dict:
    """Update a WordPress post"""
    url = f"{_get_base_url()}/posts/{post_id}"
    
    data = {}
    if title:
        data["title"] = title
    if content:
        data["content"] = content
    data.update(kwargs)
    
    response = requests.post(url, auth=_get_auth(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"WordPress API Error {response.status_code}: {response.text}"}
    
    return response.json()

def delete_post(post_id: int) -> Dict:
    """Delete a WordPress post"""
    url = f"{_get_base_url()}/posts/{post_id}"
    
    response = requests.delete(url, auth=_get_auth())
    
    if response.status_code >= 400:
        return {"error": f"WordPress API Error {response.status_code}: {response.text}"}
    
    return response.json()

def upload_media(file_path: str, title: Optional[str] = None) -> Dict:
    """Upload media to WordPress"""
    url = f"{WORDPRESS_URL.rstrip('/')}/wp-json/wp/v2/media"
    
    # Note: For Vercel deployment, you'd handle file uploads differently
    # This is a simplified version
    
    return {"error": "File uploads require different handling in serverless"}
