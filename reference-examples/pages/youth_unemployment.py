"""
Youth Unemployment in Morocco - Data Analysis Dashboard
========================================================

This module provides an analysis of youth unemployment trends in Morocco
across urban and rural regions, with bilingual support (Arabic/English).

Students can use this module to:
- Explore temporal trends in youth unemployment rates
- Compare differences between urban and rural areas
- Identify critical periods and policy implications
- Link data to other socioeconomic indicators
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def run():
    """
    Main function to run the youth unemployment analysis dashboard.

    This function:
    1. Loads youth unemployment data for Morocco
    2. Displays bilingual content (Arabic/English)
    3. Presents visualizations of unemployment trends
    4. Provides educational context and analysis prompts
    """

    # ==================== Header and Introduction ====================
    st.header("بطالة الشباب – المغرب (بيانات حقيقية/واقعية)")
    st.header("Youth Unemployment - Morocco (Real Data)")

    st.write(
        "هذه البيانات مبنية على مؤشرات حقيقية تقريبية لبطالة الشباب (% من قوة العمل 15–24 سنة)، "
        "مع توسيع بسيط لأغراض تعليمية."
    )
    st.write(
        "This data is based on approximated real indicators of youth unemployment "
        "(% of labor force ages 15-24), with slight adjustments for educational purposes."
    )

    # ==================== Data Loading ====================
    try:
        df = pd.read_csv("data/morocco/youth_unemployment.csv")
    except FileNotFoundError:
        st.error("Error: Could not find youth_unemployment.csv file. Please check the data path.")
        return

    # ==================== Data Preview ====================
    st.subheader("معاينة البيانات / Data Preview")
    st.dataframe(df)

    # Display basic statistics
    st.subheader("إحصائيات أساسية / Basic Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "متوسط بطالة الشباب الوطنية / National Avg",
            f"{df['national_youth_unemployment_rate'].mean():.2f}%"
        )

    with col2:
        st.metric(
            "متوسط بطالة الشباب الحضرية / Urban Avg",
            f"{df['urban_youth_unemployment_rate'].mean():.2f}%"
        )

    with col3:
        st.metric(
            "متوسط بطالة الشباب الريفية / Rural Avg",
            f"{df['rural_youth_unemployment_rate'].mean():.2f}%"
        )

    # ==================== Visualizations ====================

    # Chart 1: Youth unemployment over time (all regions)
    st.subheader("تطور بطالة الشباب عبر الزمن / Youth Unemployment Over Time")

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(
        df["year"],
        df["national_youth_unemployment_rate"],
        marker="o",
        label="National / وطني",
        linewidth=2.5,
        markersize=8
    )
    ax.plot(
        df["year"],
        df["urban_youth_unemployment_rate"],
        marker="s",
        label="Urban / حضر",
        linewidth=2.5,
        markersize=8
    )
    ax.plot(
        df["year"],
        df["rural_youth_unemployment_rate"],
        marker="^",
        label="Rural / ريف",
        linewidth=2.5,
        markersize=8
    )

    ax.set_xlabel("السنة / Year", fontsize=12)
    ax.set_ylabel("نسبة بطالة الشباب (%) / Youth Unemployment Rate (%)", fontsize=12)
    ax.set_title("تطور بطالة الشباب في المغرب (2015-2024) / Morocco Youth Unemployment Trends (2015-2024)",
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='best')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)

    # Chart 2: Urban vs Rural comparison
    st.subheader("المقارنة بين المناطق الحضرية والريفية / Urban vs Rural Comparison")

    fig, ax = plt.subplots(figsize=(12, 6))

    x = df["year"].values
    width = 0.35

    ax.bar(x - width/2, df["urban_youth_unemployment_rate"], width,
           label="Urban / حضر", alpha=0.8, color='steelblue')
    ax.bar(x + width/2, df["rural_youth_unemployment_rate"], width,
           label="Rural / ريف", alpha=0.8, color='coral')

    ax.set_xlabel("السنة / Year", fontsize=12)
    ax.set_ylabel("نسبة بطالة الشباب (%) / Youth Unemployment Rate (%)", fontsize=12)
    ax.set_title("المناطق الحضرية مقابل الريفية / Urban vs Rural Unemployment Rates",
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    st.pyplot(fig)

    # ==================== Key Insights ====================
    st.subheader("الاستنتاجات الرئيسية / Key Insights")

    # Calculate some key metrics
    peak_year = df.loc[df['national_youth_unemployment_rate'].idxmax()]
    peak_unemployment = peak_year['national_youth_unemployment_rate']
    peak_year_val = int(peak_year['year'])

    urban_rural_diff = (df['urban_youth_unemployment_rate'].mean() -
                       df['rural_youth_unemployment_rate'].mean())

    recent_trend = df.iloc[-1]['national_youth_unemployment_rate'] - df.iloc[-3]['national_youth_unemployment_rate']

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:
        st.info(
            f"**ذروة البطالة / Peak Unemployment:**\n\n"
            f"حدثت أعلى نسبة بطالة شباب وطنية في سنة {peak_year_val} "
            f"({peak_unemployment:.1f}%). / "
            f"The highest national youth unemployment rate occurred in {peak_year_val} ({peak_unemployment:.1f}%)."
        )

    with insight_col2:
        st.info(
            f"**الفجوة بين الحضر والريف / Urban-Rural Gap:**\n\n"
            f"متوسط الفرق هو {urban_rural_diff:.1f}% نقطة مئوية. "
            f"البطالة في المناطق الحضرية أعلى بكثير. / "
            f"The urban-rural gap averages {urban_rural_diff:.1f} percentage points. "
            f"Urban unemployment is significantly higher."
        )

    # ==================== Educational Context ====================
    st.subheader("سياق تعليمي / Educational Context")

    st.write(
        "**الأسئلة المقترحة للتحليل / Suggested Questions for Analysis:**"
    )

    st.markdown(
        """
        1. **تحليل المناطق الحضرية والريفية / Urban-Rural Analysis:**
           - لماذا تكون نسبة البطالة في المناطق الحضرية أعلى بكثير؟
           - هل يرتبط ذلك بتكلفة المعيشة أم بفرص العمل المتاحة؟
           - Why is urban youth unemployment significantly higher?
           - Is it related to cost of living or available job opportunities?

        2. **الاتجاهات الزمنية / Temporal Trends:**
           - ما السبب في ارتفاع البطالة بين 2015 و2020؟
           - هل تأثرت بالأزمات الاقتصادية أو جائحة COVID-19؟
           - What caused the increase in unemployment from 2015 to 2020?
           - Was it affected by economic crises or the COVID-19 pandemic?

        3. **الربط بمؤشرات أخرى / Linking to Other Indicators:**
           - يمكن ربط هذه البيانات بمؤشرات التعليم أو أسعار الغذاء
           - How do education levels correlate with unemployment rates?
           - Can we link this to other socioeconomic crises?

        4. **السياسات والحلول / Policies and Solutions:**
           - ما السياسات الممكنة لتقليل بطالة الشباب؟
           - كيف يمكن تطوير الفرص الاقتصادية في المناطق الريفية؟
           - What policies could reduce youth unemployment?
           - How can economic opportunities be developed in rural areas?
        """
    )

    # ==================== Data Export ====================
    st.subheader("تحميل البيانات / Download Data")

    csv = df.to_csv(index=False)
    st.download_button(
        label="تحميل CSV / Download CSV",
        data=csv,
        file_name="youth_unemployment_morocco.csv",
        mime="text/csv"
    )


if __name__ == "__main__":
    run()
