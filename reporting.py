import pandas as pd
import os
from datetime import datetime
from analysis import pareto_analysis, inventory_performance
from ai_summary import ai_summary

os.makedirs('reports', exist_ok=True)

def generate_reports(sales_df, inventory_df):
    from xlsxwriter import Workbook
    now = datetime.now().strftime("%Y-%m-%d")
    report_path = f'reports/Weekly_Report_{now}.xlsx'
    writer = pd.ExcelWriter(report_path, engine='xlsxwriter')
    workbook  = writer.book

    # Sales Pareto
    sales_pareto = pareto_analysis(sales_df, 'quantity_sold', [5])
    top5 = sales_pareto['top_5_percent']
    bottom5 = sales_pareto['bottom_5_percent']
    top5.to_excel(writer, sheet_name='Top 5% Sales', index=False)
    bottom5.to_excel(writer, sheet_name='Bottom 5% Sales', index=False)

    # Profit Pareto
    profit_pareto = pareto_analysis(sales_df, 'profit', [20])
    top20 = profit_pareto['top_20_percent']
    bottom20 = profit_pareto['bottom_20_percent']
    top20.to_excel(writer, sheet_name='Top 20% Profit', index=False)
    bottom20.to_excel(writer, sheet_name='Bottom 20% Profit', index =False)

    # Inventory
    inventory_df = inventory_performance(inventory_df)
    inv_pareto = pareto_analysis(inventory_df, 'performance_score', [10])
    top10_inv = inv_pareto['top_10_percent']
    bottom10_inv = inv_pareto['bottom_10_percent']
    top10_inv.to_excel(writer, sheet_name='Top 10% Inventory', index=False)
    bottom10_inv.to_excel(writer, sheet_name='Bottom 10% Inventory', index=False)

    # AI Summary
    combined_text = f"Top 5% Sales:\n{top5[['title','quantity_sold']]}" +                     f"\nBottom 5% Sales:\n{bottom5[['title','quantity_sold']]}" +                     f"\nTop 20% Profit:\n{top20[['title','profit']]}" +                     f"\nBottom 20% Profit:\n{bottom20[['title','profit']]}" +                     f"\nTop 10% Inventory:\n{top10_inv[['title','performance_score']]}" +                     f"\nBottom 10% Inventory:\n{inv_pareto['bottom_10_percent'][['title','performance_score']]}"
    summary = ai_summary(combined_text)
    pd.DataFrame({'Summary':[summary]}).to_excel(writer, sheet_name='AI Summary', index=False)

    writer.save()
    return report_path, summary
