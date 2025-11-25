"""
World Bank Data Scraper for Palestine & Morocco

Fetches economic indicators from World Bank Open Data API.
Reference: https://datahelpdesk.worldbank.org/knowledgebase/articles/889386
"""

import requests
import pandas as pd
from typing import Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# World Bank API base URL
WB_API = "https://api.worldbank.org/v2"

# Indicators to fetch (World Bank Indicator Codes)
INDICATORS = {
    "gdp_usd": "NY.GDP.MKTP.CD",  # GDP (current US$)
    "gdp_growth": "NY.GDP.MKTP.KD.ZG",  # GDP growth (annual %)
    "inflation": "FP.CPI.TOTL.ZG",  # Inflation, consumer prices (annual %)
    "unemployment": "SP.URB.TOTL.IN.ZS",  # Urban population (% of total)
    "population": "SP.POP.TOTL",  # Population, total
    "poverty_headcount": "SI.POV.NAHC",  # Poverty headcount ratio at national poverty line
    "gini_index": "SI.POV.GINI",  # GINI index
    "life_expectancy": "SP.DYN.LE00.IN",  # Life expectancy at birth
    "school_enrollment": "SE.ADT.LITR.ZS",  # Literacy rate
    "fdi_net_inflows": "BX.KLT.DINV.CD.WD",  # Foreign direct investment, net inflows
}

# Countries
COUNTRIES = {
    "palestine": "PSE",
    "morocco": "MAR",
}

# Years to fetch
START_YEAR = 2018
END_YEAR = 2024


def fetch_indicator(country_code: str, indicator_code: str, start_year: int = START_YEAR, 
                   end_year: int = END_YEAR) -> pd.DataFrame:
    """
    Fetch a specific indicator from World Bank API for a country.
    
    Args:
        country_code: ISO 3-letter country code (e.g., 'PSE', 'MAR')
        indicator_code: World Bank indicator code
        start_year: Start year for data
        end_year: End year for data
    
    Returns:
        DataFrame with Year, Value columns
    """
    try:
        url = f"{WB_API}/country/{country_code}/indicator/{indicator_code}"
        params = {
            "format": "json",
            "date": f"{start_year}:{end_year}",
            "per_page": 100
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if len(data) < 2 or not data[1]:
            logger.warning(f"No data for {country_code} / {indicator_code}")
            return pd.DataFrame()
        
        # Parse data
        records = []
        for record in data[1]:
            if record['value'] is not None:
                records.append({
                    'Year': int(record['date']),
                    'Value': float(record['value']),
                    'Country': country_code
                })
        
        return pd.DataFrame(records).sort_values('Year')
    
    except Exception as e:
        logger.error(f"Error fetching {indicator_code} for {country_code}: {e}")
        return pd.DataFrame()


def fetch_all_indicators(country_code: str, indicators: Optional[Dict] = None) -> Dict[str, pd.DataFrame]:
    """
    Fetch all indicators for a country.
    
    Args:
        country_code: ISO country code
        indicators: Dict of indicator_name -> indicator_code
    
    Returns:
        Dict of indicator_name -> DataFrame
    """
    if indicators is None:
        indicators = INDICATORS
    
    results = {}
    for name, code in indicators.items():
        logger.info(f"Fetching {name} for {country_code}...")
        results[name] = fetch_indicator(country_code, code)
    
    return results


def build_macro_indicators_csv() -> pd.DataFrame:
    """
    Build macro indicators CSV with GDP, inflation, growth for Palestine & Morocco.
    
    Returns:
        DataFrame with Year, Country, GDP (USD), GDP Growth (%), Inflation (%)
    """
    records = []
    
    for country_name, country_code in COUNTRIES.items():
        indicators = fetch_all_indicators(country_code, {
            'gdp': INDICATORS['gdp_usd'],
            'gdp_growth': INDICATORS['gdp_growth'],
            'inflation': INDICATORS['inflation']
        })
        
        # Merge on Year
        df_country = pd.DataFrame()
        for indicator_name, df in indicators.items():
            if not df.empty:
                df_pivot = df[['Year', 'Value']].rename(columns={'Value': indicator_name})
                if df_country.empty:
                    df_country = df_pivot
                else:
                    df_country = df_country.merge(df_pivot, on='Year', how='outer')
        
        if not df_country.empty:
            df_country['Country'] = country_name.capitalize()
            records.append(df_country)
    
    if records:
        return pd.concat(records, ignore_index=True)
    return pd.DataFrame()


def build_employment_indicators() -> pd.DataFrame:
    """
    Build employment & unemployment data.
    
    Returns:
        DataFrame with employment indicators
    """
    records = []
    
    for country_name, country_code in COUNTRIES.items():
        logger.info(f"Fetching employment data for {country_name}...")
        df = fetch_indicator(country_code, INDICATORS.get('unemployment', ''))
        if not df.empty:
            df['Country'] = country_name.capitalize()
            records.append(df)
    
    if records:
        return pd.concat(records, ignore_index=True)
    return pd.DataFrame()


def build_demographic_indicators() -> pd.DataFrame:
    """
    Build demographic data (population, life expectancy, literacy).
    
    Returns:
        DataFrame with demographic indicators
    """
    records = []
    
    for country_name, country_code in COUNTRIES.items():
        indicators = fetch_all_indicators(country_code, {
            'population': INDICATORS['population'],
            'life_expectancy': INDICATORS['life_expectancy'],
            'literacy': INDICATORS['school_enrollment']
        })
        
        df_country = pd.DataFrame()
        for indicator_name, df in indicators.items():
            if not df.empty:
                df_pivot = df[['Year', 'Value']].rename(columns={'Value': indicator_name})
                if df_country.empty:
                    df_country = df_pivot
                else:
                    df_country = df_country.merge(df_pivot, on='Year', how='outer')
        
        if not df_country.empty:
            df_country['Country'] = country_name.capitalize()
            records.append(df_country)
    
    if records:
        return pd.concat(records, ignore_index=True)
    return pd.DataFrame()


if __name__ == "__main__":
    # Test fetching
    print("Fetching macro indicators...")
    macro_df = build_macro_indicators_csv()
    print(macro_df.head(10))
    print(f"\nShape: {macro_df.shape}")
    
    print("\n" + "="*50 + "\n")
    print("Fetching demographic indicators...")
    demo_df = build_demographic_indicators()
    print(demo_df.head(10))
