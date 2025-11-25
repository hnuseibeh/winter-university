"""
Data Explorer – Plug-and-Play Dashboard Module

This module implements a generic, plug-and-play dashboard for exploring CSV datasets.
The key philosophy is:
  - Auto-detect CSV files from the data/ directory and all subdirectories
  - Require NO code changes when adding new datasets
  - Support preset configurations for known datasets (title, default axes, etc.)
  - Provide three interactive tabs: Overview, Plot, Data Table
  - Support text filtering, multiple chart types, and CSV export

To use:
  1. Add CSV files to the data/ folder (or subdirectories like data/palestine/, data/morocco/)
  2. Optionally add a preset in DATASET_PRESETS for customization
  3. Run the Streamlit app – the dashboard auto-discovers your data

No code modifications needed when adding new datasets!
"""

import streamlit as st
import pandas as pd
from pathlib import Path

# ---------- CONFIGURATION ----------
# Data directory is relative to this file's location (in pages/)
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Preset configurations for known datasets
# Allows custom titles and default plot axes without changing code
DATASET_PRESETS = {
    # Morocco datasets
    "morocco_youth_unemployment.csv": {
        "x": "year",
        "y": "national_youth_unemployment_rate",
        "title": "بطالة الشباب في المغرب / Youth Unemployment – Morocco",
    },
    "morocco_agri_stress.csv": {
        "x": "year",
        "y": "cereal_yield_kg_per_ha",
        "title": "إنتاج الحبوب في المغرب / Cereal Yield – Morocco",
    },
    "food_price_index_monthly.csv": {
        "x": "month",
        "y": "index",
        "title": "مؤشر أسعار الغذاء في المغرب / Food Price Index – Morocco",
    },

    # Palestine datasets
    "youth_education_employment.csv": {
        "x": "year",
        "y": "employment_rate",
        "title": "تعليم الشباب والتوظيف في فلسطين / Youth Education & Employment – Palestine",
    },

    # Jerusalem datasets
    "neighborhood_vulnerability.csv": {
        "x": "neighborhood",
        "y": "eviction_risk_score",
        "title": "هشاشة أحياء القدس / Jerusalem Neighborhood Vulnerability",
    },
}


# ---------- HELPER FUNCTIONS ----------

@st.cache_data
def list_csv_files(data_dir: Path):
    """
    Recursively find all CSV files in data_dir and subdirectories.
    Returns file paths relative to the data directory, sorted alphabetically.

    Example output:
      ["morocco/youth_unemployment.csv", "palestine/employment.csv", "macro/gdp.csv"]
    """
    if not data_dir.exists():
        return []

    csv_files = []
    for csv_file in data_dir.rglob("*.csv"):
        relative_path = csv_file.relative_to(data_dir)
        csv_files.append(str(relative_path))

    return sorted(csv_files)


@st.cache_data
def load_dataset(filepath: Path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)


def detect_numeric_columns(df: pd.DataFrame):
    """Return list of numeric column names."""
    return [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]


def detect_categorical_columns(df: pd.DataFrame):
    """Return list of categorical (object/text) column names."""
    return [c for c in df.columns if df[c].dtype == "object"]


def get_preset_key(relative_path: str):
    """
    Extract the filename (without directory) to match against DATASET_PRESETS.

    Example:
      "palestine/youth_education_employment.csv" -> "youth_education_employment.csv"
    """
    return Path(relative_path).name


# ---------- PAGE CONFIGURATION ----------

st.set_page_config(
    page_title="Data Explorer – Consolidated Dashboard",
    layout="wide",
)

st.title("📊 Data Explorer")
st.markdown(
    """
**Plug-and-Play Data Dashboard**

Automatically discovers and visualizes all CSV files in the `data/` folder and subdirectories.
Choose any dataset, explore it visually, filter data, and export results—all without modifying code.

**استكشاف البيانات**
لوحة بيانات تفاعلية تكتشف تلقائياً جميع ملفات CSV في مجلد البيانات.
"""
)

# ---------- SIDEBAR: DATASET SELECTION ----------

st.sidebar.header("📁 Dataset Selection")

if not DATA_DIR.exists():
    st.sidebar.error(f"Data directory not found: {DATA_DIR}")
    st.stop()

csv_files = list_csv_files(DATA_DIR)

if not csv_files:
    st.sidebar.warning("No CSV files found in data/ folder. Add CSV files and restart the app.")
    st.stop()

dataset_relative_path = st.sidebar.selectbox(
    "Choose a dataset file",
    csv_files,
    help="Select from all CSV files discovered in data/ and subdirectories"
)

dataset_path = DATA_DIR / dataset_relative_path
df = load_dataset(dataset_path)

