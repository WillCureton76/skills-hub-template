"""
Skills Hub - FastAPI Application
One endpoint to rule them all
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import os
import requests
import json

app = FastAPI(title="Skills Hub", description="Your personal API connector hub")

# Import all skill functions
from skills import wordpress, notion, github_ops, vercel_ops

# Skill routing table
SKILLS = {
    # WordPress
    "wordpress_create_post": wordpress.create_post,
    "wordpress_get_posts": wordpress.get_posts,
    "wordpress_update_post": wordpress.update_post,
    "wordpress_delete_post": wordpress.delete_post,
    "wordpress_upload_media": wordpress.upload_media,
    
    # Notion
    "notion_query_database": notion.query_database,
    "notion_create_page": notion.create_page,
    "notion_update_page": notion.update_page,
    "notion_get_page": notion.get_page,
    "notion_append_blocks": notion.append_blocks,
    
    # GitHub
    "github_list_repos": github_ops.list_repos,
    "github_create_repo": github_ops.create_repo,
    "github_get_repo": github_ops.get_repo,
    "github_create_file": github_ops.create_file,
    "github_update_file": github_ops.update_file,
    "github_create_issue": github_ops.create_issue,
    "github_list_issues": github_ops.list_issues,
    
    # Vercel
    "vercel_list_projects": vercel_ops.list_projects,
    "vercel_create_project": vercel_ops.create_project,
    "vercel_create_env_var": vercel_ops.create_env_var,
    "vercel_list_env_vars": vercel_ops.list_env_vars,
    "vercel_list_deployments": vercel_ops.list_deployments,
}

@app.get("/")
async def root():
    """Health check and info endpoint"""
    return {
        "name": "Skills Hub",
        "status": "operational",
        "available_skills": list(SKILLS.keys()),
        "total_skills": len(SKILLS)
    }

@app.post("/skill-call")
async def skill_call(request: Request):
    """
    Universal skill router
    
    Accepts: {"skill": "skill_name", "params": {...}}
    Returns: Result from the skill function
    """
    try:
        payload = await request.json()
        
        skill_name = payload.get("skill")
        params = payload.get("params", {})
        
        if not skill_name:
            raise HTTPException(status_code=400, detail="Missing 'skill' parameter")
        
        if skill_name not in SKILLS:
            raise HTTPException(
                status_code=404, 
                detail=f"Skill '{skill_name}' not found. Available: {list(SKILLS.keys())}"
            )
        
        # Execute the skill
        skill_function = SKILLS[skill_name]
        result = skill_function(**params)
        
        return JSONResponse(content=result)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    """Simple health check"""
    return {"status": "healthy"}

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
