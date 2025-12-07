"""Base Agent class for Pharma Agentic AI.

Defines the abstract base class for all agents in the system.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from datetime import datetime


class AgentConfig(BaseModel):
    """Configuration for an agent."""
    name: str
    description: str
    version: str = "1.0.0"
    max_retries: int = 3
    timeout: Optional[int] = None


class BaseAgent(ABC):
    """Abstract base class for all agents."""

    def __init__(self, config: AgentConfig):
        """Initialize the agent with configuration."""
        self.config = config
        self.created_at = datetime.now()
        self.last_updated = datetime.now()

    @abstractmethod
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent with given input data."""
        pass

    @abstractmethod
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """Validate input data for the agent."""
        pass

    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the agent."""
        return {
            "name": self.config.name,
            "status": "active",
            "created_at": self.created_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
        }
