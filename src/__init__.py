"""Pharma Agentic AI - Main package.

This module provides the main Pharma Agentic AI system for pharmaceutical drug discovery
using multi-agent orchestration with Large Language Models.
"""

__version__ = "1.0.0"
__author__ = "Team P16"
__email__ = "team@pharma-agentic-ai.com"

from src.agents.base_agent import BaseAgent
from src.agents.drug_discovery_agent import DrugDiscoveryAgent
from src.agents.literature_agent import LiteratureAgent
from src.models.drug_model import DrugModel
from src.services.llm_service import LLMService

__all__ = [
    "BaseAgent",
    "DrugDiscoveryAgent",
    "LiteratureAgent",
    "DrugModel",
    "LLMService",
]
