GenAI Project Setup in Windows (VS Code + venv + uv)

📁 1. Create Project Folder
mkdir genai-project
cd genai-project

🧪 2. Create Virtual Environment
python -m venv .venv


▶️ Activate Environment

Windows (PowerShell):

.venv\Scripts\activate

⚡ 3. Install uv (if not installed)
pip install uv

👉 Verify:

uv --version
📦 4. Install Dependencies using uv
uv add streamlit openai python-dotenv

👉 This will:

Install packages
Create/update pyproject.toml
Manage dependencies cleanly ✅
🔐 5. Create .env File
OPENAI_API_KEY=your_api_key_here
📄 6. Create .gitignore
.venv/
.env
__pycache__/
