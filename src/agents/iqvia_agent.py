import asyncio
from typing import Dict, Any
import httpx
from .base_agent import BaseAgent

class IQVIAAgent(BaseAgent):
    """Agent for fetching market data from IQVIA API."""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.iqvia_api_key = api_key
        self.base_url = "https://api.iqvia.com/pharma"
    
    async def fetch_market_size(self, drug_name: str) -> Dict[str, Any]:
        """Fetch market size data for a drug."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/market-size",
                params={"drug": drug_name},
                headers={"Authorization": f"Bearer {self.iqvia_api_key}"}
            )
            return response.json()
    
    async def fetch_sales_trends(self, drug_name: str) -> Dict[str, Any]:
        """Fetch historical sales trends for a drug."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/sales-trends",
                params={"drug": drug_name},
                headers={"Authorization": f"Bearer {self.iqvia_api_key}"}
            )
            return response.json()
    
    async def fetch_competitor_data(self, indication: str) -> Dict[str, Any]:
        """Fetch competitive landscape for an indication."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/competitors",
                params={"indication": indication},
                headers={"Authorization": f"Bearer {self.iqvia_api_key}"}
            )
            return response.json()
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """Execute the IQVIA agent task."""
        market_size = await self.fetch_market_size(task)
        trends = await self.fetch_sales_trends(task)
        competitors = await self.fetch_competitor_data(task)
        
        return {
            "market_size": market_size,
            "sales_trends": trends,
            "competitive_landscape": competitors
        }
