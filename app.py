from flask import Flask, render_template, send_from_directory

from flask_frozen import Freezer


app = Flask(__name__)
freezer = Freezer(app)
app.jinja_env.globals['enumerate'] = enumerate

# ── DATA ──────────────────────────────────────────────────────────────────────

PROFILE = {
    "name": "Saeed Fadaei",
    "role": "PhD Researcher in Computer Science",
    "org": "University of Surrey",
    "org_url": "https://www.surrey.ac.uk/",
    "location": "Surrey, UK",
    "email": "saeed.fadaei1996@gmail.com",
    "linkedin": "https://linkedin.com/in/iamsaeedfadaei",
    "github": "https://github.com/nyxaeed",
    "bio": (
        "PhD researcher at the University of Surrey specialising in LEO satellite "
        "Networks, Internet Infrastructure, and CDN Architectures. <br>"
        "Maintainer of <a href=\"https://leoscope.surrey.ac.uk\" style=\"text-decoration: underline;\">LEOScope</a>"
    ),
    "tagline": "I study the internet architecture for now...",
    "avatar": "/static/img/avatar.png",
}

INTERESTS = [
    "LEO Satellite Networks",
    "Internet Measurement",
    "Network Congestion Control",
    "Privacy Enhancing Technologies",
    "Distributed Systems",
]

EDUCATION = [
    {
        "degree": "PhD in Computer Science",
        "institution": "University of Surrey",
        "location": "Guildford, UK",
        "period": "Oct 2024 – Present",
        "detail": "",
    },
    {
        "degree": "M.Sc. in Computer Systems Networking & Telecommunications",
        "institution": "University of Isfahan",
        "location": "Isfahan, Iran",
        "period": "2019 – 2023",
        "detail": "Thesis: Network Slicing Based Mobility Management in 5G Networks and Beyond: QoS Improvement Approach",
    },
    {
        "degree": "B.Sc. in Computer Engineering",
        "institution": "Hamedan University of Technology",
        "location": "Hamedan, Iran",
        "period": "2014 – 2018",
        "detail": "Thesis: Blockchain in Cloud Computing: Security Challenges",
    },
]

SKILLS = [
    {
        "category": "Languages",
        "icon": "💻",
        "tools": ["Python", "JavaScript", "Bash", "SQL", "HTML/CSS", "Go", "C/C++"],
    },
    {
        "category": "ML & Data",
        "icon": "🧠",
        "tools": ["PyTorch", "TensorFlow", "OpenCV", "Pandas", "NumPy", "scikit-learn"],
    },
    {
        "category": "Frameworks",
        "icon": "⚙️",
        "tools": ["FastAPI", "Django", "Flask", "Sanic", "React"],
    },
    {
        "category": "DevOps & Infra",
        "icon": "🐳",
        "tools": ["Docker", "Kubernetes", "Ansible", "Kafka", "Redis", "Git"],
    },
    {
        "category": "Databases",
        "icon": "🗄️",
        "tools": ["PostgreSQL", "MySQL", "MongoDB"],
    },
    # {
    #     "category": "Research Tools",
    #     "icon": "📡",
    #     "tools": ["Wireshark", "iperf3", "Scapy", "LaTeX", "NetworkX", "Tailscale"],
    # },
]

