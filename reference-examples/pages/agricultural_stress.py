"""
Agricultural Stress Dashboard – Morocco
========================================

This page explores agricultural stress indicators in Morocco, including
cereal yield, rainfall patterns, and food price fluctuations.

Students can analyze how climate variations (rainfall) impact agricultural
productivity (cereal yield) and how these factors relate to food security
through price indices. This dashboard demonstrates the interconnection between
climate, agriculture, and economic crises.

Key Insights:
- Low rainfall years (e.g., 2022) correlate with reduced cereal yields
- Food price indices tend to rise when agricultural stress increases
- Understanding these relationships is crucial for economic resilience
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# Define the path to the data file
DATA_PATH = Path(__file__).parents[1] / "data" / "morocco" / "agri_stress.csv"


def load_data() -> pd.DataFrame:
    """
    Load agricultural stress data from CSV file.

    Returns:
        pd.DataFrame: DataFrame containing year, cereal_yield, rainfall_index,
                     and food_price_index columns
    """
    df = pd.read_csv(DATA_PATH)
    return df


def run():
    """
    Main function to run the Agricultural Stress dashboard.

    This function:
    1. Displays the page title and description in bilingual format
    2. Loads the agricultural stress data from CSV
    3. Shows a preview of the data
    4. Displays visualizations for:
       - Cereal yield trends over time
       - Rainfall and food price indices
    5. Provides educational context about agricultural stress
    """

    # Page title in both Arabic and English
    st.title("🌾 Agricultural Stress in Morocco | الإجهاد الزراعي في المغرب")

    # Introduction section with bilingual description
    st.markdown(
        """
        ### About This Dashboard | حول لوحة التحكم هذه

        **English:**
        This dashboard analyzes agricultural stress indicators in Morocco using
        **approximate real data** on cereal productivity and climate indicators.

        We explore:
        - **Cereal yield (kg/ha)**: A measure of agricultural productivity
        - **Rainfall index**: Normalized rainfall patterns (0–1 scale)
        - **Food price index**: Normalized food prices (0–1 scale)

        Agricultural stress often stems from climate variability, and can lead to
        broader economic and social crises including food insecurity and rural unemployment.

        ---

        **العربية:**
        تحلل لوحة التحكم هذه مؤشرات الإجهاد الزراعي في المغرب باستخدام بيانات حقيقية تقريبية
        حول إنتاج الحبوب ومؤشرات المناخ.

        نستكشف:
        - **غلة الحبوب (كغ/هكتار)**: مقياس إنتاجية زراعية
        - **مؤشر هطول الأمطار**: أنماط الأمطار المعيارية (مقياس 0–1)
        - **مؤشر الأسعار الغذائية**: الأسعار الغذائية المعيارية (مقياس 0–1)

        غالباً ما ينشأ الإجهاد الزراعي من التغيرات المناخية ويمكن أن يؤدي إلى أزمات
        اقتصادية واجتماعية أوسع تشمل انعدام الأمن الغذائي والبطالة الريفية.
        """
    )

    # Load the agricultural stress data
    df = load_data()

    # Display data preview
    st.subheader("📊 Data Preview | معاينة البيانات")
    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "year": "Year",
            "cereal_yield_kg_per_ha": "Cereal Yield (kg/ha)",
            "rainfall_index": "Rainfall Index (0–1)",
            "food_price_index": "Food Price Index (0–1)",
        }
    )

    st.markdown("---")

    # Visualization 1: Cereal Yield Over Time
    st.subheader("📈 Cereal Yield Trends | تطور غلة الحبوب عبر السنوات")
    st.markdown(
        """
        **What does this tell us?**

        The cereal yield graph shows the productivity of grain farming over time.
        Lower yields indicate agricultural stress, which may be caused by:
        - Drought and insufficient rainfall
        - Poor soil conditions
        - Climate variability
        - Pest outbreaks

        Notice the drop in 2022 when rainfall was extremely low (0.3 index).
        """
    )

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(
        df["year"],
        df["cereal_yield_kg_per_ha"],
        marker="o",
        linewidth=2,
        markersize=8,
        color="#2E7D32",
        label="Cereal Yield"
    )
    ax1.fill_between(
        df["year"],
        df["cereal_yield_kg_per_ha"],
        alpha=0.3,
        color="#2E7D32"
    )
    ax1.set_xlabel("Year | السنة", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Cereal Yield (kg/ha) | غلة الحبوب (كغ/هكتار)", fontsize=12, fontweight="bold")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)
    plt.tight_layout()
    st.pyplot(fig1)

    st.markdown("---")

    # Visualization 2: Rainfall and Food Prices
    st.subheader("🌧️ Rainfall Index & Food Prices | مؤشر الأمطار والأسعار الغذائية")
    st.markdown(
        """
        **What's the connection?**

        This chart shows two important relationships:

        1. **Rainfall Index** (blue line): Represents water availability for crops.
           Lower rainfall = More agricultural stress

        2. **Food Price Index** (orange line): Shows food affordability. Higher prices
           indicate economic stress for consumers, especially in rural areas.

        **Notice:** When rainfall drops, food prices often rise, indicating that reduced
        agricultural output leads to food scarcity and higher prices. This creates a
        **double crisis**: farmers earn less while consumers pay more.
        """
    )

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    # Plot rainfall index
    ax2.plot(
        df["year"],
        df["rainfall_index"],
        marker="o",
        linewidth=2.5,
        markersize=8,
        color="#1976D2",
        label="Rainfall Index (0–1)"
    )
    ax2.fill_between(
        df["year"],
        df["rainfall_index"],
        alpha=0.2,
        color="#1976D2"
    )

    # Plot food price index on the same axes
    ax2.plot(
        df["year"],
        df["food_price_index"],
        marker="s",
        linewidth=2.5,
        markersize=8,
        color="#F57C00",
        label="Food Price Index (0–1)"
    )
    ax2.fill_between(
        df["year"],
        df["food_price_index"],
        alpha=0.2,
        color="#F57C00"
    )

    ax2.set_xlabel("Year | السنة", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Index Value (0–1) | قيمة المؤشر (0–1)", fontsize=12, fontweight="bold")
    ax2.set_ylim(0, 1)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10, loc="best")
    plt.tight_layout()
    st.pyplot(fig2)

    st.markdown("---")

    # Summary Statistics
    st.subheader("📋 Summary Statistics | الإحصائيات الملخصة")

    col1, col2, col3 = st.columns(3)

    with col1:
        avg_yield = df["cereal_yield_kg_per_ha"].mean()
        st.metric(
            "Average Cereal Yield",
            f"{avg_yield:.0f} kg/ha",
            help="Average productivity across all years"
        )

    with col2:
        avg_rainfall = df["rainfall_index"].mean()
        st.metric(
            "Average Rainfall Index",
            f"{avg_rainfall:.2f}",
            help="Average water availability (0–1 scale)"
        )

    with col3:
        avg_price = df["food_price_index"].mean()
        st.metric(
            "Average Food Price Index",
            f"{avg_price:.2f}",
            help="Average food prices (0–1 scale)"
        )

    st.markdown("---")

    # Educational context and implications
    st.subheader("🎓 Key Takeaways | النقاط الرئيسية")
    st.info(
        """
        **Why This Matters for Economic & Social Crises:**

        1. **Climate Vulnerability**: Morocco's agriculture is highly dependent on rainfall,
           making it vulnerable to droughts and climate change.

        2. **Food Security**: Agricultural stress directly impacts food availability and prices,
           affecting millions of households, especially in rural areas.

        3. **Rural Livelihoods**: When cereal yields fall, farmers' incomes decline, leading to
           rural unemployment and migration to cities, fueling urban unemployment.

        4. **Inflation & Cost of Living**: Higher food prices contribute to inflation, reducing
           purchasing power and increasing poverty rates.

        5. **Policy Implications**: Governments must invest in climate adaptation, irrigation,
           crop diversification, and social safety nets to protect farmers and consumers.

        **Connection to Other Dashboards:**
        - See "Youth Unemployment" for rural-urban migration trends
        - See "Macro Indicators" for inflation impacts
        - See "Household Budgets" for food spending as % of income
        """
    )

    # Data source and educational note
    st.markdown("---")
    st.caption(
        "📝 Data note: This dashboard uses approximate real-world data for educational purposes. "
        "For policy decisions, consult official FAO (Food and Agriculture Organization) statistics. "
        "| ملاحظة البيانات: تستخدم لوحة التحكم هذه بيانات حقيقية تقريبية لأغراض تعليمية."
    )
