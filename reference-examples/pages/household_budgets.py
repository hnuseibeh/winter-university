"""
Household Budgets Dashboard
============================

This page analyzes household budget shocks in Palestinian territories,
examining how external economic shocks (fuel price increases, food price
increases, and mixed shocks) impact household financial deficits.

Students can explore:
- How budget deficits vary across different shock scenarios
- The breakdown of household expenditure shares across essential categories
- Regional variations in economic vulnerability
- The relationship between household size and financial stress
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# Define the path to the data file
DATA_PATH = Path(__file__).parents[1] / "data" / "palestine" / "household_budget_shocks.csv"


def load_data() -> pd.DataFrame:
    """
    Load household budget shock data from CSV file.

    Returns:
        pd.DataFrame: DataFrame containing household characteristics and budget impact data
    """
    df = pd.read_csv(DATA_PATH)
    return df


def run():
    """
    Main function to run the Household Budgets dashboard.

    This function:
    1. Displays the page title and educational context
    2. Loads the household budget data
    3. Provides interactive filters for region and shock scenario
    4. Displays multiple visualizations of budget impacts
    5. Shows key statistics and insights
    """

    # Page title and description
    st.title("💰 Household Budgets in Palestinian Territories")
    st.markdown(
        """
        ### Understanding Household Financial Vulnerability

        This dashboard examines how economic shocks affect household budgets in Palestinian territories.
        When external shocks occur (such as fuel price increases or food price increases), households
        struggle to afford essential goods and services, leading to budget deficits.

        **Key Concepts:**
        - **Shock Scenarios**: Different economic stress situations (fuel price +20%, food price +30%, or mixed shocks)
        - **Budget Deficit**: The amount (in USD) by which a household's essential expenditures exceed monthly income
        - **Expenditure Shares**: The percentage of household spending on food, energy, and transport
        - **Regional Variations**: Different areas experience different levels of economic vulnerability
        """
    )

    # Load the data
    df = load_data()

    # ===== SIDEBAR FILTERS =====
    st.sidebar.header("Filters")

    # Filter 1: Select region
    regions = sorted(df["region"].unique().tolist())
    selected_regions = st.sidebar.multiselect(
        "Region",
        regions,
        default=regions,
        help="Select one or more regions to filter the analysis"
    )

    # Filter 2: Select shock scenario
    shock_scenarios = sorted(df["shock_scenario"].unique().tolist())
    selected_shocks = st.sidebar.multiselect(
        "Shock Scenario",
        shock_scenarios,
        default=shock_scenarios,
        help="Select which economic shock scenarios to analyze"
    )

    # Apply filters
    dff = df[
        (df["region"].isin(selected_regions)) &
        (df["shock_scenario"].isin(selected_shocks))
    ]

    if len(dff) == 0:
        st.warning("No data matches your filter selection. Please adjust your filters.")
        return

    # ===== KEY STATISTICS =====
    st.subheader("📊 Overview Statistics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        avg_deficit = dff["simulated_new_budget_deficit_usd"].mean()
        st.metric("Average Deficit (USD)", f"${avg_deficit:.2f}")

    with col2:
        max_deficit = dff["simulated_new_budget_deficit_usd"].max()
        st.metric("Maximum Deficit (USD)", f"${max_deficit:.2f}")

    with col3:
        avg_household_size = dff["household_size"].mean()
        st.metric("Avg Household Size", f"{avg_household_size:.1f} people")

    with col4:
        avg_income = dff["monthly_income_usd"].mean()
        st.metric("Average Monthly Income (USD)", f"${avg_income:.2f}")

    # ===== MAIN VISUALIZATIONS =====
    st.divider()

    # Visualization 1: Budget Deficit by Shock Scenario
    st.subheader("1. Budget Deficit by Shock Scenario")
    st.markdown(
        """
        This chart shows the average budget deficit for each type of economic shock.
        A larger deficit indicates that households need more money to meet their essential needs.
        """
    )

    deficit_by_shock = dff.groupby("shock_scenario")["simulated_new_budget_deficit_usd"].agg(
        ["mean", "std", "count"]
    ).reset_index()

    fig1 = px.bar(
        deficit_by_shock,
        x="shock_scenario",
        y="mean",
        error_y="std",
        title="Average Household Budget Deficit by Shock Scenario",
        labels={
            "shock_scenario": "Shock Scenario",
            "mean": "Average Deficit (USD)"
        },
        color="shock_scenario",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig1.update_layout(
        xaxis_title="Shock Scenario",
        yaxis_title="Average Deficit (USD)",
        showlegend=False,
        hovermode="x unified"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Visualization 2: Expenditure Shares Breakdown
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("2. Average Expenditure Shares")
        st.markdown(
            """
            What percentage of household spending goes to different essential categories?
            These shares show budget priorities across the region.
            """
        )

        # Calculate average expenditure shares
        avg_shares = {
            "Food": dff["food_share_of_expenditure"].mean() * 100,
            "Energy": dff["energy_share_of_expenditure"].mean() * 100,
            "Transport": dff["transport_share_of_expenditure"].mean() * 100,
        }
        avg_shares["Other"] = 100 - sum(avg_shares.values())

        fig2 = go.Figure(
            data=[
                go.Pie(
                    labels=list(avg_shares.keys()),
                    values=list(avg_shares.values()),
                    marker=dict(
                        colors=px.colors.qualitative.Set2,
                        line=dict(color="white", width=2)
                    ),
                    textposition="auto",
                    hovertemplate="<b>%{label}</b><br>%{value:.1f}%<extra></extra>"
                )
            ]
        )
        fig2.update_layout(
            title="Average Household Expenditure Distribution"
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col_right:
        st.subheader("3. Expenditure Shares by Region")
        st.markdown(
            """
            Do different regions have different spending patterns?
            This stacked bar chart shows how budget priorities vary by location.
            """
        )

        # Calculate expenditure shares by region
        region_shares = dff.groupby("region")[
            ["food_share_of_expenditure", "energy_share_of_expenditure", "transport_share_of_expenditure"]
        ].mean().reset_index()

        region_shares = region_shares.rename(columns={
            "food_share_of_expenditure": "Food",
            "energy_share_of_expenditure": "Energy",
            "transport_share_of_expenditure": "Transport"
        })

        fig3 = go.Figure(
            data=[
                go.Bar(name="Food", x=region_shares["region"], y=region_shares["Food"] * 100),
                go.Bar(name="Energy", x=region_shares["region"], y=region_shares["Energy"] * 100),
                go.Bar(name="Transport", x=region_shares["region"], y=region_shares["Transport"] * 100),
            ]
        )
        fig3.update_layout(
            barmode="stack",
            title="Expenditure Shares by Region",
            xaxis_title="Region",
            yaxis_title="Percentage of Expenditure (%)",
            hovermode="x unified",
            height=400
        )
        st.plotly_chart(fig3, use_container_width=True)

    # Visualization 3: Regional Comparison of Impacts
    st.subheader("4. Regional Comparison: Budget Deficit Impact")
    st.markdown(
        """
        How does economic vulnerability differ across regions?
        This chart shows the average deficit for each region, broken down by shock type.
        """
    )

    deficit_by_region_shock = dff.groupby(["region", "shock_scenario"])[
        "simulated_new_budget_deficit_usd"
    ].mean().reset_index()

    fig4 = px.bar(
        deficit_by_region_shock,
        x="region",
        y="simulated_new_budget_deficit_usd",
        color="shock_scenario",
        title="Average Budget Deficit by Region and Shock Scenario",
        labels={
            "region": "Region",
            "simulated_new_budget_deficit_usd": "Average Deficit (USD)",
            "shock_scenario": "Shock Scenario"
        },
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig4.update_layout(
        xaxis_title="Region",
        yaxis_title="Average Deficit (USD)",
        hovermode="x unified"
    )
    st.plotly_chart(fig4, use_container_width=True)

    # Visualization 4: Household Size vs Budget Deficit
    st.subheader("5. Household Size and Budget Vulnerability")
    st.markdown(
        """
        Does having more family members increase financial stress?
        This scatter plot shows the relationship between household size and budget deficit,
        colored by shock scenario.
        """
    )

    fig5 = px.scatter(
        dff,
        x="household_size",
        y="simulated_new_budget_deficit_usd",
        color="shock_scenario",
        size="monthly_income_usd",
        hover_data=["region", "monthly_income_usd"],
        title="Household Size vs Budget Deficit",
        labels={
            "household_size": "Household Size (Number of People)",
            "simulated_new_budget_deficit_usd": "Budget Deficit (USD)",
            "shock_scenario": "Shock Scenario"
        },
        color_discrete_sequence=px.colors.qualitative.Set2,
        opacity=0.6
    )
    fig5.update_layout(
        hovermode="closest",
        xaxis=dict(dtick=1)  # Show integer values on x-axis
    )
    st.plotly_chart(fig5, use_container_width=True)

    # ===== DETAILED DATA TABLE =====
    st.divider()
    st.subheader("6. Detailed Data Table")
    st.markdown(
        """
        Explore the complete dataset with all household characteristics and shock impacts.
        You can sort and search through the data below.
        """
    )

    # Prepare display dataframe
    display_df = dff[[
        "household_id",
        "region",
        "household_size",
        "monthly_income_usd",
        "food_share_of_expenditure",
        "energy_share_of_expenditure",
        "transport_share_of_expenditure",
        "shock_scenario",
        "simulated_new_budget_deficit_usd"
    ]].copy()

    # Format columns for better readability
    display_df = display_df.rename(columns={
        "household_id": "Household ID",
        "region": "Region",
        "household_size": "Size",
        "monthly_income_usd": "Monthly Income (USD)",
        "food_share_of_expenditure": "Food Share",
        "energy_share_of_expenditure": "Energy Share",
        "transport_share_of_expenditure": "Transport Share",
        "shock_scenario": "Shock Scenario",
        "simulated_new_budget_deficit_usd": "Budget Deficit (USD)"
    })

    st.dataframe(display_df, use_container_width=True)

    # ===== KEY INSIGHTS =====
    st.divider()
    st.subheader("🔍 Key Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            **Deficit Severity:**
            - The average household budget deficit in the selected data is **${dff['simulated_new_budget_deficit_usd'].mean():.2f}**
            - Maximum deficit observed: **${dff['simulated_new_budget_deficit_usd'].max():.2f}**
            - {(dff['simulated_new_budget_deficit_usd'] > 0).sum()} out of {len(dff)} households ({(dff['simulated_new_budget_deficit_usd'] > 0).sum()/len(dff)*100:.1f}%) face a budget deficit

            **Household Characteristics:**
            - Households have an average of {dff['household_size'].mean():.1f} members
            - Average monthly income is ${dff['monthly_income_usd'].mean():.2f}
            """
        )

    with col2:
        st.markdown(
            f"""
            **Expenditure Patterns:**
            - Food represents {dff['food_share_of_expenditure'].mean()*100:.1f}% of household spending
            - Energy represents {dff['energy_share_of_expenditure'].mean()*100:.1f}% of household spending
            - Transport represents {dff['transport_share_of_expenditure'].mean()*100:.1f}% of household spending

            **Most Vulnerable Group:**
            - {dff.loc[dff['simulated_new_budget_deficit_usd'].idxmax(), 'region']} shows highest individual deficits
            - Mixed shocks tend to create {dff[dff['shock_scenario']=='mixed_shock']['simulated_new_budget_deficit_usd'].mean():.2f} USD average deficit
            """
        )
