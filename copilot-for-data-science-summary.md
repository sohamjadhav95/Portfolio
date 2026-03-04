# Data Science Copilot

**Dual-mode AI data science assistant with Graph-Based DAG execution engine.**

Data Science Copilot is a full-stack web application that allows users to interact with CSV datasets using natural language. It features two execution modes:
- **Normal Mode:** For single-step AI operations (immediate execution).
- **Pro Mode:** For multi-step planned pipelines, driven by a DAG (Directed Acyclic Graph) execution engine.

## Key Features

- **Graph-Based Execution (Pro Mode):** Generates and executes a Directed Acyclic Graph plan. Provides step-by-step progress tracking, sandboxed execution, retry mechanisms, and automatic re-planning up to 2 times on failure.
- **Dataset Profiling:** Full column statistics, correlation matrices, and warning generation prior to planning pipelines.
- **Three-Tier Model Routing System:**
  - *Heavy:* DAG planning, re-planning, final summaries (Groq DeepSeek R1 / Gemini 2.0 Flash)
  - *Mid:* Code generation per node, retries (Groq Llama 3.3 70B)
  - *Light:* Intent classification, complexity detection (Groq Llama 3.1 8B)
- **Safe Sandboxed Execution Context:** Strict timeout controls and bounded memory limits for generated artifacts and dataframes.

## Tech Stack

- **Backend:** Python 3.9+, Flask, SQLAlchemy, Flask-CORS
- **AI/ML Integration:** Groq, OpenRouter API wrappers with automatic fallback routing
- **Data Processing:** Pandas, NumPy, SciPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Frontend:** HTML, CSS, JavaScript (Vanilla SPA architecture)
- **Auth:** JWT-based authentication
