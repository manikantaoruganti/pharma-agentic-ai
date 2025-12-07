from typing import Dict, Any, List
import httpx
from .base_agent import BaseAgent

class ClinicalTrialsAgent(BaseAgent):
    """Agent for querying ClinicalTrials.gov API."""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://clinicaltrials.gov/api/v2"
    
    async def search_trials(self, drug_name: str, indication: str) -> List[Dict[str, Any]]:
        """Search for clinical trials matching drug and indication."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/studies",
                params={
                    "query.intr": drug_name,
                    "query.cond": indication,
                    "format": "json"
                }
            )
            data = response.json()
            return data.get("studies", [])
    
    async def get_trial_details(self, nct_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific trial."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/studies/{nct_id}")
            return response.json()
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """Execute clinical trials search."""
        # Parse task format: "drug:indication"
        parts = task.split(":")
        drug = parts[0] if len(parts) > 0 else "aspirin"
        indication = parts[1] if len(parts) > 1 else "cardiovascular"
        
        trials = await self.search_trials(drug, indication)
        
        return {
            "total_trials": len(trials),
            "trials": trials[:10],  # Return top 10
            "drug": drug,
            "indication": indication
        }
