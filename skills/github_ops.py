"""
GitHub API Functions
"""

import os
import requests
import base64
from typing import Optional, Dict, List

# Get credentials from environment
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def _get_headers():
    """Get GitHub API headers"""
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

BASE_URL = "https://api.github.com"

def list_repos(per_page: int = 30, sort: str = "updated") -> List[Dict]:
    """List user repositories"""
    url = f"{BASE_URL}/user/repos"
    
    params = {
        "per_page": per_page,
        "sort": sort
    }
    
    response = requests.get(url, headers=_get_headers(), params=params)
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()

def create_repo(name: str, description: str = "", private: bool = False, 
                auto_init: bool = True) -> Dict:
    """Create a new repository"""
    url = f"{BASE_URL}/user/repos"
    
    data = {
        "name": name,
        "description": description,
        "private": private,
        "auto_init": auto_init
    }
    
    response = requests.post(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()

def get_repo(owner: str, repo: str) -> Dict:
    """Get a specific repository"""
    url = f"{BASE_URL}/repos/{owner}/{repo}"
    
    response = requests.get(url, headers=_get_headers())
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()

def create_file(owner: str, repo: str, path: str, content: str, 
                message: str, branch: str = "main") -> Dict:
    """Create a file in a repository"""
    url = f"{BASE_URL}/repos/{owner}/{repo}/contents/{path}"
    
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch
    }
    
    response = requests.put(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()

def update_file(owner: str, repo: str, path: str, content: str,
                message: str, sha: str, branch: str = "main") -> Dict:
    """Update a file in a repository"""
    url = f"{BASE_URL}/repos/{owner}/{repo}/contents/{path}"
    
    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "sha": sha,
        "branch": branch
    }
    
    response = requests.put(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()

def create_issue(owner: str, repo: str, title: str, body: str = "",
                 labels: Optional[List[str]] = None) -> Dict:
    """Create an issue"""
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    
    data = {
        "title": title,
        "body": body
    }
    
    if labels:
        data["labels"] = labels
    
    response = requests.post(url, headers=_get_headers(), json=data)
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()

def list_issues(owner: str, repo: str, state: str = "open", per_page: int = 30) -> List[Dict]:
    """List issues for a repository"""
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    
    params = {
        "state": state,
        "per_page": per_page
    }
    
    response = requests.get(url, headers=_get_headers(), params=params)
    
    if response.status_code >= 400:
        return {"error": f"GitHub API Error {response.status_code}: {response.text}"}
    
    return response.json()
