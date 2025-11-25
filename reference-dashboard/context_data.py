"""
Research Context & Background Data extracted from academic reports.
This data is synthesized from 5 research PDFs about economic & social crises in Palestine & Morocco.
"""

RESEARCH_CONTEXT = {
    "about": {
        "title": "Economic & Social Crises in Palestine and Morocco",
        "subtitle": "AI-Driven Crisis Prediction and Data Visualization",
        "description": """
This project explores systemic economic and social crises in two distinct contexts:
**Palestine** (fragmented, occupation-constrained economy) and **Morocco** (climate-vulnerable, 
inequality-driven instability). The research foundation synthesizes legal frameworks, 
demographic pressures, labor market distortions, and environmental risks.
        """
    },
    "palestine": {
        "title": "Palestine: Economics of Strangulation & Fragmentation",
        "key_challenges": [
            {
                "name": "Structural Economy Constraints",
                "description": "Truncated economy where primary macroeconomic levers (currency, borders, trade) are controlled by external occupying power.",
                "indicators": ["Fiscal dependency on clearance revenues", "Fragmented labor market (Areas A, B, C)", "Limited digital infrastructure (3G/2G networks)"]
            },
            {
                "name": "East Jerusalem: Demographic Engineering",
                "description": "Deliberate multi-decade policy architecture to maintain Jewish majority (target: 60% by 2007) through settlement expansion and Palestinian displacement.",
                "indicators": [
                    "14,500+ residency revocations since 1967",
                    "13% of land allocated for Palestinian residential construction",
                    "100,000+ at risk of home demolition",
                    "40% of population receives ~10% of municipal budget"
                ]
            },
            {
                "name": "Existential Temporality: Qalandia Checkpoint",
                "description": "Weaponization of time through checkpoint delays—average 110 minutes—disrupting employment, healthcare access, and mental health.",
                "indicators": [
                    "26,000 daily crossers experiencing unpredictable delays",
                    "High sarcasm scores indicating psychological distress",
                    "Dark humor as coping mechanism for dehumanization"
                ]
            },
            {
                "name": "Commercial Ecosystem Collapse",
                "description": "Old City souvenir & crafts sector (371 shops, historically tourism-dependent) declined from stagnation to structural collapse 2023-2025.",
                "indicators": [
                    "~90% of businesses shuttered post-Oct 2023",
                    "'Administrative attrition' through tax enforcement & permit revocation",
                    "Separation Barrier cutting off labor supply & customer base"
                ]
            }
        ],
        "economic_metrics": {
            "gdp_loss_2000_2020": "$45 billion cumulative GDP loss due to occupation",
            "palestinian_contribution_to_economy": "7% from East Jerusalem",
            "worker_annual_earnings": "$3 billion (Palestinian workers in Israeli economy, early 2022)",
            "inequality": "Palestinian areas receive 10% of municipal budget despite 40% of population"
        }
    },
    "morocco": {
        "title": "Morocco: Vulnerability to Climate & Inequality",
        "key_challenges": [
            {
                "name": "Rain-Fed Economic Volatility",
                "description": "Agriculture-dependent economy highly sensitive to rainfall patterns. Droughts trigger rural income collapse, urban migration, and food price spikes.",
                "indicators": ["Variable agricultural yields", "Rural-urban migration pressure", "Food price inflation cycles"]
            },
            {
                "name": "Spatial Inequality & Multidimensional Poverty",
                "description": "Despite high open data availability ranking (24th globally), profound regional disparities are masked by national aggregates. Rural areas and urban peripheries concentrated with poverty.",
                "indicators": ["Rural poverty concentration", "Atlas Mountains subsistence farming", "Urban periphery vulnerability"]
            },
            {
                "name": "Youth Unemployment & Social Volatility",
                "description": "Structural mismatch between education outputs and labor market needs, particularly among youth. Creates pressure for migration and social unrest.",
                "indicators": ["High youth unemployment rates", "Education-labor mismatch by field", "Regional disparities in opportunity"]
            }
        ],
        "economic_metrics": {
            "data_ranking": "Open Data Inventory rank: 24th globally",
            "poverty_type": "Multidimensional poverty concentrated in rural & urban periphery",
            "primary_challenge": "Polycrisis: climate volatility + structural unemployment + inequality"
        }
    },
    "ai_applications": {
        "title": "AI & Crisis Prediction Opportunities",
        "methods": [
            {
                "method": "Satellite Remote Sensing",
                "use": "Monitor agricultural health (NDVI), industrial activity, urban sprawl",
                "example": "Agricultural stress monitoring in Morocco using vegetation indices"
            },
            {
                "method": "Natural Language Processing (NLP)",
                "use": "Analyze dialectal sentiment in Darija & Palestinian Arabic from social media",
                "example": "Sarcasm scoring at Qalandia checkpoint; sentiment analysis of economic stress"
            },
            {
                "method": "Telecom Mobility Data",
                "use": "Track displacement patterns, labor market shocks, checkpoint congestion",
                "example": "Mapping movement through Separation Barrier; detecting mass migration events"
            },
            {
                "method": "Scenario Modeling",
                "use": "Project supply-demand mismatches, drought impacts, unemployment trajectories",
                "example": "Education-labor scenario builder with policy levers (intake rates, job creation)"
            }
        ],
        "ethical_considerations": [
            "Data sovereignty & community-led governance",
            "Privacy preservation (avoid surveillance dual-use)",
            "Beware of algorithmic bias in conflict zones",
            "Transparent, accountable prediction models",
            "Distinction between monitoring & control"
        ]
    },
    "datasets_rationale": {
        "macro_indicators": {
            "title": "GDP, Unemployment, Youth Unemployment, Inflation (Palestine & Morocco)",
            "rationale": "Foundational macro-economic health indicators. Early warning system for aggregate shocks."
        },
        "education_labor_mismatch": {
            "title": "Field of Study vs. Job Demand Scenario Model (Palestine)",
            "rationale": "Students can project supply-demand divergence under different policy scenarios (intake rates, job creation). Hands-on policy simulation.",
            "interactive_elements": ["Graduate supply growth slider", "Job demand growth slider", "Projection horizon selector"]
        },
        "youth_unemployment": {
            "title": "Youth Unemployment by Region (Morocco)",
            "rationale": "Break down national averages to urban/rural divide. Reveals spatial inequality driving social volatility.",
            "feature": "Comparative regional trends (national vs. urban vs. rural)"
        },
        "micro_enterprises": {
            "title": "Micro-Enterprise Risk & Economic Resilience (East Jerusalem)",
            "rationale": "Operationalize 'administrative attrition' at business level. Show fragility of informal sector under policy pressure.",
            "metrics": ["Risk score distribution", "Monthly income by risk category", "Vulnerability to tax enforcement"]
        },
        "agricultural_stress": {
            "title": "Vegetation Health (NDVI) & Climate Vulnerability (Morocco)",
            "rationale": "Satellite-derived early warning for drought-driven migration and food insecurity. Link environmental data to economic collapse.",
            "feature": "Regional NDVI trends with seasonal patterns"
        }
    }
}

