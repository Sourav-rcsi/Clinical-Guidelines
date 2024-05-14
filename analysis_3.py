# Importing libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import wilcoxon, mannwhitneyu, friedmanchisquare
import scipy.stats as stats
from op_data import output_data
from plot import data_vis, box_plot, p_plots

def get_google_sheet(path, sheet_name):
    df_col = pd.read_excel(path, sheet_name=sheet_name)
    df_response = df_col.T[1:] # Transpose, rename and remove 1st row
    return df_response


sheet_path = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYNovLb5zqMt-SEIWH7npEOYrqYh8UsglffyUSJ5NksG5FSHshZ5RMQx9Lfbl1e4jaWGpYRfR54lV9/pub?output=xlsx"
df_q1 = get_google_sheet(sheet_path, "Q1")
df_q2 = get_google_sheet(sheet_path, "Q2")
df_q3 = get_google_sheet(sheet_path, "Q3")
df_q1 = df_q1.reset_index(drop=True)
df_q2 = df_q2.reset_index(drop=True)
df_q3 = df_q3.reset_index(drop=True)
# print(df_q1, df_q1.columns)

# Extract the four columns for technologies
first_columns1 = df_q1.iloc[:, :5]
second_columns1 = df_q1.iloc[:, 5:10]
third_columns1 = df_q1.iloc[:, 10:15]
four_columns1 = df_q1.iloc[:, 15:]
first_columns2 = df_q2.iloc[:, :5]
second_columns2 = df_q2.iloc[:, 5:10]
third_columns2 = df_q2.iloc[:, 10:15]
four_columns2 = df_q2.iloc[:, 15:]
first_columns3 = df_q3.iloc[:, :5]
second_columns3 = df_q3.iloc[:, 5:10]
third_columns3 = df_q3.iloc[:, 10:15]
four_columns3 = df_q3.iloc[:, 15:]

col_names = {0: 'SCG', 1: 'Google', 2: 'ChatGPT-3.5', 3: 'ThinkAny'}
# Calculate mean for each row
row_means1 = first_columns1.mean(axis=1)
row_means2 = second_columns1.mean(axis=1)
row_means3 = third_columns1.mean(axis=1)
row_means4 = four_columns1.mean(axis=1)
df_ct_1 = pd.concat([row_means1, row_means2, row_means3, row_means4], axis=1)
df_ct_1 = df_ct_1.rename(columns=col_names)
row_means1 = first_columns2.mean(axis=1)
row_means2 = second_columns2.mean(axis=1)
row_means3 = third_columns2.mean(axis=1)
row_means4 = four_columns2.mean(axis=1)
df_ct_2 = pd.concat([row_means1, row_means2, row_means3, row_means4], axis=1)
df_ct_2 = df_ct_2.rename(columns=col_names)
row_means1 = first_columns3.mean(axis=1)
row_means2 = second_columns3.mean(axis=1)
row_means3 = third_columns3.mean(axis=1)
row_means4 = four_columns3.mean(axis=1)
df_ct_3 = pd.concat([row_means1, row_means2, row_means3, row_means4], axis=1)
df_ct_3 = df_ct_3.rename(columns=col_names)
# print(df_ct_1)
# print(df_ct_2)
# print(df_ct_3)



# # Define overall significance level
# alpha = 0.05
# # Number of questions
# num_comparisons = 3
# # Calculate corrected significance level
# alpha_corrected = alpha / num_comparisons
# print('New alpha value:', alpha_corrected)
#
#
# # Friedman test
# friedman_statistic, friedman_pvalue = stats.friedmanchisquare(df_ct_3['SCG'], df_ct_3['Google'], df_ct_3['ChatGPT-3.5'], df_ct_3['ThinkAny'])
# print("Friedman Test")
# print("Friedman statistic:", friedman_statistic)
# print("p-value:", friedman_pvalue)
#
# # Wilcoxon Signed-Rank Test:
# w_statistic_g1, w_p_value_g1 = wilcoxon(df_ct_3['SCG'], df_ct_3['Google'])
# w_statistic_gpt1, w_p_value_gpt1 = wilcoxon(df_ct_3['SCG'], df_ct_3['ChatGPT-3.5'])
# w_statistic_ta1, w_p_value_ta1 = wilcoxon(df_ct_3['SCG'], df_ct_3['ThinkAny'])
# print("Wilcoxon Signed-Rank Test - Gold Standard vs Google:")
# print("Statistic:", w_statistic_g1)
# print("p-value:", w_p_value_g1)
# print("Wilcoxon Signed-Rank Test - Gold Standard vs ChatGPT:")
# print("Statistic:", w_statistic_gpt1)
# print("p-value:", w_p_value_gpt1)
# print("Wilcoxon Signed-Rank Test - Gold Standard vs ThinkAny:")
# print("Statistic:", w_statistic_ta1)
# print("p-value:", w_p_value_ta1)
#
#
# # Mann-Whitney U Test
# m_statistic_g1, m_p_value_g1 = mannwhitneyu(df_ct_3['SCG'].astype(int), df_ct_3['Google'].astype(int))
# m_statistic_gpt1, m_p_value_gpt1 = mannwhitneyu(df_ct_3['SCG'].astype(int), df_ct_3['ChatGPT-3.5'].astype(int))
# m_statistic_ta1, m_p_value_ta1 = mannwhitneyu(df_ct_3['SCG'].astype(int), df_ct_3['ThinkAny'].astype(int))
# print("Mann-Whitney U Test - Gold Standard vs Google:")
# print("Statistic:", m_statistic_g1)
# print("p-value:", m_p_value_g1)
# print("Mann-Whitney U Test - Gold Standard vs ChatGPT:")
# print("Statistic:", m_statistic_gpt1)
# print("p-value:", m_p_value_gpt1)
# print("Mann-Whitney U Test - Gold Standard vs ThinkAny:")
# print("Statistic:", m_statistic_ta1)
# print("p-value:", m_p_value_ta1)


# # Plotting the data
data_vis(df_ct_1, df_ct_2, df_ct_3)
box_plot(df_ct_1, df_ct_2, df_ct_3)
opt_data = output_data()
p_plots(opt_data)


