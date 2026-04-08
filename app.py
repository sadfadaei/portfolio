from flask import Flask, render_template, send_from_directory

from flask_frozen import Freezer


app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True
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
    "github": "https://github.com/sadfadaei",
    "bio": (
        "PhD researcher at the University of Surrey specialising in LEO satellite "
        "Networks, Internet Infrastructure, and CDN Architectures. <br>"
        "Maintainer of <a href=\"https://leoscope.surrey.ac.uk\" style=\"text-decoration: underline;\">LEOScope</a>"
    ),
    "tagline": "I study the internet architecture for now...",
    "avatar": "img/avatar.png",
    "cv_pdf": "cv.pdf",
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
        "paper_count": 1,
        "award_text": "🏆 Awarded",
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
        "badge": "ACM SIGMETRICS 2026",
        "bullets": [
            "Correlated Kp index & X-ray flux with latency, loss, and throughput KPIs",
            "Compared Starlink, OneWeb, and GEO providers during X-class flares",
            "First large-scale empirical study of its kind",
        ],
        "paper_count": 2,
        "award_text": "🎓 SRC Award Nominated",
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
        "paper_count": 1,
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
        "paper_count": 1,
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
        "paper_count": 1,
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
        "url": "https://dl.acm.org/doi/10.1145/3788084",
        "bibtex": """@article{10.1145/3788084,
author = {Fadaei, Saeed and Raman, Aravindh and Sharma, Prince Bhardwaj Pawankumar and Sastry, Nishanth},
title = {A Comprehensive Study of Satellite Network Performance During Severe or Extreme Geomagnetic Storms over 1.5 Years (May 2024 – Oct 2025)},
year = {2026},
issue_date = {March 2026},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {10},
number = {1},
url = {https://doi.org/10.1145/3788084},
doi = {10.1145/3788084},
abstract = {Geomagnetic or Solar storms are often associated with disruptions in satellite communications, yet their impact on real-world performance remains under-explored even as satellite broadband usage grows exponentially due to Starlink and others. This is particularly critical now, as we are currently near the peak of a so-called solar cycle, which is associated with increased solar storm activity. Using data from a combination of active and passive measurements, we conduct a comprehensive study of the network effects all the 15 strong, severe or extreme solar storms that occurred in the past 1.5 years (May 2024 – Oct 2025). We bring together three different datasets: First, we use LEOScope, a public global LEO testbed to schedule controlled and fine-grained measurements at seven locations globally during solar storms. The results reveal a severe degradation in performance during such events, manifesting as a 20\\% decrease in throughput, a 10\\% increase in latency, and a doubling of the packet loss rate. Second, we use data from M-Lab (Google) speedtests conducted by satellite network users, to enhance global coverage. We obtain over 4 million records, which allows us to do a comparative analysis by studying variation in performance degradation across different latitudes in the same longitude range (over the North and South American continents) and effects across similar (40°–55°) latitudes during periods of high geomagnetic disturbance. Finally, we supplement this with data from Cloudflare AIM, which, in addition to common network speed metrics, also provide an estimation of how this affects user experience for common applications such as gaming, streaming and VoIP. These findings provide new insights into how space weather affects LEO, MEO, and GEO satellite Networks.},
journal = {Proc. ACM Meas. Anal. Comput. Syst.},
month = mar,
articleno = {2},
numpages = {23},
keywords = {satellite networks, geomagnetic storms, solar cycle, leo constellations, network measurement, starlink, performance analysis, space weather}
}"""
    },
    {
        "title": "LEOScope: Building a Global Testbed for Low-Earth Orbit Satellite Networks",
        "venue": "ACM SIGCOMM CCR 2025",
        "note": "",
        "award": "🏆 Best of CCR Award",
        "url": "https://dl.acm.org/doi/10.1145/3750832.3750835",
        "bibtex": """@article{10.1145/3750832.3750835,
author = {Fadaei, Saeed and Tiwari, Shubham and Taneja, Aryan and Bhushan, Saksham and Kassem, Mohamed and Raman, Aravindh and Bhattacherjee, Debopam and Qiu, Lili and Woodward, Alan and Sastry, Nishanth},
title = {LEOScope: Building a Global Testbed for Low-Earth Orbit Satellite Networks},
year = {2025},
issue_date = {April 2025},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {55},
number = {2},
issn = {0146-4833},
url = {https://doi.org/10.1145/3750832.3750835},
doi = {10.1145/3750832.3750835},
abstract = {Low-Earth Orbit (LEO) satellite mega-constellations which offer broad coverage and low latencies offer a revolutionary new connectivity option. However, they also have complex orbital dynamics leading to continuous latency changes and frequent satellite hand-offs. We are building a globally spanning testbed, LEOScope1, to quantify the performance opportunities and bottlenecks of such networks. This paper discusses the unique features we incorporated into LEOScope to adapt it to the dynamics of LEO networks and to enable experimentation on volunteer nodes. To demonstrate the broad utility of the testbed, we report Starlink performance across countries using LEOScope. Our primary aim is to describe the testbed and announce its availability to the SIGCOMM community for non-commercial research activities.},
journal = {SIGCOMM Comput. Commun. Rev.},
month = jul,
pages = {13–21},
numpages = {9},
keywords = {satellite networks, LEO constellations, network testbed, performance measurement, orbital dynamics}
}"""
    },
    {
        "title": "Storms Above, Disruptions Below: Mapping The Impact of Extreme Solar Storms Across Orbital Regimes",
        "venue": "ACM SIGCOMM 2025",
        "note": "Student Research Competition Nominee",
        "award": "",
        "url": "https://doi.org/10.1145/3744969.3748456",
        "bibtex": """@inproceedings{10.1145/3744969.3748456,
author = {Fadaei, Saeed and Raman, Aravindh and Sastry, Nishanth},
title = {Storms Above, Disruptions Below: Mapping The Impact of Extreme Solar Storms Across Orbital Regimes},
year = {2025},
isbn = {9798400720260},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3744969.3748456},
doi = {10.1145/3744969.3748456},
abstract = {Low Earth Orbit (LEO) constellations like Starlink now serve millions of users, including in disaster zones and unserved regions. However, LEO systems operate in a highly dynamic space environment, where solar activity can trigger geomagnetic storms that disturb ionospheric propagation, satellite drag, and radio link quality. In this work, we present a cross-layer empirical study of how the most intense solar storms of Solar Cycle 25---particularly those in May and October 2024---impacted the performance of LEO networks. Using active testbed probes (via LEOScope) and satellite telemetry we correlate geomagnetic storm activity with degradations in throughput, latency, and link stability. Our analysis reveals geographically skewed performance drops, latency inflation, and increased session drops. We conclude with a vision for a future prediction system that integrates solar observatory feeds, satellite tracking, and crowd-sourced measurements to forecast Internet disruptions under extreme space weather.},
booktitle = {Proceedings of the ACM SIGCOMM 2025 Posters and Demos},
pages = {118–120},
numpages = {3},
keywords = {Low Earth Orbit constellations, Starlink, cross-layer analysis, geomagnetic storms, ionospheric propagation, network performance, satellite drag, solar activity, space weather},
location = {Coimbra, Portugal},
series = {ACM SIGCOMM Posters and Demos '25}
}"""
    },
    {
        "title": "Protecting Vulnerable Voices: Synthetic Dataset Generation for Self-Disclosure Detection",
        "venue": "ASONAM 2025",
        "note": "",
        "award": "",
        "url": "https://link.springer.com/chapter/10.1007/978-3-032-13821-7_1",
        "bibtex": """@incollection{jangra2026protecting,
  title={Protecting Vulnerable Voices: Synthetic Dataset Generation for Self-disclosure Detection},
  author={Jangra, S. and De, S. and Sastry, N. and Fadaei, S.},
  booktitle={Social Networks Analysis and Mining},
  pages={3--18},
  year={2026},
  editor={An, A. and Cuzzocrea, A. and Hu, H.},
  publisher={Springer Nature Switzerland},
  url={https://link.springer.com/chapter/10.1007/978-3-032-13821-7_1}
}"""
    },
    {
        "title": "It's a bird? It's a plane? It's CDN!",
        "venue": "ACM HotNets 2024",
        "note": "",
        "award": "",
        "url": "https://dl.acm.org/doi/10.1145/3696348.3696879",
        "bibtex": """@inproceedings{10.1145/3696348.3696879,
author = {Bose, Rohan and Fadaei, Saeed and Mohan, Nitinder and Kassem, Mohamed and Sastry, Nishanth and Ott, J\\\"{o}rg},
title = {It's a bird? It's a plane? It's CDN!: Investigating Content Delivery Networks in the LEO Satellite Networks Era},
year = {2024},
isbn = {9798400712722},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3696348.3696879},
doi = {10.1145/3696348.3696879},
abstract = {Content Delivery Networks (CDNs) have been pivotal in the dramatic evolution of the Internet, handling the majority of data traffic for billions of connected users. Low-Earth-Orbit (LEO) satellite networks, such as Starlink, aim to revolutionize global connectivity by providing high-speed, low-latency Internet to remote regions. However, LEO satellite networks (LSNs) face challenges integrating with traditional CDNs, which rely on geographical proximity for efficient content delivery - a method that clashes with the operational dynamics of LSNs. In this paper, we scrutinize the operation of CDNs in the context of LSNs, using Starlink as a case study. We develop a browser extension NetMet that performs extensive web browsing experiments from controlled nodes using both Starlink and terrestrial Internet access. Additionally, we analyse crowdsourced speed tests from Starlink users to Cloudflare CDN servers globally. Our results indicate significant performance issues for Starlink users, stemming from the misalignment between terrestrial and satellite infrastructures. We then investigate the potential for SpaceCDNs which integrate CDN infrastructure directly within the LSNs, and show that this approach offers a promising alternative that decreases latencies by over 50\\%, making them comparable with the CDN experience of users behind terrestrial ISPs. Our aim is to stimulate further research and discussion on overcoming the challenges of effective content delivery with growing LSN offerings.},
booktitle = {Proceedings of the 23rd ACM Workshop on Hot Topics in Networks},
pages = {1–9},
numpages = {9},
keywords = {CDN measurements, Internet Measurements, LEO Satellite networks, Starlink},
location = {Irvine, CA, USA},
series = {HotNets '24}
}"""
    },
    {
        "title": "Shrinking VOD Traffic via Rényi-Entropic Optimal Transport",
        "venue": "ACM SIGMETRICS 2024",
        "note": "",
        "award": "",
        "url": "https://dl.acm.org/doi/abs/10.1145/3639033",
        "bibtex": """@article{10.1145/3639033,
author = {Lo, Chi-Jen (Roger) and Marina, Mahesh K. and Sastry, Nishanth and Xu, Kai and Fadaei, Saeed and Li, Yong},
title = {Shrinking VOD Traffic via R\\'{e}nyi-Entropic Optimal Transport},
year = {2024},
issue_date = {March 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {8},
number = {1},
url = {https://doi.org/10.1145/3639033},
doi = {10.1145/3639033},
abstract = {In response to the exponential surge in Internet Video on Demand (VOD) traffic, numerous research endeavors have concentrated on optimizing and enhancing infrastructure efficiency. In contrast, this paper explores whether users' demand patterns can be shaped to reduce the pressure on infrastructure. Our main idea is to design a mechanism that alters the distribution of user requests to another distribution which is much more cache-efficient, but still remains 'close enough' (in the sense of cost) to fulfil each individual user's preference. To quantify the cache footprint of VOD traffic, we propose a novel application of R\\'{e}nyi entropy as its proxy, capturing the 'richness' (the number of distinct videos or cache size) and the 'evenness' (the relative popularity of video accesses) of the on-demand video distribution. We then demonstrate how to decrease this metric by formulating a problem drawing on the mathematical theory of optimal transport (OT). Additionally, we establish a key equivalence theorem: minimizing R\\'{e}nyi entropy corresponds to maximizing soft cache hit ratio (SCHR) --- a variant of cache hit ratio allowing similarity-based video substitutions. Evaluation on a real-world, city-scale video viewing dataset reveals a remarkable 83\\% reduction in cache size (associated with VOD caching traffic). Crucially, in alignment with the above-mentioned equivalence theorem, our approach yields a significant uplift to SCHR, achieving close to 100\\%.},
journal = {Proc. ACM Meas. Anal. Comput. Syst.},
month = feb,
articleno = {7},
numpages = {34},
keywords = {cache-aware video recommendation, renyi entropy, soft cache hit ratio}
}"""
    },
    {
        "title": "Blockchain in Cloud Computing and Security Challenges",
        "venue": "CITCOMP03 2018",
        "note": "",
        "award": "",
        "url": "https://civilica.com/doc/854103",
        "bibtex": """@inproceedings{fadaei2018blockchain,
  title={Blockchain in Cloud Computing and Security Challenges},
  author={Fadaei, Saeed},
  booktitle={CITCOMP03},
  year={2018},
  url={https://civilica.com/doc/854103}
}"""
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
