import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def data_vis(df_q1, df_q2, df_q3):
    q1_avg = list(df_q1.mean(axis=0))
    q2_avg = list(df_q2.mean(axis=0))
    q3_avg = list(df_q3.mean(axis=0))
    print('Averages:', len(q1_avg), len(q2_avg), len(q3_avg))
    data = {
        'Technology': ['SCG', 'Google', 'ChatGPT-3.5', 'ThinkAny'],
        'Q1': q1_avg,
        'Q2': q2_avg,
        'Q3': q3_avg,
    }
    df_plot = pd.DataFrame(data)
    print(df_plot)

    # Melt the DataFrame
    df_melted = df_plot.melt(id_vars='Technology', var_name='Question', value_name='Score')
    # Calculate average scores for each question
    avg_scores = df_melted.groupby('Question')['Score'].mean().reset_index()

    # Plot
    plt.figure(figsize=(12, 6))

    markers = ['o', 's', '^', 'D']  # Different markers for each technology
    for i, tech in enumerate(df_plot['Technology']):
        tech_data = df_melted[df_melted['Technology'] == tech]
        sns.lineplot(data=tech_data, x='Question', y='Score', marker=markers[i], markersize=10, label=tech)
        sns.scatterplot(data=tech_data, x='Question', y='Score', marker=markers[i], s=200, legend=False)

    # sns.barplot(data=avg_scores, x='Question', y='Score', color='gray', alpha=0.5, ci=None)
    plt.ylim(1, 5)  # Set y-axis limits
    plt.xlabel('Clinical Guideline Question')
    plt.ylabel('Likert Scale Rating')
    # plt.title('Scores for each Question by Technology')
    plt.legend()
    plt.show()


def box_plot(df_q1, df_q2, df_q3):
    frames = [df_q1, df_q2, df_q3]
    data = pd.concat(frames)
    # print(data)

    # Convert data to DataFrame
    df = pd.DataFrame(data)
    print(df.columns)
    # Melt the DataFrame
    df_melted = df.melt(value_name='Rating', var_name='Technology')

    # Draw boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_melted, x='Technology', y='Rating', palette='Set3')
    plt.xlabel('Technology')
    plt.ylabel('Likert Scale Rating')
    # plt.title('Boxplot of Ratings for Each Technology')
    plt.ylim(0, 6)  # Set y-axis limits
    # plt.legend(df.columns, loc='upper right')
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

def p_plots(data):
    # Extracting data for plotting
    methods = ['Google', 'ChatGPT-3.5', 'ThinkAny']
    questions = ['Q1', 'Q2', 'Q3']
    response_data = {}

    wsr_data = []
    mwu_data = []

    for question in questions:
        wsr_stats = []
        mwu_stats = []
        for method in methods:
            wsr_stat = data[question]['WSR'][f'WSR-Sv{method[0]}']['statistic']
            mwu_stat = data[question]['MWU'][f'MWU-Sv{method[0]}']['statistic']
            wsr_stats.append(wsr_stat)
            mwu_stats.append(mwu_stat)
        wsr_data.append(wsr_stats)
        mwu_data.append(mwu_stats)

    # Plotting violin plots
    plt.figure(figsize=(10, 6))
    violin = sns.violinplot(data=wsr_data)
    plt.xticks(range(len(questions)), questions)
    plt.xlabel('Questions')
    plt.ylabel('p-value')
    # plt.title('Comparison of Wilcoxon Signed-Rank Test Statistics Across Questions and Methods')
    legend_labels = ['Google', 'ChatGPT-3.5', 'ThinkAny']
    legend_handles = [violin.collections[i] for i in range(len(methods))]
    plt.legend(legend_handles, legend_labels)
    plt.show()

    plt.figure(figsize=(10, 6))
    violin = sns.violinplot(data=mwu_data)
    plt.xticks(range(len(questions)), questions)
    plt.xlabel('Questions')
    plt.ylabel('p-value')
    # plt.title('Comparison of Mann-Whitney U Test Statistics Across Questions and Methods')
    legend_handles = [violin.collections[i] for i in range(len(methods))]
    plt.legend(legend_handles, legend_labels)
    plt.show()



# Barplot
# Violinplot
