# 🚀 Skills Hub Template

**One-click deployable API connector hub for Claude**

This template lets you host your own Skills Hub on Vercel, giving Claude access to WordPress, Notion, GitHub, and Vercel APIs through one simple endpoint.

## 🎯 What This Solves

Instead of sharing Skills with API keys embedded (security risk), you:
1. Deploy YOUR OWN hub
2. Add YOUR API keys (server-side, secure)
3. Whitelist ONLY your hub URL
4. Use ONE tiny router Skill

**Result:** Your keys stay server-side. No one can steal them. You control everything.

---

## ⚡ Quick Setup (5 Minutes)

### Step 1: Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/WillCureton76/skills-hub-template)

Click the button above. Vercel will ask for environment variables:

### Step 2: Add Your API Keys

When prompted, add these environment variables:

```
WORDPRESS_URL=https://your-site.com
WORDPRESS_USERNAME=your-email@example.com
WORDPRESS_PASSWORD=your-app-password

NOTION_TOKEN=secret_xxxxxxxxxxxxx

GITHUB_TOKEN=ghp_xxxxxxxxxxxxx

VERCEL_TOKEN=xxxxxxxxxxxxx
```

### Step 3: Deploy!

Click "Deploy". Vercel will build and deploy your hub.

You'll get a URL like: `https://your-hub-abc123.vercel.app`

### Step 4: Download the Router Skill

Download [skill-router.md](./skill-router.md) from this repo.

Edit the `HUB_URL` line to match your deployment URL:

```python
HUB_URL = "https://your-hub-abc123.vercel.app"
```

### Step 5: Upload to Claude

Upload `skill-router.md` to Claude Skills.

**Done!** Claude can now call your hub securely.

---

## 🔒 Security Model

```
Claude Environment:
├─ Network: Whitelist ONLY your-hub.vercel.app
├─ Skill: Simple router (no API keys)
└─ Calls: POST to your-hub.vercel.app/skill-call

Your Hub (Vercel):
├─ API keys (YOUR env vars, server-side)
├─ Skills code (YOUR logic)
└─ You control everything
```

**Why This is Secure:**
- ✅ API keys never touch Claude
- ✅ Everyone hosts their own hub
- ✅ Network whitelisting prevents data exfiltration
- ✅ You control the infrastructure
- ✅ Open source - audit the code

---

## 📚 Available Skills

### WordPress
- `wordpress_create_post` - Create posts
- `wordpress_get_posts` - Get posts  
- `wordpress_update_post` - Update posts
- `wordpress_delete_post` - Delete posts
- `wordpress_upload_media` - Upload media

### Notion
- `notion_query_database` - Query databases
- `notion_create_page` - Create pages
- `notion_update_page` - Update pages
- `notion_get_page` - Get page details
- `notion_append_blocks` - Add content to pages

### GitHub
- `github_list_repos` - List repositories
- `github_create_repo` - Create repositories
- `github_get_repo` - Get repo details
- `github_create_file` - Create files
- `github_update_file` - Update files
- `github_create_issue` - Create issues
- `github_list_issues` - List issues

### Vercel
- `vercel_list_projects` - List projects
- `vercel_create_project` - Create projects
- `vercel_create_env_var` - Add environment variables
- `vercel_list_env_vars` - List environment variables
- `vercel_list_deployments` - List deployments

---

## 🧪 Testing Your Hub

After deployment, test the endpoint:

```bash
curl -X POST https://your-hub.vercel.app/skill-call \
  -H "Content-Type: application/json" \
  -d '{
    "skill": "github_list_repos",
    "params": {"per_page": 5}
  }'
```

Or visit: `https://your-hub.vercel.app/` for the health check.

---

## 🛠️ How It Works

### The Hub (This Repo)
```python
@app.post("/skill-call")
async def skill_call(request):
    payload = await request.json()
    skill = payload["skill"]
    params = payload["params"]
    
    # Route to the right function
    result = SKILLS[skill](**params)
    return result
```

### The Router Skill (What you upload to Claude)
```python
import requests

HUB_URL = "https://your-hub.vercel.app"

def call_skill(skill, **params):
    response = requests.post(
        f"{HUB_URL}/skill-call",
        json={"skill": skill, "params": params}
    )
    return response.json()
```

**That's it.** Simple HTTP. No MCP complexity. Just works.

---

## 📖 Usage Examples

### From Claude

Once you've uploaded the router Skill, Claude can call your hub:

```python
# Create a Notion page
call_skill("notion_create_page", 
    parent={"page_id": "abc123"},
    properties={"Name": {"title": [{"text": {"content": "New Page"}}]}}
)

# Create a GitHub repo
call_skill("github_create_repo",
    name="my-new-repo",
    description="Created via Skills Hub",
    private=False
)

# Create a WordPress post
call_skill("wordpress_create_post",
    title="Hello World",
    content="<p>My first post!</p>",
    status="publish"
)
```

---

## 🔧 Customization

### Adding More Skills

1. Create a new file in `skills/` (e.g., `skills/slack.py`)
2. Add functions for your API
3. Import in `api/index.py`
4. Add to the `SKILLS` dictionary

### Updating Environment Variables

Go to your Vercel dashboard:
1. Select your project
2. Settings → Environment Variables
3. Add/Edit variables
4. Redeploy

---

## 🚨 Important Notes

### Network Whitelisting

Configure Claude to ONLY allow your hub URL:
- Settings → Network → Whitelist
- Add: `your-hub.vercel.app`

This prevents malicious Skills from calling other URLs.

### API Key Security

- Never commit API keys to Git
- Always use environment variables
- Rotate keys regularly
- Use scoped tokens when possible

---

## 📝 License

MIT License - Feel free to fork and customize!

---

## 🙏 Credits

Created by Will Cureton as part of the "Skills as MCP Alternative" discovery.

**The Innovation:**  
Instead of building MCP servers with complex protocols, we discovered that Skills + Python + network access creates instant API connectors with zero infrastructure.

This template is the "safe sharing" pattern - everyone hosts their own hub, so API keys stay secure.

---

## 🐛 Issues?

Open an issue on GitHub or check the [Troubleshooting Guide](./TROUBLESHOOTING.md).

---

**Happy hacking!** 🎉