EXPERIENCE = [
    {
        "title": "PhD Researcher",
        "company": "University of Surrey",
        "company_url": "https://www.surrey.ac.uk/",
        "location": "Guildford, UK",
        "period": "Oct 2024 – Present",
        "current": True,
        "bullets": [
            "Investigating LEO satellite network measurement and solar storm impacts on orbital internet infrastructure.",
            "Built the LEOScope testbed — a global measurement network spanning Northern Canada to Antarctica.",
            "ACM SIGMETRICS 2026 paper accepted on 1.5 years of solar storm measurement data.",
            "🏆 Best of CCR — ACM SIGCOMM 2025.",
        ],
    },
    {
        "title": "AI Research Engineer",
        "company": "University of Surrey",
        "company_url": "https://www.surrey.ac.uk/",
        "location": "Guildford, UK",
        "period": "Dec 2023 – Oct 2024",
        "current": False,
        "bullets": [
            "Developed LEOScope, a scalable global testbed for measuring LEO satellite network performance.",
            "Engineered Risk Playground (AP4L project) — a gamified privacy education tool.",
            "Developed Transition Guardian browser plugin; resulted in ASONAM 2025 publication.",
        ],
    },
    {
        "title": "Software Team Lead",
        "company": "Hezardastan Group (Karnameh)",
        "company_url": "",
        "location": "Tehran, Iran",
        "period": "Aug 2022 – Dec 2023",
        "current": False,
        "bullets": [
            "Refactored feature-freeze system, quadrupling the user base.",
            "Implemented real-time car inspection offer system; reduced operation costs by 80% (5× efficiency gain).",
            "Built automated price-estimation bot used as an industry reference for car pricing.",
            "Developed notification system from scratch to improve company–user communication.",
        ],
    },
    {
        "title": "Software Backend Team Lead",
        "company": "Panco",
        "company_url": "",
        "location": "Tehran, Iran",
        "period": "May 2022 – Aug 2022",
        "current": False,
        "bullets": [
            "Developed three new games driving a 3× increase in company revenue.",
            "Clustered the data layer, increasing system throughput by 4× and improving fault tolerance.",
            "Implemented a queue manager for seamless real-time user experience.",
        ],
    },
    {
        "title": "Software Engineer & Blockchain Researcher",
        "company": "Nobitex (Cryptocurrency Exchange)",
        "company_url": "",
        "location": "Tehran, Iran",
        "period": "May 2021 – May 2022",
        "current": False,
        "bullets": [
            "Implemented multi-layer transaction validation for AML compliance.",
            "Developed the core wallet system and an AI-based authentication system.",
            "Built automated deployment pipelines and configuration management systems.",
        ],
    },
    {
        "title": "Backend Engineer",
        "company": "Shaya Smart Solutions",
        "company_url": "",
        "location": "Tehran, Iran",
        "period": "Apr 2020 – May 2021",
        "current": False,
        "bullets": [
            "Developed a real-time trading core for the Iranian stock market (Agah Broker).",
            "Implemented an optimised pipeline to crawl and annotate Farsi multimedia and documents.",
        ],
    },
]

PROJECTS = [
    {
        "title": "LEOScope: Global LEO Testbed",
        "tags": ["Satellite Networks", "Measurement", "Starlink"],
        "summary": (
            "A scalable global testbed measuring network performance across LEO satellite providers "
            "— spanning from Northern Canada to Antarctica."
        ),
        "badge": "🏆 Best of CCR · ACM SIGCOMM 2025",
        "bullets": [
            "Deployed probes from Northern Canada to McMurdo Station, Antarctica",
            "Long-term framework studying Geomagnetic Storms (Solar Cycle 25)",
            "Characterised TCP congestion control over ISL paths",
        ],
        "paper_url": "",
        "code_url": "",
    },
    {
        "title": "Solar Storms & Orbital Internet Resilience",
        "tags": ["Measurement", "Solar Storms", "LEO/MEO/GEO"],
        "summary": (
            "1.5 years of continuous measurement mapping the impact of extreme solar storms "
            "across all orbital regimes."
        ),
        "badge": "ACM SIGMETRICS 2026 — Accepted",
        "bullets": [
            "Correlated Kp index & X-ray flux with latency, loss, and throughput KPIs",
            "Compared Starlink, OneWeb, and GEO providers during X-class flares",
            "First large-scale empirical study of its kind",
        ],
        "paper_url": "",
        "code_url": "",
    },
    {
        "title": "CDN Architecture for LEO — VDC",
        "tags": ["CDN", "LEO", "Video Streaming"],
        "summary": (
            "Virtual Delivery Constellations (VDC): novel CDN placement strategies "
            "optimised for LEO satellite constellation topology."
        ),
        "badge": "ACM HotNets 2024",
        "bullets": [
            "Optimised PoP placement within Starlink-class constellations",
            "Power-aware satellite selection for content delivery",
            "Break-even analysis vs ground-based CDN",
        ],
        "paper_url": "",
        "code_url": "",
    },
    {
        "title": "Transition Guardian — Privacy Plugin",
        "tags": ["Privacy", "ML", "Browser Extension"],
        "summary": (
            "On-device AI browser plugin that detects and blocks accidental sharing of "
            "sensitive self-disclosure data — zero external data leakage."
        ),
        "badge": "ASONAM 2025",
        "bullets": [
            "Runs entirely on-device inside the browser",
            "Detects minority status indicators before form submission",
            "Targets users during high-risk life transitions",
        ],
        "paper_url": "",
        "code_url": "",
    },
    {
        "title": "Shrinking VOD Traffic via Rényi-Entropic OT",
        "tags": ["Video Streaming", "Optimisation", "CDN"],
        "summary": (
            "Optimal transport-based approach to reduce VOD traffic volume using "
            "Rényi entropy regularisation."
        ),
        "badge": "ACM SIGMETRICS 2024",
        "bullets": [
            "Applied Rényi-entropic optimal transport to video chunk scheduling",
            "Significant reduction in redundant VOD traffic",
        ],
        "paper_url": "",
        "code_url": "",
    },
]

