"""
Checkpoint Monitor Dashboard Module

This module analyzes checkpoint wait times in Jerusalem using the checkpoint
wait times dataset. It provides visualizations and statistical analysis of how
waiting times vary by day of week and time of day.

Educational Context:
- Checkpoint systems significantly impact mobility and quality of life
- Wait times vary by day of week due to different traffic patterns
- Time-of-day analysis reveals peak congestion periods
- This data supports understanding of movement restrictions' economic impacts

Data Source: Jerusalem checkpoint wait times dataset
Bilingual Support: Arabic (العربية) and English
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def run():
    """
    Main execution function for the checkpoint monitor dashboard.

    This function:
    1. Loads checkpoint wait time data from CSV
    2. Displays data preview and basic statistics
    3. Creates visualizations of wait times by day and hour
    4. Provides analysis insights for economic/social impact assessment
    """

    # Page header with bilingual support
    st.header("مؤشر زمن الحواجز في القدس – Jerusalem Checkpoint Monitor")

    # Educational context
    st.write(
        "**Context / السياق:** This dashboard analyzes waiting times at checkpoints "
        "in Jerusalem, which are a critical factor in understanding movement restrictions "
        "and their economic and social impacts. "
        "- هذه لوحة معلومات تحلل أوقات الانتظار في الحواجز في القدس"
    )

    # Load data from the new path
    try:
        df = pd.read_csv("data/jerusalem/checkpoint_wait_times.csv")
    except FileNotFoundError:
        st.error(
            "Data file not found. Please ensure checkpoint_wait_times.csv is in "
            "data/jerusalem/ directory."
        )
        return

    # Display data preview
    st.subheader("معاينة البيانات / Data Preview")
    st.write(
        f"Dataset contains {len(df)} checkpoint crossing records with the following columns:"
    )
    st.dataframe(df.head(10))

    # Display basic statistics
    st.subheader("إحصائيات أساسية / Basic Statistics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Wait Time (min)",
            f"{df['wait_minutes'].mean():.1f}"
        )

    with col2:
        st.metric(
            "Maximum Wait Time (min)",
            f"{df['wait_minutes'].max():.0f}"
        )

    with col3:
        st.metric(
            "Minimum Wait Time (min)",
            f"{df['wait_minutes'].min():.0f}"
        )

    with col4:
        st.metric(
            "Std Deviation (min)",
            f"{df['wait_minutes'].std():.1f}"
        )

    # Analysis by day of week
    st.subheader("متوسط زمن الانتظار لكل يوم / Average Waiting Time by Day of Week")
    st.write(
        "This chart shows how average checkpoint wait times vary across different days. "
        "Peak congestion days require additional planning and resources."
    )

    # Calculate average wait time by day
    avg_by_day = df.groupby("day_of_week")["wait_minutes"].mean().reset_index()
    avg_by_day = avg_by_day.sort_values("wait_minutes", ascending=False)

    # Create bar chart for day of week
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        range(len(avg_by_day)),
        avg_by_day["wait_minutes"],
        color=['#d62728' if x > df['wait_minutes'].mean() else '#2ca02c'
               for x in avg_by_day["wait_minutes"]]
    )

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2.,
            height,
            f'{height:.1f}',
            ha='center',
            va='bottom',
            fontsize=10
        )

    ax.set_xlabel("اليوم / Day of Week", fontsize=12, fontweight='bold')
    ax.set_ylabel("متوسط زمن الانتظار (دقيقة) / Avg Wait Time (minutes)",
                  fontsize=12, fontweight='bold')
    ax.set_xticks(range(len(avg_by_day)))
    ax.set_xticklabels(avg_by_day["day_of_week"], rotation=45, ha='right')
    ax.axhline(y=df['wait_minutes'].mean(), color='blue', linestyle='--',
               label=f'Average: {df["wait_minutes"].mean():.1f} min', linewidth=2)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)

    # Analysis by hour of day
    st.subheader("متوسط زمن الانتظار حسب الساعة / Average Waiting Time by Hour of Day")
    st.write(
        "Morning and evening hours typically show higher congestion as people commute. "
        "Understanding these patterns is essential for policy planning and resource allocation."
    )

    # Calculate average wait time by hour
    avg_by_hour = df.groupby("hour")["wait_minutes"].mean().reset_index()
    avg_by_hour = avg_by_hour.sort_values("hour")

    # Create line chart for hour of day
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(
        avg_by_hour["hour"],
        avg_by_hour["wait_minutes"],
        marker='o',
        linewidth=2,
        markersize=8,
        color='#1f77b4'
    )
    ax.fill_between(
        avg_by_hour["hour"],
        avg_by_hour["wait_minutes"],
        alpha=0.3,
        color='#1f77b4'
    )

    ax.set_xlabel("الساعة / Hour of Day", fontsize=12, fontweight='bold')
    ax.set_ylabel("متوسط زمن الانتظار (دقيقة) / Avg Wait Time (minutes)",
                  fontsize=12, fontweight='bold')
    ax.set_xticks(range(6, 22, 2))
    ax.grid(True, alpha=0.3)
    ax.axhline(y=df['wait_minutes'].mean(), color='red', linestyle='--',
               label=f'Average: {df["wait_minutes"].mean():.1f} min', linewidth=2)
    ax.legend()

    plt.tight_layout()
    st.pyplot(fig)

    # Heatmap: Wait times by day and hour
    st.subheader("الخريطة الحرارية: أوقات الانتظار / Heatmap: Wait Times by Day and Hour")
    st.write(
        "This heatmap reveals patterns across the week. Darker red indicates longer wait times, "
        "showing peak congestion periods."
    )

    # Create pivot table for heatmap
    pivot_table = df.pivot_table(
        values='wait_minutes',
        index='day_of_week',
        columns='hour',
        aggfunc='mean'
    )

    # Create heatmap
    fig, ax = plt.subplots(figsize=(14, 6))
    im = ax.imshow(pivot_table.values, cmap='RdYlGn_r', aspect='auto')

    # Set ticks and labels
    ax.set_xticks(range(len(pivot_table.columns)))
    ax.set_yticks(range(len(pivot_table.index)))
    ax.set_xticklabels(pivot_table.columns)
    ax.set_yticklabels(pivot_table.index)

    ax.set_xlabel("الساعة / Hour", fontsize=12, fontweight='bold')
    ax.set_ylabel("اليوم / Day of Week", fontsize=12, fontweight='bold')

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("متوسط زمن الانتظار (دقيقة) / Avg Wait Time (min)",
                   rotation=270, labelpad=20)

    plt.tight_layout()
    st.pyplot(fig)

    # Statistical insights
    st.subheader("الرؤى الإحصائية / Statistical Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Highest Average Wait Times (Top 3):**")
        top_days = avg_by_day.nlargest(3, "wait_minutes")
        for idx, row in top_days.iterrows():
            st.write(f"- {row['day_of_week']}: {row['wait_minutes']:.1f} minutes")

    with col2:
        st.write("**Lowest Average Wait Times (Bottom 3):**")
        bottom_days = avg_by_day.nsmallest(3, "wait_minutes")
        for idx, row in bottom_days.iterrows():
            st.write(f"- {row['day_of_week']}: {row['wait_minutes']:.1f} minutes")

    st.write("**Peak Hours:**")
    peak_hour = avg_by_hour.loc[avg_by_hour['wait_minutes'].idxmax()]
    off_peak_hour = avg_by_hour.loc[avg_by_hour['wait_minutes'].idxmin()]

    st.write(
        f"- Peak congestion: **{peak_hour['hour']:.0f}:00** with "
        f"{peak_hour['wait_minutes']:.1f} minutes average wait\n"
        f"- Off-peak: **{off_peak_hour['hour']:.0f}:00** with "
        f"{off_peak_hour['wait_minutes']:.1f} minutes average wait"
    )

    # Educational conclusion
    st.subheader("التأثير التعليمي / Educational Impact")
    st.info(
        "Checkpoint wait times are a crucial indicator of mobility restrictions and their "
        "socioeconomic impacts. This analysis demonstrates:\n\n"
        "1. **Temporal Patterns**: Wait times vary significantly by day and hour\n"
        "2. **Resource Requirements**: Peak periods require more capacity\n"
        "3. **Commuting Costs**: Longer waits increase transportation time and economic burden\n"
        "4. **Policy Implications**: Understanding these patterns is essential for policy "
        "recommendations addressing movement and access restrictions"
    )


if __name__ == "__main__":
    run()
