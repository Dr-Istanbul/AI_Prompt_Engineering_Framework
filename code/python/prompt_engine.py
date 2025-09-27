"""
🎯 Advanced Prompt Engineering Engine
Core technology that powers the AI Agency business model
"""

import json
import re
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum

class Industry(Enum):
    INSURANCE = "insurance"
    LEGAL = "legal"
    HEALTHCARE = "healthcare"
    ECOMMERCE = "ecommerce"
    REAL_ESTATE = "real_estate"
    CONSULTING = "consulting"

@dataclass
class BusinessContext:
    """Structured business context for prompt engineering"""
    industry: Industry
    company_size: str  # "startup", "sme", "enterprise"
    target_audience: str
    primary_goals: List[str]
    key_metrics: List[str]
    competitors: List[str]

class PromptEngine:
    """
    Advanced prompt engineering system that transforms basic requests
    into agency-quality AI instructions
    """
    
    def __init__(self):
        self.templates = self._load_templates()
        self.industry_knowledge = self._load_industry_knowledge()
    
    def _load_templates(self) -> Dict[str, Any]:
        """Load advanced prompt templates"""
        return {
            "website_analysis": {
                "template": """
ACT as a Senior {industry} Web Strategist with {experience} years of experience.

BUSINESS CONTEXT ANALYSIS:
- Company: {company_name}
- Industry: {industry}
- Target Audience: {audience}
- Primary Goals: {goals}
- Key Competitors: {competitors}

TECHNICAL ANALYSIS REQUEST:
Conduct a comprehensive website analysis of {website_url} focusing on:

1. USER EXPERIENCE (UX) ASSESSMENT:
   - Navigation flow and information architecture
   - Mobile responsiveness and cross-device compatibility
   - Loading performance and technical optimization
   - Accessibility compliance (WCAG 2.1 standards)

2. CONVERSION OPTIMIZATION:
   - Call-to-action placement and effectiveness
   - Lead capture form optimization
   - User journey mapping and friction points
   - Trust signal implementation

3. CONTENT STRATEGY:
   - Message clarity and value proposition
   - SEO structure and keyword optimization
   - Content freshness and relevance
   - Competitive positioning

4. TECHNICAL PERFORMANCE:
   - Page speed metrics and optimization opportunities
   - Mobile-first indexing readiness
   - Security implementation and best practices
   - Integration capabilities with business systems

DELIVERABLE REQUIREMENTS:
- Present findings in a structured report format
- Include specific, actionable recommendations prioritized by impact
- Provide measurable success metrics for each recommendation
- Reference industry best practices and data-driven insights

RESPONSE FORMAT: JSON structure with analysis sections and priority scoring.
                """,
                "variables": ["industry", "experience", "company_name", "audience", "goals", "competitors", "website_url"]
            },
            
            "redesign_strategy": {
                "template": """
ACT as a Chief Digital Officer specializing in {industry} transformations.

STRATEGIC REDESIGN MANDATE:
Develop a comprehensive website redesign strategy for {company_name} that achieves:

BUSINESS OBJECTIVES:
- {primary_goal} improvement by {target_percentage}%
- Enhanced {key_metric} performance
- Competitive differentiation from {main_competitor}
- Market leadership positioning in {industry}

DESIGN PRINCIPLES:
- Implement {design_philosophy} methodology
- Ensure {accessibility_standard} compliance
- Optimize for {primary_device} experience
- Incorporate {brand_personality} aesthetic

TECHNICAL REQUIREMENTS:
- {cms_platform} integration capability
- {performance_target} loading speed
- {seo_framework} optimization
- {analytics_tool} implementation

DELIVERABLE: Phased implementation plan with timeline, resource allocation, and success metrics.
                """,
                "variables": ["industry", "company_name", "primary_goal", "target_percentage", "key_metric", 
                            "main_competitor", "design_philosophy", "accessibility_standard", "primary_device", 
                            "brand_personality", "cms_platform", "performance_target", "seo_framework", "analytics_tool"]
            }
        }
    
    def _load_industry_knowledge(self) -> Dict[Industry, Dict[str, Any]]:
        """Industry-specific knowledge for targeted prompts"""
        return {
            Industry.INSURANCE: {
                "keywords": ["trust", "security", "reliability", "protection"],
                "colors": ["blue", "navy", "white", "gray"],
                "metrics": ["quote requests", "policy purchases", "lead quality"],
                "competitors": ["State Farm", "Geico", "Allstate"]
            },
            Industry.LEGAL: {
                "keywords": ["expertise", "confidentiality", "experience", "results"],
                "colors": ["dark blue", "burgundy", "gold", "black"],
                "metrics": ["consultation bookings", "case submissions", "client retention"],
                "competitors": ["large firms", "boutique practices", "online services"]
            },
            Industry.ECOMMERCE: {
                "keywords": ["conversion", "shopping", "deals", "fast shipping"],
                "colors": ["varies by brand", "high contrast", "action-oriented"],
                "metrics": ["add-to-cart rate", "checkout completion", "average order value"],
                "competitors": ["Amazon", "niche players", "direct competitors"]
            }
        }
    
    def generate_analysis_prompt(self, business: BusinessContext, website_url: str) -> str:
        """Generate professional website analysis prompt"""
        industry_data = self.industry_knowledge.get(business.industry, {})
        
        prompt_template = self.templates["website_analysis"]["template"]
        
        # Fill template with business context
        filled_prompt = prompt_template.format(
            industry=business.industry.value.title(),
            experience="15",
            company_name="[Company Name]",
            audience=business.target_audience,
            goals=", ".join(business.primary_goals),
            competitors=", ".join(business.competitors),
            website_url=website_url
        )
        
        return self._enhance_with_industry_knowledge(filled_prompt, industry_data)
    
    def generate_redesign_prompt(self, business: BusinessContext, analysis_results: Dict) -> str:
        """Generate strategic redesign prompt based on analysis"""
        prompt_template = self.templates["redesign_strategy"]["template"]
        
        filled_prompt = prompt_template.format(
            industry=business.industry.value.title(),
            company_name="[Company Name]",
            primary_goal=business.primary_goals[0],
            target_percentage="40",
            key_metric=business.key_metrics[0],
            main_competitor=business.competitors[0] if business.competitors else "industry leaders",
            design_philosophy="mobile-first, conversion-focused",
            accessibility_standard="WCAG 2.1 AA",
            primary_device="mobile",
            brand_personality="professional yet approachable",
            cms_platform="WordPress/Webflow",
            performance_target="2-second",
            seo_framework="technical and content optimization",
            analytics_tool="Google Analytics 4"
        )
        
        return filled_prompt
    
    def _enhance_with_industry_knowledge(self, prompt: str, industry_data: Dict) -> str:
        """Enhance prompt with industry-specific insights"""
        enhancements = []
        
        if "keywords" in industry_data:
            enhancements.append(f"Industry keywords: {', '.join(industry_data['keywords'])}")
        if "colors" in industry_data:
            enhancements.append(f"Recommended color psychology: {', '.join(industry_data['colors'])}")
        
        if enhancements:
            prompt += f"\n\nINDUSTRY-SPECIFIC INSIGHTS:\n" + "\n".join(f"- {enhancement}" for enhancement in enhancements)
        
        return prompt

