---
name: skill-router
description: Universal router to your personal Skills Hub. This tiny Skill connects Claude to YOUR hosted hub where all API logic and keys live securely.
---

# Skills Hub Router

**One Skill to Rule Them All**

This router connects Claude to your personal Skills Hub deployed on Vercel.

## Setup

1. Deploy your hub using the template: https://github.com/WillCureton76/skills-hub-template
2. Get your deployment URL from Vercel (e.g., `https://your-hub-abc123.vercel.app`)
3. Edit the `HUB_URL` below to match YOUR hub
4. Upload this file to Claude Skills
5. Done!

## Configuration

```python
# 🔧 EDIT THIS LINE - Add your hub URL
HUB_URL = "https://your-hub-abc123.vercel.app"
```

## Router Code

```python
import requests
from typing import Dict, Any

# Your hub URL (edit above)
HUB_URL = "https://your-hub-abc123.vercel.app"

def call_skill(skill: str, **params) -> Dict[str, Any]:
    """
    Call any skill on your hub.
    
    Args:
        skill: Name of the skill to call (e.g., 'wordpress_create_post')
        **params: Parameters to pass to the skill
        
    Returns:
        dict: Result from the skill
        
    Example:
        call_skill('github_create_repo', name='my-repo', description='Test', private=False)
    """
    try:
        response = requests.post(
            f"{HUB_URL}/skill-call",
            json={
                "skill": skill,
                "params": params
            },
            timeout=30
        )
        
        # Check for errors
        if response.status_code >= 400:
            return {
                "error": f"Hub returned error {response.status_code}",
                "details": response.text
            }
        
        return response.json()
        
    except requests.exceptions.Timeout:
        return {"error": "Request timed out - hub may be slow or down"}
    except requests.exceptions.ConnectionError:
        return {"error": f"Could not connect to hub at {HUB_URL}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

# Helper function for health check
def check_hub_health() -> Dict:
    """Check if your hub is operational"""
    try:
        response = requests.get(f"{HUB_URL}/health", timeout=10)
        return response.json()
    except Exception as e:
        return {"error": f"Hub health check failed: {str(e)}"}
```

## Available Skills

When you call `call_skill()`, use these skill names:

### WordPress
- `wordpress_create_post`
- `wordpress_get_posts`
- `wordpress_update_post`
- `wordpress_delete_post`

### Notion
- `notion_query_database`
- `notion_create_page`
- `notion_update_page`
- `notion_get_page`
- `notion_append_blocks`

### GitHub
- `github_list_repos`
- `github_create_repo`
- `github_get_repo`
- `github_create_file`
- `github_update_file`
- `github_create_issue`
- `github_list_issues`

### Vercel
- `vercel_list_projects`
- `vercel_create_project`
- `vercel_create_env_var`
- `vercel_list_env_vars`
- `vercel_list_deployments`

## Usage Examples

```python
# Create a GitHub repository
result = call_skill('github_create_repo',
    name='my-new-project',
    description='Created via Skills Hub',
    private=False
)

# Query a Notion database
result = call_skill('notion_query_database',
    database_id='abc123...',
    filter_obj={'property': 'Status', 'status': {'equals': 'Active'}}
)

# Create a WordPress post
result = call_skill('wordpress_create_post',
    title='Hello World',
    content='<p>My first post via hub!</p>',
    status='publish'
)

# Create Vercel environment variable
result = call_skill('vercel_create_env_var',
    project_id='my-project',
    key='DATABASE_URL',
    value='postgresql://...'
)
```

## Security Notes

✅ **Your API keys are server-side** - Never touch Claude  
✅ **Network whitelisting recommended** - Only allow your hub URL  
✅ **You control the infrastructure** - Your Vercel account  
✅ **Open source** - Audit the hub code on GitHub

## Troubleshooting

### "Could not connect to hub"
- Check your `HUB_URL` is correct
- Verify your Vercel deployment is live
- Check Claude's network whitelist includes your hub

### "Hub returned error 500"
- Check your hub's environment variables in Vercel
- View deployment logs in Vercel dashboard
- Verify API tokens are valid

### "Skill not found"
- Check the skill name spelling
- View available skills: Visit `https://your-hub.vercel.app/`

## Learn More

- Template repo: https://github.com/WillCureton76/skills-hub-template
- Documentation: See README in template repo
- Issues: Open on GitHub

---

**This is the future of Skills sharing** - Everyone hosts their own hub, so API keys stay secure and controlled.
