################################################################################
# AI_Data_Agent
################################################################################
Python-based AI Data Agent for Bookstores
Analyzes sales and inventory data, applies Pareto analysis, generates weekly Excel reports,
summarizes insights using AI, and optionally emails reports automatically.

################################################################################
# Project Overview
################################################################################
AI_Data_Agent is a production-ready Python project designed for independent bookstores
selling on platforms like Amazon. Its goal is to help store owners make data-driven decisions
by providing actionable insights about sales, profitability, and inventory health.

Key features:
- Connects to a MariaDB/MySQL database (or uses sample data in DEV mode)
- Performs Pareto analysis (80/20 rule) on sales, profit, and inventory
- Generates Excel reports for weekly sales, profitability, and inventory recommendations
- Uses AI (OpenAI GPT) to generate natural language summaries of data
- Optionally automates sending reports via email

################################################################################
# Folder Structure
################################################################################
AI_Data_Agent/
├── main.py                  # Main script to run analysis and generate reports
├── scheduler.py             # Script to schedule weekly report generation and email
├── config.py                # Configuration file with DB, OpenAI, and email placeholders
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Ignore reports, temp files, etc.
├── reports/                 # Folder for generated Excel reports
└── utils/                   # Helper modules
    ├── db_utils.py          # Database connection and data fetch
    ├── analysis.py          # Pareto analysis and inventory performance
    ├── reporting.py         # Excel report generation
    └── ai_summary.py        # AI summary generation using OpenAI

################################################################################
# Setup Instructions
################################################################################
1. Install dependencies:
   pip install -r requirements.txt

2. Configure credentials:
   - Database credentials (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
   - OpenAI API key (OPENAI_API_KEY)
   - Email credentials (optional for automated emailing)

3. Run the project:
   - Generate reports manually:
     python main.py
   - Schedule weekly automated reports (with email):
     python scheduler.py

################################################################################
# Development Mode
################################################################################
If you do not have a database, set MODE = 'DEV' in config.py.
- This will use sample data for testing and development.
- AI summary will return a dummy message.

################################################################################
# Features in Detail
################################################################################
1. Sales Analysis:
   - Top/bottom items by quantity sold
   - Highlights fastest and slowest selling books

2. Profitability Analysis:
   - Top/bottom items by gross profit
   - Helps identify most and least profitable products

3. Inventory Health:
   - Analyzes stock age and quantity
   - Flags items for restocking or markdown

4. AI Summary:
   - Uses OpenAI GPT to summarize report data in natural language
   - Provides clear insights for store owners

5. Automated Reporting:
   - Scheduler runs weekly to generate and optionally email reports
   - Reports saved in reports/ folder

################################################################################
# Usage Example
################################################################################
from utils.db_utils import fetch_data
from utils.reporting import generate_reports

sales_df, inventory_df = fetch_data()
report_file, summary_text = generate_reports(sales_df, inventory_df)

print(f"Report generated: {report_file}")
print(summary_text)

################################################################################
# License
################################################################################
Currently, no license is added. You may add an MIT License later if you want others
to use and share the project freely.

################################################################################
# Notes
################################################################################
- Ensure reports/ folder exists (or will be created automatically)
- For email automation, less secure app access may be needed for Gmail
- AI integration requires a valid OpenAI API key
- .gitignore is included to ignore reports/, __pycache__/, and future zip files

################################################################################
# Future Improvements
################################################################################
- Integration with other marketplaces (eBay, Shopify, etc.)
- More advanced AI analysis (trend prediction, category insights)
- Interactive dashboard for visual reports
