"""
🧠 AI Prompt Engineering Framework

A machine learning research project that systematizes prompt engineering
across multiple domains, treating AI communication as an optimization problem.
"""

__version__ = "1.0.0"
__author__ = "Dr-Istanbul AI Research Team"
__description__ = "Bridging AI capabilities and real-world applications through systematic prompt engineering"

from .prompt_engine import PromptEngine, BusinessContext, Industry
from .api_integrations import WebsiteAnalysisAPI
from .research_framework import ResearchExperiment, CrossDomainValidator

__all__ = [
    "PromptEngine", 
    "BusinessContext", 
    "Industry",
    "WebsiteAnalysisAPI",
    "ResearchExperiment",
    "CrossDomainValidator"
]
