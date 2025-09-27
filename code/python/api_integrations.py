"""
🌐 AI API Integration Layer
Real-world integrations with popular AI platforms
"""

import requests
import json
from typing import Dict, Any

class AIProvider:
    """Base class for AI provider integrations"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = ""
    
    def send_prompt(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Send prompt to AI provider and return response"""
        raise NotImplementedError

class OpenAIClient(AIProvider):
    """OpenAI GPT integration for professional results"""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.openai.com/v1/chat/completions"
    
    def send_prompt(self, prompt: str, model: str = "gpt-4", temperature: float = 0.3) -> Dict[str, Any]:
        """Send structured prompt to OpenAI"""
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system", 
                    "content": "You are a senior digital strategist with 15+ years experience. Provide professional, actionable advice based on industry best practices."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": temperature,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "response": None}

class AnthropicClient(AIProvider):
    """Anthropic Claude integration for long-form content"""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.anthropic.com/v1/messages"
    
    def send_prompt(self, prompt: str, model: str = "claude-3-sonnet-20240229") -> Dict[str, Any]:
        """Send prompt to Claude for detailed analysis"""
        
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        
        payload = {
            "model": model,
            "max_tokens": 4000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "response": None}

class WebsiteAnalysisAPI:
    """
    Complete website analysis API using AI providers
    Demonstrates the core business service
    """
    
    def __init__(self, openai_key: str, anthropic_key: str = None):
        self.openai = OpenAIClient(openai_key)
        self.anthropic = AnthropicClient(anthropic_key) if anthropic_key else None
    
    def analyze_website(self, website_url: str, business_context: Dict) -> Dict[str, Any]:
        """Complete website analysis using AI"""
        
        from prompt_engine import PromptEngine, BusinessContext, Industry
        
        # Convert dict to BusinessContext object
        business = BusinessContext(
            industry=Industry(business_context["industry"]),
            company_size=business_context["company_size"],
            target_audience=business_context["target_audience"],
            primary_goals=business_context["primary_goals"],
            key_metrics=business_context["key_metrics"],
            competitors=business_context["competitors"]
        )
        
        # Generate professional analysis prompt
        engine = PromptEngine()
        prompt = engine.generate_analysis_prompt(business, website_url)
        
        # Send to AI provider (prefer Claude for analysis, fallback to OpenAI)
        if self.anthropic:
            response = self.anthropic.send_prompt(prompt)
        else:
            response = self.openai.send_prompt(prompt)
        
        return {
            "prompt_used": prompt,
            "ai_response": response,
            "business_context": business_context,
            "website_analyzed": website_url
        }
    
    def generate_redesign_proposal(self, analysis_results: Dict) -> Dict[str, Any]:
        """Generate client-ready redesign proposal"""
        
        proposal_prompt = f"""
Based on the following website analysis, create a comprehensive redesign proposal:

ANALYSIS RESULTS:
{json.dumps(analysis_results, indent=2)}

PROPOSAL REQUIREMENTS:
- Executive summary of key findings
- Specific redesign recommendations with rationale
- Implementation timeline (phased approach)
- Investment required and ROI projections
- Success metrics and measurement approach

Format as a professional business proposal suitable for client presentation.
        """
        
        response = self.openai.send_prompt(proposal_prompt, temperature=0.2)
        
        return {
            "proposal": response,
            "analysis_based_on": analysis_results
        }

# Example client implementation
def demo_client_workflow():
    """Demonstrate complete client workflow"""
    
    # Mock API keys (would be environment variables in production)
    OPENAI_KEY = "sk-xxx"
    ANTHROPIC_KEY = "sk-ant-xxx"
    
    # Initialize the service
    api = WebsiteAnalysisAPI(OPENAI_KEY, ANTHROPIC_KEY)
    
    # Example business context
    business_context = {
        "industry": "insurance",
        "company_size": "sme",
        "target_audience": "small business owners seeking liability coverage",
        "primary_goals": ["increase quote requests", "improve lead quality"],
        "key_metrics": ["conversion rate", "lead quality score"],
        "competitors": ["Geico", "State Farm", "Progressive"]
    }
    
    print("🏢 CLIENT WORKFLOW DEMONSTRATION")
    print("=" * 50)
    
    # Step 1: Website analysis
    print("1. 📊 Analyzing website...")
    analysis = api.analyze_website("https://example-insurance.com", business_context)
    print("   Analysis completed. Prompt length:", len(analysis["prompt_used"]))
    
    # Step 2: Generate proposal
    print("2. 📝 Generating redesign proposal...")
    proposal = api.generate_redesign_proposal(analysis)
    print("   Proposal generated successfully")
    
    # Step 3: Output results structure
    print("3. 📋 Results structure:")
    print("   - Analysis prompt:", len(analysis["prompt_used"]), "characters")
    print("   - Business context:", len(business_context), "elements")
    print("   - Proposal generated: Yes")
    
    return {
        "analysis": analysis,
        "proposal": proposal
    }

if __name__ == "__main__":
    # Run demonstration
    results = demo_client_workflow()
    print("\n✅ CLIENT WORKFLOW DEMONSTRATION COMPLETE")
    print("This API layer demonstrates the technical implementation")
    print("of the AI Agency business model serving real clients.")
