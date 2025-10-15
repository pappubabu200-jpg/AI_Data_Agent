from utils.db_utils import fetch_data
from utils.reporting import generate_reports

sales_df, inventory_df = fetch_data()
report_file, summary_text = generate_reports(sales_df, inventory_df)

print(f"Report generated: {report_file}")
print(summary_text)