st.sidebar.success(f"✓ Loaded: {dataset_relative_path}")
st.sidebar.write(f"**Rows:** {len(df)} | **Columns:** {len(df.columns)}")

# Get preset configuration (if any)
preset_key = get_preset_key(dataset_relative_path)
preset = DATASET_PRESETS.get(preset_key, {})
title = preset.get("title", dataset_relative_path)

# ---------- MAIN TABS ----------

tab_overview, tab_plot, tab_table = st.tabs(
    ["🔍 Overview", "📊 Plot", "📋 Data Table"]
)

# ===== TAB 1: OVERVIEW =====

with tab_overview:
    st.subheader(title)

    st.markdown("### Dataset Information")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.write("")

    st.markdown("### Column Names")
    st.write(list(df.columns))

    with st.expander("📊 Descriptive Statistics"):
        st.write(df.describe(include="all"))

# ===== TAB 2: PLOT =====

with tab_plot:
    st.subheader("📊 Create a Visualization")

    numeric_cols = detect_numeric_columns(df)
    cat_cols = detect_categorical_columns(df)

    if not numeric_cols:
        st.warning("⚠️ No numeric columns found in this dataset. Cannot create plots.")
    else:
        # Set default axes from preset (if available)
        default_x = preset.get("x")
        default_y = preset.get("y")

        # X-axis selector
        default_x_idx = 0
        if default_x and default_x in df.columns:
            default_x_idx = df.columns.get_loc(default_x)

        x_axis = st.selectbox(
            "X-axis (horizontal)",
            options=list(df.columns),
            index=default_x_idx,
        )

        # Y-axis selector (numeric only)
        default_y_idx = 0
        if default_y and default_y in numeric_cols:
            default_y_idx = numeric_cols.index(default_y)

        y_axis = st.selectbox(
            "Y-axis (numeric)",
            options=numeric_cols,
            index=default_y_idx,
        )

        # Color/grouping selector
        color_by = st.selectbox(
            "Color/group by (optional)",
            options=["(None)"] + cat_cols,
            index=0,
        )

        # Chart type options
        st.markdown("### Chart Type")
        chart_type = st.radio(
            "Select chart type",
            ["Line", "Bar", "Scatter"],
            horizontal=True,
        )

        # Text filter
        st.markdown("### Text Filter")
        filter_text = st.text_input(
            "Filter rows by text (searches all text columns)",
            help="Enter a word or phrase to filter rows"
        )

        # Apply filter
        df_filtered = df.copy()
        if filter_text.strip():
            mask = pd.Series([False] * len(df_filtered))
            for col in cat_cols:
                mask = mask | df_filtered[col].astype(str).str.contains(
                    filter_text, case=False, na=False
                )
            df_filtered = df_filtered[mask]

        st.write(f"**Rows after filter:** {len(df_filtered)} (original: {len(df)})")

        if len(df_filtered) == 0:
            st.warning("⚠️ No rows match the current filter.")
        else:
            try:
                if chart_type == "Line":
                    st.line_chart(
                        df_filtered.set_index(x_axis)[[y_axis]],
                        height=400,
                        use_container_width=True,
                    )
                elif chart_type == "Bar":
                    st.bar_chart(
                        df_filtered.set_index(x_axis)[[y_axis]],
                        height=400,
                        use_container_width=True,
                    )
                else:  # Scatter
                    import altair as alt

                    base = alt.Chart(df_filtered).mark_circle(size=60).encode(
                        x=alt.X(x_axis, title=x_axis),
                        y=alt.Y(y_axis, title=y_axis),
                    )

                    if color_by != "(None)" and color_by in df_filtered.columns:
                        base = base.encode(color=color_by)

                    st.altair_chart(base.interactive(), use_container_width=True)

            except Exception as e:
                st.error(f"Error creating plot: {e}")

# ===== TAB 3: DATA TABLE =====

with tab_table:
    st.subheader("📋 Data Table")
    st.markdown("View the full dataset or filtered results, and export as CSV.")

    show_filtered = st.checkbox(
        "Show filtered version (from Plot tab)",
        value=True,
    )

    if show_filtered and "df_filtered" in locals():
        st.dataframe(df_filtered, use_container_width=True)
        csv_to_download = df_filtered
        display_count = len(df_filtered)
    else:
        st.dataframe(df, use_container_width=True)
        csv_to_download = df
        display_count = len(df)

    st.write(f"Displaying {display_count} rows")

    # CSV export button
    csv_bytes = csv_to_download.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="⬇️ Download as CSV",
        data=csv_bytes,
        file_name=f"export_{Path(dataset_relative_path).stem}.csv",
        mime="text/csv",
    )