# Quick reference: Key research findings
KEY_INSIGHTS = {
    "palestine_economy": "Truncated by external control; depends on Israeli clearance revenues; lacks currency & trade sovereignty.",
    "east_jerusalem": "Architecture of control via residency revocation (14,500+), planning denial (13% land), tax enforcement, evictions.",
    "checkpoint_toll": "26,000 daily crossers; avg. 110 min delay; high sarcasm/dark humor indicating psychological trauma.",
    "old_city_collapse": "90% of shops shuttered; 'administrative attrition' via tax enforcement during zero-revenue period.",
    "morocco_climate": "Rain-fed GDP; droughts trigger rural-urban migration, food inflation, social unrest.",
    "inequality_gaps": "Multidimensional poverty masked by national averages; regional disparities require spatial AI disaggregation.",
    "youth_crisis": "Education-labor mismatch pressure; varies by field & region; creates migration & social volatility pressure.",
}

# Data visualization storytelling
NARRATIVES = {
    "qalandia": {
        "title": "Existential Temporality at Qalandia Checkpoint",
        "story": """
26,000 Palestinians cross Qalandia checkpoint daily, facing unpredictable 110-minute average delays.
This isn't just a traffic bottleneck—it's temporal warfare: the systematic weaponization of time 
to subordinate Palestinian lives to Israeli-imposed rhythms. 

Dark humor and sarcasm scores (0.85 high) are coping mechanisms for dehumanization. 
Communities communicate via real-time message networks (155 daily messages, 3.1x during incidents)
to mitigate risk and manage collective anxiety.

**Question:** How do we quantify psychological toll of systemic uncertainty?
        """
    },
    "old_city": {
        "title": "Administrative Attrition: Souvenir Cluster Collapse (2023-2025)",
        "story": """
The Old City's 371 souvenir shops sustained historic Palestinian commerce for decades, 
benefiting from tourism and pilgrimage flows. But post-Oct 2023 militarization + administrative
pressure (property tax enforcement, permit revocation) created a "zero-revenue fixed-cost crisis."

~90% of businesses now shuttered. This isn't kinetic destruction (like Gaza) but slow demographic 
engineering: merchants displaced via bureaucratic mechanisms, replaced by settlers, space 
transformed from living market to political stage.

**Question:** How do you survive fixed costs when customer revenue drops to zero?
        """
    },
    "climate_migration": {
        "title": "Rain-Fed Morocco: Drought → Migration → Social Unrest",
        "story": """
Morocco's rural economy hinges on rainfall. A drought doesn't just reduce yields—it cascades:
- Rural income collapse
- Mass migration to urban peripheries
- Urban unemployment spike
- Food price inflation
- Social volatility & unrest

Vegetation indices (NDVI) from satellites provide 2-4 month lead time for predicting these shocks,
enabling proactive humanitarian & economic interventions.

**Question:** Can we predict food crises before they trigger migration & instability?
        """
    }
}
