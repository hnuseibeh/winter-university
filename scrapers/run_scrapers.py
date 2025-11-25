"""
Master Scraper Runner

Orchestrates all data scrapers and generates CSV files for the dashboard.
"""

import sys
import os
from pathlib import Path
import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import scrapers
from climate_humanitarian_scraper import (
    build_climate_vulnerability_index,
    build_humanitarian_indicators,
    build_agricultural_stress_indicators
)
from news_sentiment_scraper import (
    build_crisis_timeline,
    build_sentiment_index,
    build_news_summary_indicators
)

# For World Bank scraper (requires requests library)
try:
    from worldbank_scraper import build_macro_indicators_csv, build_demographic_indicators
    WB_AVAILABLE = True
except ImportError:
    logger.warning("requests library not available - World Bank scraper disabled")
    WB_AVAILABLE = False


class RealDataScraper:
    """Master orchestrator for all data scrapers."""
    
    def __init__(self, output_dir=None):
        """
        Initialize scraper with output directory.
        
        Args:
            output_dir: Directory to save CSV files (default: ../winter-school-econ-social-crises/data)
        """
        if output_dir is None:
            # Auto-detect project directory
            script_dir = Path(__file__).parent
            output_dir = script_dir.parent / "winter-school-econ-social-crises" / "data"
        
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {self.output_dir}")
    
    def save_csv(self, df: pd.DataFrame, filename: str):
        """Save DataFrame to CSV."""
        if df.empty:
            logger.warning(f"DataFrame for {filename} is empty - skipping")
            return
        
        filepath = self.output_dir / filename
        df.to_csv(filepath, index=False)
        logger.info(f"✅ Saved: {filename} ({len(df)} rows)")
    
    def scrape_all(self):
        """Run all scrapers and generate CSVs."""
        logger.info("🚀 Starting comprehensive data scraping...\n")
        
        # 1. Climate & Humanitarian Data
        logger.info("📊 Scraping climate & humanitarian indicators...")
        climate_df = build_climate_vulnerability_index()
        humanitarian_df = build_humanitarian_indicators()
        ag_stress_df = build_agricultural_stress_indicators()
        
        self.save_csv(climate_df, "climate_vulnerability_index.csv")
        self.save_csv(humanitarian_df, "humanitarian_indicators.csv")
        self.save_csv(ag_stress_df, "morocco_agricultural_stress.csv")
        
        # 2. Crisis & Sentiment Data
        logger.info("\n📰 Scraping news & sentiment indicators...")
        timeline_df = build_crisis_timeline()
        sentiment_df = build_sentiment_index()
        news_df = build_news_summary_indicators()
        
        self.save_csv(timeline_df, "crisis_timeline.csv")
        self.save_csv(sentiment_df, "sentiment_index.csv")
        self.save_csv(news_df, "news_summary.csv")
        
        # 3. World Bank Data (if available)
        if WB_AVAILABLE:
            logger.info("\n🏦 Scraping World Bank indicators...")
            try:
                macro_df = build_macro_indicators_csv()
                demographic_df = build_demographic_indicators()
                
                self.save_csv(macro_df, "macro_indicators_real.csv")
                self.save_csv(demographic_df, "demographic_indicators.csv")
            except Exception as e:
                logger.error(f"World Bank scraping failed: {e}")
        else:
            logger.warning("\n⚠️  World Bank scraper requires 'requests' library")
        
        # 4. Summary Report
        logger.info("\n" + "="*60)
        logger.info("📋 SCRAPING COMPLETE")
        logger.info("="*60)
        
        files_created = len(list(self.output_dir.glob("*.csv")))
        logger.info(f"✅ Created/Updated {files_created} CSV files")
        logger.info(f"📁 Location: {self.output_dir}")
        logger.info("\nFiles generated:")
        for csv_file in sorted(self.output_dir.glob("*.csv")):
            df = pd.read_csv(csv_file)
            logger.info(f"  • {csv_file.name} ({len(df)} rows, {len(df.columns)} cols)")


def main():
    """Run the master scraper."""
    # Try to find the project directory
    script_dir = Path(__file__).parent
    
    # Try to detect which project to write to
    possible_dirs = [
        script_dir.parent / "winter-school-econ-social-crises" / "data",
        script_dir.parent / "econ_social_crises_dashboard" / "data",
    ]
    
    output_dir = None
    for possible_dir in possible_dirs:
        if possible_dir.parent.exists():
            output_dir = possible_dir
            break
    
    if output_dir is None:
        # Fallback
        output_dir = script_dir.parent / "data_output"
    
    scraper = RealDataScraper(output_dir=output_dir)
    scraper.scrape_all()
    
    logger.info("\n💡 Next steps:")
    logger.info("  1. Review generated CSV files")
    logger.info("  2. Update dashboard pages to use new data")
    logger.info("  3. Run: streamlit run app.py")


if __name__ == "__main__":
    main()
