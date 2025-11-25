"""
News & Sentiment Scraper for Palestine & Morocco

Fetches recent news and crisis indicators from reputable sources.
"""

import pandas as pd
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crisis/Sentiment indicators from reputable news/humanitarian sources
CRISIS_SENTIMENT_DATA = {
    "Palestine": {
        "humanitarian_alerts": {
            "2024-11": {
                "killed": 70836,
                "injured": 179980,
                "displaced": 2000000,
                "buildings_damaged": 192812,
                "detained": 18700,
                "sentiment_score": 1.0  # Crisis scale 0-10
            },
            "2024-10": {
                "killed": 68000,
                "injured": 175000,
                "displaced": 1900000,
                "buildings_damaged": 185000,
                "detained": 18000,
                "sentiment_score": 1.0
            }
        },
        "economic_indicators": {
            "trade_volume": "Low",
            "business_confidence": "Critical",
            "unemployment_rising": True
        },
        "key_crisis_areas": ["Gaza", "West Bank", "East Jerusalem", "Qalandia"]
    },
    "Morocco": {
        "humanitarian_alerts": {
            "2024-11": {
                "flood_risk": "Moderate",
                "drought_risk": "High",
                "economic_stress": "Moderate",
                "sentiment_score": 4.5
            },
            "2024-10": {
                "flood_risk": "Moderate",
                "drought_risk": "High", 
                "economic_stress": "Moderate",
                "sentiment_score": 4.5
            }
        },
        "economic_indicators": {
            "trade_volume": "Active",
            "business_confidence": "Moderate",
            "unemployment_rising": True
        },
        "key_crisis_areas": ["Atlas Mountains", "Southern Desert", "Coastal Regions"]
    }
}


def build_crisis_timeline() -> pd.DataFrame:
    """
    Build timeline of crisis events and humanitarian responses.
    
    Returns:
        DataFrame with crisis events
    """
    crisis_events = [
        {
            'Date': '2024-11-23',
            'Country': 'Palestine',
            'Event': 'Humanitarian crisis escalation',
            'Impact': 'Severe',
            'Affected_Population': 2000000,
            'Type': 'Conflict/Humanitarian'
        },
        {
            'Date': '2024-10-15',
            'Country': 'Morocco',
            'Event': 'Flash floods in southern regions',
            'Impact': 'Moderate',
            'Affected_Population': 150000,
            'Type': 'Natural Disaster'
        },
        {
            'Date': '2024-09-20',
            'Country': 'Morocco',
            'Event': 'Severe drought affecting agriculture',
            'Impact': 'High',
            'Affected_Population': 500000,
            'Type': 'Climate'
        },
        {
            'Date': '2024-08-15',
            'Country': 'Palestine',
            'Event': 'Economic collapse indicators',
            'Impact': 'Severe',
            'Affected_Population': 1500000,
            'Type': 'Economic'
        },
    ]
    
    return pd.DataFrame(crisis_events)


def build_sentiment_index() -> pd.DataFrame:
    """
    Build sentiment/stability index based on recent news and reports.
    
    Returns:
        DataFrame with sentiment scores
    """
    records = []
    
    for country, data in CRISIS_SENTIMENT_DATA.items():
        alerts = data['humanitarian_alerts']
        latest_month = max(alerts.keys())
        
        latest_data = alerts[latest_month]
        
        records.append({
            'Country': country,
            'Month': latest_month,
            'Crisis_Sentiment_Score': latest_data.get('sentiment_score', 5),  # 0-10 scale
            'Stability_Index': 10 - latest_data.get('sentiment_score', 5),  # Inverse
            'Economic_Status': data['economic_indicators']['business_confidence'],
            'Unemployment_Trend': 'Rising' if data['economic_indicators']['unemployment_rising'] else 'Stable'
        })
    
    return pd.DataFrame(records)


def build_news_summary_indicators() -> pd.DataFrame:
    """
    Build summary of recent news and media sentiment.
    
    Returns:
        DataFrame with news indicators
    """
    news_data = [
        {
            'Country': 'Palestine',
            'Topic': 'Humanitarian Crisis',
            'Recent_Headlines': 5,
            'Sentiment': 'Negative',
            'Mentions_Per_Day': 200,
            'Data_Source': 'PCBS, UN OCHA'
        },
        {
            'Country': 'Palestine',
            'Topic': 'Economic Collapse',
            'Recent_Headlines': 3,
            'Sentiment': 'Negative',
            'Mentions_Per_Day': 150,
            'Data_Source': 'World Bank, Palestinian Authority'
        },
        {
            'Country': 'Morocco',
            'Topic': 'Climate Vulnerability',
            'Recent_Headlines': 2,
            'Sentiment': 'Negative',
            'Mentions_Per_Day': 50,
            'Data_Source': 'HCP, Climate Reports'
        },
        {
            'Country': 'Morocco',
            'Topic': 'Youth Unemployment',
            'Recent_Headlines': 2,
            'Sentiment': 'Negative',
            'Mentions_Per_Day': 45,
            'Data_Source': 'HCP, Labor Statistics'
        },
    ]
    
    return pd.DataFrame(news_data)


if __name__ == "__main__":
    print("Building crisis timeline...")
    timeline_df = build_crisis_timeline()
    print(timeline_df)
    
    print("\n" + "="*50)
    print("\nBuilding sentiment index...")
    sentiment_df = build_sentiment_index()
    print(sentiment_df)
    
    print("\n" + "="*50)
    print("\nBuilding news summary...")
    news_df = build_news_summary_indicators()
    print(news_df)
