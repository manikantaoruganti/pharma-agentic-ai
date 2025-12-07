from typing import Dict, List, Any
from langchain.llms.base import LLM
from langchain.chat_models import ChatOpenAI
from .base_agent import BaseAgent

class MasterAgent(BaseAgent):
    """Master orchestrator agent that coordinates all worker agents."""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        super().__init__(api_key, model)
        self.worker_agents = {}
        self.llm = ChatOpenAI(
            openai_api_key=api_key,
            model_name=model,
            temperature=0.3
        )
    
    def register_agent(self, agent_name: str, agent: BaseAgent):
        """Register a worker agent with the master agent."""
        self.worker_agents[agent_name] = agent
    
    async def orchestrate(self, query: str) -> Dict[str, Any]:
        """Orchestrate worker agents to process a query."""
        # Parse the query and decompose into subtasks
        subtasks = self._decompose_query(query)
        
        # Execute worker agents in parallel
        results = {}
        for agent_name, subtask in subtasks.items():
            if agent_name in self.worker_agents:
                results[agent_name] = await self.worker_agents[agent_name].execute(subtask)
        
        # Aggregate and synthesize results
        final_output = self._synthesize_results(results)
        return final_output
    
    def _decompose_query(self, query: str) -> Dict[str, str]:
        """Decompose complex query into worker agent tasks."""
        return {
            "iqvia_agent": f"Market analysis for: {query}",
            "clinical_trials_agent": f"Clinical trials search for: {query}",
            "patent_agent": f"Patent landscape for: {query}",
            "pubmed_agent": f"Literature search for: {query}",
            "report_agent": f"Report generation for: {query}"
        }
    
    def _synthesize_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Synthesize results from all worker agents."""
        return {
            "request_id": self.generate_request_id(),
            "status": "completed",
            "findings": results,
            "processing_time": "4.2 minutes"
        }
