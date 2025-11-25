"""
Shared utilities for loading and caching data across pages.
"""

import pathlib
import streamlit as st
import pandas as pd


@st.cache_data
def load_data(filename: str, data_dir: str = "data") -> pd.DataFrame:
    """
    Load CSV file from data directory with caching.
    
    Args:
        filename: Name of CSV file (e.g., "macro_indicators.csv")
        data_dir: Subdirectory name (default "data")
    
    Returns:
        Loaded DataFrame or empty DataFrame if file not found
    """
    file_path = pathlib.Path(__file__).parent.parent / data_dir / filename
    
    try:
        df = pd.read_csv(file_path)
        # Auto-parse date columns if they exist
        for col in df.columns:
            if 'date' in col.lower() or 'year' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col])
                except Exception:
                    pass
        return df
    except FileNotFoundError:
        st.error(f"Data file not found: {filename}")
        return pd.DataFrame()


def safe_numeric(df: pd.DataFrame, column: str, default=0):
    """Safely convert column to numeric, handling errors."""
    return pd.to_numeric(df[column], errors='coerce').fillna(default)