PUBLICATIONS = [
    {
        "title": "A Comprehensive Study of Satellite Network Performance During 1.5 years of Solar Storm (May 2024–Oct 2025)",
        "venue": "ACM SIGMETRICS 2026",
        "note": "",
        "award": "",
        "url": "",
    },
    {
        "title": "LEOScope: Building a Global Testbed for Low-Earth Orbit Satellite Networks",
        "venue": "ACM SIGCOMM CCR 2025",
        "note": "",
        "award": "🏆 Best of CCR Award",
        "url": "",
    },
    {
        "title": "Storms Above, Disruptions Below: Mapping The Impact of Extreme Solar Storms Across Orbital Regimes",
        "venue": "ACM SIGCOMM 2025",
        "note": "Student Research Competition Nominee",
        "award": "",
        "url": "",
    },
    {
        "title": "Protecting Vulnerable Voices: Synthetic Dataset Generation for Self-Disclosure Detection",
        "venue": "ASONAM 2025",
        "note": "",
        "award": "",
        "url": "",
    },
    {
        "title": "It's a bird? It's a plane? It's CDN!",
        "venue": "ACM HotNets 2024",
        "note": "",
        "award": "",
        "url": "",
    },
    {
        "title": "Shrinking VOD Traffic via Rényi-Entropic Optimal Transport",
        "venue": "ACM SIGMETRICS 2024",
        "note": "",
        "award": "",
        "url": "",
    },
    {
        "title": "Blockchain in Cloud Computing and Security Challenges",
        "venue": "CITCOMP03 2018",
        "note": "",
        "award": "",
        "url": "",
    },
]

AWARDS = [
    {
        "title": "Best of CCR",
        "event": "ACM SIGCOMM 2025",
        "date": "Sep 2025",
        "paper": "LEOScope: Building a Global Testbed for Low-Earth Orbit Satellite Networks",
        "icon": "🏆",
    },
    {
        "title": "Student Research Competition (SRC) Nomination",
        "event": "ACM SIGCOMM 2025",
        "date": "Sep 2025",
        "paper": "Storms Above, Disruptions Below: Mapping the Impact of Extreme Solar Storms Across Orbital Regimes",
        "icon": "🎓",
    },
]


# ── ROUTES ────────────────────────────────────────────────────────────────────

@app.route('/Users/<path:filename>')
def serve_user_files(filename):
    return send_from_directory('/Users', filename)

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        interests=INTERESTS,
        education=EDUCATION,
        skills=SKILLS,
        experience=EXPERIENCE,
        projects=PROJECTS,
        publications=PUBLICATIONS,
        awards=AWARDS,
    )


if __name__ == "__main__":
    freezer.freeze()
    app.run(debug=True, port=1124)
