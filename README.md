# Saeed Fadaei — Portfolio (Flask)

A personal academic portfolio site built with Python + Flask.  
All content lives in `app.py` as plain Python dicts — no database, no CMS.

---

## 🏃 Run Locally

### Prerequisites

- Python 3.10 or newer ([python.org](https://python.org))
- pip (comes with Python)

### 1. Clone / download the project

```bash
# If you cloned from GitHub:
git clone https://github.com/nyxaeed/nyxaeed.github.io.git
cd nyxaeed.github.io

# Or just unzip the downloaded folder and cd into it:
cd saeed-flask
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# macOS / Linux
source venv/bin/activate

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

```bash
python app.py
```

Open **http://localhost:5000** in your browser. ✅

The server auto-reloads when you edit `app.py` or any template.

---

## 📝 Editing Your Content

Everything is in **`app.py`** — find the `# ── DATA ──` section at the top.

| Variable       | What it controls                       |
| -------------- | -------------------------------------- |
| `PROFILE`      | Name, role, bio, tagline, social links |
| `SKILLS`       | Skill groups and items                 |
| `EXPERIENCE`   | Work history (title, company, bullets) |
| `EDUCATION`    | Degrees and institutions               |
| `PROJECTS`     | Research project cards                 |
| `PUBLICATIONS` | Publication list                       |
| `AWARDS`       | Honors and awards                      |

After editing, just save — the dev server reloads automatically.

### Adding your photo

Place a photo at `static/img/avatar.jpg` (square crop recommended).  
If no photo is found, the site shows your initials **SF** as a fallback.

---

## 🚀 Deploy to a Server (Production)

### Option A: Any Linux VPS (Hetzner, DigitalOcean, Linode…)

```bash
# On the server, install deps
pip install -r requirements.txt

# Run with Gunicorn (production WSGI server)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Point Nginx to port 8000 as a reverse proxy.

### Option B: Railway (free tier, no config needed)

1. Push code to a GitHub repo
2. Go to [railway.app](https://railway.app) → **New Project → Deploy from GitHub repo**
3. Railway auto-detects Flask and deploys — live URL in ~1 minute

### Option C: Render (free tier)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Set **Start Command**: `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
4. Deploy — free HTTPS URL provided automatically

### Option D: GitHub Pages (static export — advanced)

GitHub Pages only hosts static files. To use it with Flask, use `Frozen-Flask`:

```bash
pip install Frozen-Flask
```

Add to `app.py`:

```python
from flask_frozen import Freezer
 freezer = Freezer(app)
if __name__ == '__main__':
    freezer.freeze()  # generates /build folder
```

Then push the `/build` folder contents to your `gh-pages` branch.

---

## 📁 Project Structure

```
saeed-flask/
├── app.py                  ← Flask app + ALL content data
├── requirements.txt
├── README.md
├── templates/
│   └── index.html          ← Jinja2 template (HTML structure)
└── static/
    ├── css/
    │   └── style.css       ← All styles
    ├── js/
    │   └── main.js         ← Scroll effects, nav
    └── img/
        └── avatar.jpg      ← Your photo (add this yourself)
```
