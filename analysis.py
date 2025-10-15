import pandas as pd

def pareto_analysis(df, value_col, percentages=[1,5,10,20]):
    df_sorted = df.sort_values(value_col, ascending=False).reset_index(drop=True)
    results = {}
    for p in percentages:
        top_n = max(1, int(len(df) * p / 100))
        bottom_n = max(1, int(len(df) * p / 100))
        results[f'top_{p}_percent'] = df_sorted.head(top_n)
        results[f'bottom_{p}_percent'] = df_sorted.tail(bottom_n)
    return results

def inventory_performance(inventory_df):
    inventory_df['performance_score'] = inventory_df['stock_quantity'] / (inventory_df['stock_age_days']+1)
    return inventory_df
