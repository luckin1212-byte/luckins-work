
# NovaMind – AI-Powered Marketing Content Pipeline

**Live Demo:** [luckins-work-4qkozj3rsp5oze9ejqcpkq.streamlit.app](https://luckins-work-4qkozj3rsp5oze9ejqcpkq.streamlit.app)

NovaMind is a lightweight, automated pipeline that generates, distributes, and analyzes marketing content using **OpenAI** and **Streamlit**.
It simulates HubSpot-style CRM workflows to deliver personalized newsletters and evaluate performance.


## Architecture

```
User → Streamlit UI → AI Generator → CRM Sender → Performance Analyzer → Insights
```

**Modules**

| File                      | Description                          |
| ------------------------- | ------------------------------------ |
| `ai_generator.py`         | Generates blog + persona newsletters |
| `crm_newsletter.py`       | Sends or simulates email campaigns   |
| `performance_analysis.py` | Simulates engagement & AI summary    |
| `dashboard.py`            | Streamlit app connecting all modules |

---

## Tech Stack

* **Python 3.9+**, **Streamlit**
* **OpenAI API** (`gpt-4o-mini`)
* **Requests**, **dotenv**, **pandas**
* *(Optional)* HubSpot API for real email campaigns

---

## Run Locally

```bash
git clone https://github.com/<your-username>/nova-ai-marketing-pipeline.git
cd nova-ai-marketing-pipeline
pip install -r requirements.txt
```

Create `.env`:

```
OPENAI_API_KEY=sk-yourkey
# Optional HubSpot
HUBSPOT_API_KEY=pat-yourkey
HUBSPOT_EMAIL_ID=123456789
```

Run Streamlit:

```bash
streamlit run dashboard.py
```

Open → [http://localhost:8501](http://localhost:8501)

---

## Example Outputs

**Campaign Log**

```json
{"campaign_title": "AI in Creative Automation", "recipients": ["alice@startup.com"]}
```

**Performance Log**

```json
{"Founder": {"open_rate": 0.52, "click_rate": 0.31}}
```

---

## Future Ideas

* Real HubSpot campaign integration
* AI subject line A/B testing
* Dashboard analytics with charts


