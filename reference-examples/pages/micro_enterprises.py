"""
Micro Enterprises Resilience Dashboard - Jerusalem
====================================================

This module analyzes the resilience of micro-enterprises in Jerusalem neighborhoods,
examining how factors like income, rent, taxes, and digital access affect business risk.

The data is synthetic and designed for educational purposes. Students can modify
the risk_score calculation, add new variables, or substitute with real data.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def run():
    """
    Main function to display the micro-enterprises resilience dashboard.

    Features:
    - Data preview with key economic indicators
    - Risk score distribution analysis
    - Income comparison across risk categories
    - Sector-based risk and income analysis
    - Educational notes on data enhancement
    """

    # Page title with bilingual support
    st.header("مرونة المشاريع المتناهية الصغر – القدس / Micro-Enterprises Resilience - Jerusalem")

    # Educational context
    st.write(
        "**Educational Dataset**: This data is synthetic and created for training purposes. "
        "Groups can replace it with real data from economic reports or field surveys about "
        "local shops and micro-businesses."
    )
    st.write(
        "**البيانات التعليمية**: هذه البيانات مصطنعة لأغراض التدريب. يمكن للمجموعات استبدالها "
        "ببيانات حقيقية حول المحلات أو المشاريع من تقارير اقتصادية أو مسوح ميدانية."
    )

    # Load the data from the correct path
    df = pd.read_csv("data/jerusalem/micro_enterprises.csv")

    # ============================================================================
    # DATA PREVIEW SECTION
    # ============================================================================
    st.subheader("معاينة البيانات / Data Preview")
    st.write(
        "**Column descriptions**:\n"
        "- **shop_id**: Unique identifier for each micro-enterprise\n"
        "- **neighborhood**: Jerusalem neighborhood location\n"
        "- **sector**: Type of business (groceries, restaurants, traditional crafts, tourism, services)\n"
        "- **risk_category**: Low, Medium, or High risk classification\n"
        "- **monthly_income_usd**: Average monthly revenue in USD\n"
        "- **monthly_rent_usd**: Monthly rent/overhead costs in USD\n"
        "- **tax_burden_index**: Tax pressure (0-100 scale)\n"
        "- **digital_access_score**: Digital infrastructure access (0-100 scale)\n"
        "- **risk_score**: Overall vulnerability score (0-100 scale)"
    )
    st.dataframe(df.head(10))

    # Display basic statistics
    st.write("**Dataset Statistics:**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Shops", len(df))
    with col2:
        st.metric("Avg Monthly Income", f"${df['monthly_income_usd'].mean():.0f}")
    with col3:
        st.metric("Avg Monthly Rent", f"${df['monthly_rent_usd'].mean():.0f}")
    with col4:
        st.metric("Avg Risk Score", f"{df['risk_score'].mean():.1f}")

    # ============================================================================
    # RISK SCORE ANALYSIS SECTION
    # ============================================================================
    st.subheader("توزيع درجة المخاطر / Risk Score Distribution")
    st.write(
        "This histogram shows how many shops fall into each risk score range. "
        "Higher scores indicate greater vulnerability to economic shocks. "
        "Notice the patterns: are most shops concentrated in high-risk or low-risk zones?"
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df["risk_score"], bins=10, color='steelblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel("درجة المخاطر / Risk Score", fontsize=12)
    ax.set_ylabel("عدد المشاريع / Number of Shops", fontsize=12)
    ax.set_title("Distribution of Business Vulnerability", fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    st.pyplot(fig)

    # ============================================================================
    # INCOME BY RISK CATEGORY SECTION
    # ============================================================================
    st.subheader("متوسط الدخل الشهري حسب فئة الخطر / Average Monthly Income by Risk Category")
    st.write(
        "How does income differ based on risk level? Do lower-income shops tend to have "
        "higher risk scores? This analysis helps identify which businesses need support."
    )

    # Calculate average income by risk category
    avg_income = df.groupby("risk_category")["monthly_income_usd"].mean().reset_index()

    # Order categories logically
    category_order = ["منخفض", "متوسط", "مرتفع"]  # Low, Medium, High in Arabic
    avg_income['risk_category'] = pd.Categorical(
        avg_income['risk_category'],
        categories=category_order,
        ordered=True
    )
    avg_income = avg_income.sort_values('risk_category')

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    bars = ax2.bar(
        [f"{cat}\n(Low/Med/High)" for cat in avg_income["risk_category"]],
        avg_income["monthly_income_usd"],
        color=['green', 'orange', 'red'],
        alpha=0.7,
        edgecolor='black'
    )
    ax2.set_ylabel("متوسط الدخل (دولار) / Average Monthly Income (USD)", fontsize=12)
    ax2.set_title("Income by Risk Category", fontsize=14, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.0f}',
                ha='center', va='bottom', fontweight='bold')

    st.pyplot(fig2)

    # ============================================================================
    # SECTOR ANALYSIS SECTION
    # ============================================================================
    st.subheader("تحليل القطاع / Sector Analysis")
    st.write(
        "Different business sectors face different challenges. Let's examine how "
        "risk and income vary by type of business (groceries, restaurants, tourism, etc.)."
    )

    col1, col2 = st.columns(2)

    # Sector-based risk analysis
    with col1:
        st.write("**Average Risk Score by Sector**")
        sector_risk = df.groupby("sector")["risk_score"].mean().sort_values(ascending=False)

        fig3, ax3 = plt.subplots(figsize=(10, 5))
        bars = ax3.barh(sector_risk.index, sector_risk.values, color='coral', alpha=0.7, edgecolor='black')
        ax3.set_xlabel("درجة المخاطر / Risk Score", fontsize=11)
        ax3.set_title("Risk by Business Sector", fontsize=12, fontweight='bold')
        ax3.grid(axis='x', alpha=0.3)

        # Add value labels
        for bar in bars:
            width = bar.get_width()
            ax3.text(width, bar.get_y() + bar.get_height()/2.,
                    f'{width:.1f}',
                    ha='left', va='center', fontweight='bold', fontsize=9)

        st.pyplot(fig3)

    # Sector-based income analysis
    with col2:
        st.write("**Average Income by Sector**")
        sector_income = df.groupby("sector")["monthly_income_usd"].mean().sort_values(ascending=False)

        fig4, ax4 = plt.subplots(figsize=(10, 5))
        bars = ax4.barh(sector_income.index, sector_income.values, color='skyblue', alpha=0.7, edgecolor='black')
        ax4.set_xlabel("متوسط الدخل (دولار) / Average Income (USD)", fontsize=11)
        ax4.set_title("Income by Business Sector", fontsize=12, fontweight='bold')
        ax4.grid(axis='x', alpha=0.3)

        # Add value labels
        for bar in bars:
            width = bar.get_width()
            ax4.text(width, bar.get_y() + bar.get_height()/2.,
                    f'${width:.0f}',
                    ha='left', va='center', fontweight='bold', fontsize=9)

        st.pyplot(fig4)

    # ============================================================================
    # INCOME VS RENT RELATIONSHIP SECTION
    # ============================================================================
    st.subheader("العلاقة بين الدخل والإيجار / Income vs Rent Relationship")
    st.write(
        "How much of monthly income goes to rent? This 'rent burden' is critical for "
        "business survival. A shop paying 50% or more of income as rent faces high risk."
    )

    # Calculate rent burden
    df['rent_burden_pct'] = (df['monthly_rent_usd'] / df['monthly_income_usd'] * 100).round(1)

    fig5, ax5 = plt.subplots(figsize=(10, 6))
    scatter = ax5.scatter(
        df['monthly_income_usd'],
        df['monthly_rent_usd'],
        c=df['risk_score'],
        cmap='RdYlGn_r',
        s=100,
        alpha=0.6,
        edgecolors='black'
    )
    ax5.set_xlabel("Monthly Income (USD)", fontsize=12)
    ax5.set_ylabel("Monthly Rent (USD)", fontsize=12)
    ax5.set_title("Income vs Rent: Business Viability Analysis", fontsize=14, fontweight='bold')
    ax5.grid(alpha=0.3)

    # Add a reference line (where income = rent)
    max_val = max(df['monthly_income_usd'].max(), df['monthly_rent_usd'].max())
    ax5.plot([0, max_val], [0, max_val], 'k--', alpha=0.3, label='Income = Rent (breakeven)')
    ax5.legend()

    cbar = plt.colorbar(scatter, ax=ax5)
    cbar.set_label("Risk Score", fontsize=11)

    st.pyplot(fig5)

    # Display rent burden statistics
    st.write("**Rent Burden Analysis:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg Rent Burden", f"{df['rent_burden_pct'].mean():.1f}%")
    with col2:
        high_burden = len(df[df['rent_burden_pct'] > 50])
        st.metric("Shops with >50% Rent Burden", f"{high_burden} ({high_burden/len(df)*100:.0f}%)")
    with col3:
        st.metric("Max Rent Burden", f"{df['rent_burden_pct'].max():.1f}%")

    # ============================================================================
    # NEIGHBORHOOD ANALYSIS SECTION
    # ============================================================================
    st.subheader("التحليل حسب الحي / Neighborhood Analysis")
    st.write(
        "Different neighborhoods in Jerusalem may have different economic conditions. "
        "Let's see how risk and income vary geographically."
    )

    neighborhood_stats = df.groupby("neighborhood").agg({
        'risk_score': 'mean',
        'monthly_income_usd': 'mean',
        'shop_id': 'count'
    }).rename(columns={'shop_id': 'count'}).sort_values('risk_score', ascending=False)

    st.dataframe(neighborhood_stats.round(2))

    # ============================================================================
    # EDUCATIONAL RECOMMENDATIONS
    # ============================================================================
    st.info(
        "**Student Enhancement Ideas**:\n\n"
        "1. **Modify Risk Calculation**: Change the risk_score formula to emphasize "
        "different factors (e.g., higher weight for tax burden)\n\n"
        "2. **Add New Variables**: Incorporate additional factors:\n"
        "   - Debt levels\n"
        "   - Employee count\n"
        "   - Business age/experience\n"
        "   - Access to credit\n"
        "   - Market volatility\n\n"
        "3. **Use Real Data**: Replace synthetic data with actual economic surveys, "
        "municipal records, or field research\n\n"
        "4. **Policy Analysis**: Which neighborhoods/sectors need most support? "
        "Design interventions based on your findings\n\n"
        "5. **Visualization Improvements**: Create interactive maps, time-series analysis, "
        "or clustering visualizations"
    )

    st.info(
        "**أفكار تحسين للطلاب**:\n\n"
        "1. **تعديل حساب المخاطر**: تغيير معادلة risk_score لإعطاء وزن مختلف لعوامل مختلفة\n\n"
        "2. **إضافة متغيرات جديدة**:\n"
        "   - الديون والالتزامات\n"
        "   - عدد الموظفين\n"
        "   - عمر المشروع\n"
        "   - الوصول للتمويل\n"
        "   - تقلب السوق\n\n"
        "3. **استخدام بيانات حقيقية**: استبدال البيانات المصطنعة ببيانات من استطلاعات "
        "اقتصادية حقيقية أو أبحاث ميدانية\n\n"
        "4. **تحليل السياسات**: أي الأحياء والقطاعات تحتاج دعم أكثر؟ "
        "صمم تدخلات بناءً على نتائجك\n\n"
        "5. **تحسين التصور**: أنشئ خرائط تفاعلية أو تحليلات سلاسل زمنية"
    )


# Run the dashboard
if __name__ == "__main__":
    run()
