"""
Vercel API Functions
"""

import os
import requests
from typing import Optional, Dict, List

# Get credentials from environment
VERCEL_TOKEN = os.environ.get("VERCEL_TOKEN", "")

def _get_headers():
    """Get Vercel API headers"""
    return {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type": "application/json"
    }

BASE_URL = "https://api.vercel.com"

def list_projects(team_id: Optional[str] = None) -> Dict:
    """List all projects"""
    url = f"{BASE_URL}/v9/projects"
    
    params = {}
    if team_id:
        params["teamId"] = team_id
    
    response = requests.get(url, headers=_get_headers(), params=params)
    
    if response.status_code >= 400:
        return {"error": f"Vercel API Error {response.status_code}: {response.text}"}
    
    return response.json()

def create_project(name: str, framework: Optional[str] = None,
                   team_id: Optional[str] = None) -> Dict:
    """Create a new project"""
    url = f"{BASE_URL}/v9/projects"
    
    data = {"name": name}
    if framework:
        data["framework"] = framework
    
    params = {}
    if team_id:
        params["teamId"] = team_id
    
    response = requests.post(url, headers=_get_headers(), json=data, params=params)
    
    if response.status_code >= 400:
        return {"error": f"Vercel API Error {response.status_code}: {response.text}"}
    
    return response.json()

def list_env_vars(project_id: str, team_id: Optional[str] = None) -> Dict:
    """List environment variables for a project"""
    url = f"{BASE_URL}/v10/projects/{project_id}/env"
    
    params = {}
    if team_id:
        params["teamId"] = team_id
    
    response = requests.get(url, headers=_get_headers(), params=params)
    
    if response.status_code >= 400:
        return {"error": f"Vercel API Error {response.status_code}: {response.text}"}
    
    return response.json()

def create_env_var(project_id: str, key: str, value: str,
                   target: Optional[List[str]] = None, 
                   type: str = "encrypted",
                   team_id: Optional[str] = None) -> Dict:
    """Create an environment variable"""
    if target is None:
        target = ["production", "preview", "development"]
    
    url = f"{BASE_URL}/v10/projects/{project_id}/env"
    
    data = {
        "key": key,
        "value": value,
        "type": type,
        "target": target
    }
    
    params = {}
    if team_id:
        params["teamId"] = team_id
    
    response = requests.post(url, headers=_get_headers(), json=data, params=params)
    
    if response.status_code >= 400:
        return {"error": f"Vercel API Error {response.status_code}: {response.text}"}
    
    return response.json()

def list_deployments(project_id: Optional[str] = None,
                    team_id: Optional[str] = None,
                    limit: int = 20) -> Dict:
    """List deployments"""
    url = f"{BASE_URL}/v6/deployments"
    
    params = {"limit": limit}
    if project_id:
        params["projectId"] = project_id
    if team_id:
        params["teamId"] = team_id
    
    response = requests.get(url, headers=_get_headers(), params=params)
    
    if response.status_code >= 400:
        return {"error": f"Vercel API Error {response.status_code}: {response.text}"}
    
    return response.json()