class PromptOptimizer:
    """
    Optimizes prompts based on performance feedback and A/B testing
    """
    
    def __init__(self):
        self.performance_data = []
    
    def add_performance_metric(self, prompt: str, results: Dict[str, Any]):
        """Track prompt performance for continuous improvement"""
        self.performance_data.append({
            "prompt": prompt,
            "results": results,
            "timestamp": "2024-01-01"  # Would be datetime.now() in production
        })
    
    def optimize_prompt(self, base_prompt: str, target_metric: str) -> str:
        """Optimize prompt based on historical performance"""
        # Simple optimization - in production would use ML
        optimizations = {
            "conversion_rate": "Add stronger call-to-action language and urgency indicators",
            "quality_score": "Increase specificity and add validation requirements",
            "speed": "Simplify language and reduce context length"
        }
        
        optimization = optimizations.get(target_metric, "Add more specific constraints and examples")
        
        return base_prompt + f"\n\nOPTIMIZATION FOR {target_metric.upper()}:\n- {optimization}"

# Example usage and demonstration
def demonstrate_agency_workflow():
    """Demonstrate the complete AI agency workflow"""
    
    # Initialize the prompt engineering engine
    engine = PromptEngine()
    optimizer = PromptOptimizer()
    
    # Example business context (insurance company)
    insurance_business = BusinessContext(
        industry=Industry.INSURANCE,
        company_size="sme",
        target_audience="small business owners seeking liability coverage",
        primary_goals=["increase quote requests", "improve lead quality", "reduce acquisition cost"],
        key_metrics=["conversion rate", "lead quality score", "time-to-quote"],
        competitors=["Geico", "State Farm", "Progressive"]
    )
    
    print("🚀 AI AGENCY WORKFLOW DEMONSTRATION")
    print("=" * 50)
    
    # Step 1: Generate professional analysis prompt
    analysis_prompt = engine.generate_analysis_prompt(
        insurance_business, 
        "https://example-insurance.com"
    )
    
    print("📊 GENERATED ANALYSIS PROMPT:")
    print(analysis_prompt[:500] + "...")  # Show first 500 chars
    print("\n" + "=" * 50)
    
    # Step 2: Generate redesign strategy prompt
    redesign_prompt = engine.generate_redesign_prompt(
        insurance_business,
        {"conversion_issues": ["weak CTAs", "complex forms", "missing trust signals"]}
    )
    
    print("🎨 GENERATED REDESIGN STRATEGY PROMPT:")
    print(redesign_prompt[:500] + "...")
    print("\n" + "=" * 50)
    
    # Step 3: Demonstrate optimization
    optimized_prompt = optimizer.optimize_prompt(analysis_prompt, "conversion_rate")
    
    print("⚡ OPTIMIZED PROMPT (Conversion Focus):")
    print("Original length:", len(analysis_prompt))
    print("Optimized length:", len(optimized_prompt))
    print("Optimization added:", len(optimized_prompt) - len(analysis_prompt), "characters")
    
    return {
        "analysis_prompt": analysis_prompt,
        "redesign_prompt": redesign_prompt,
        "optimized_prompt": optimized_prompt
    }

if __name__ == "__main__":
    # Run the demonstration
    results = demonstrate_agency_workflow()
    
    print("\n✅ DEMONSTRATION COMPLETE")
    print("This engine powers the AI Agency business model by transforming")
    print("basic requests into professional, results-driven AI instructions.")
