"""
🔬 Research Framework for Prompt Engineering Studies
ML-focused components for systematic experimentation
"""

import numpy as np
from typing import List, Dict, Any
from dataclasses import dataclass
from sklearn.metrics import precision_score, recall_score

@dataclass
class ExperimentResult:
    """Structured results for prompt engineering experiments"""
    prompt_variation: str
    domain: str
    task: str
    performance_metrics: Dict[str, float]
    execution_time: float
    token_usage: int

class ResearchExperiment:
    """ML-style experimentation framework for prompt engineering"""
    
    def __init__(self):
        self.results = []
        self.metrics_tracker = MetricsTracker()
    
    def run_ab_test(self, prompt_a: str, prompt_b: str, 
                   domain: str, task: str, n_iterations: int = 10) -> Dict[str, Any]:
        """A/B test different prompt variations"""
        
        results_a = []
        results_b = []
        
        for i in range(n_iterations):
            # Execute both prompts and collect results
            result_a = self.execute_prompt(prompt_a, domain, task)
            result_b = self.execute_prompt(prompt_b, domain, task)
            
            results_a.append(result_a)
            results_b.append(result_b)
        
        # Statistical analysis
        analysis = self.analyze_results(results_a, results_b)
        
        return {
            "prompt_a_results": results_a,
            "prompt_b_results": results_b,
            "statistical_analysis": analysis,
            "recommendation": self.get_recommendation(analysis)
        }
    
    def analyze_results(self, results_a: List, results_b: List) -> Dict[str, float]:
        """Statistical analysis of experiment results"""
        # Extract performance scores
        scores_a = [r.performance_metrics["composite_score"] for r in results_a]
        scores_b = [r.performance_metrics["composite_score"] for r in results_b]
        
        # Basic statistical tests
        mean_a, mean_b = np.mean(scores_a), np.mean(scores_b)
        std_a, std_b = np.std(scores_a), np.std(scores_b)
        
        # T-test equivalent (simplified)
        effect_size = (mean_b - mean_a) / np.sqrt((std_a**2 + std_b**2) / 2)
        
        return {
            "mean_difference": mean_b - mean_a,
            "effect_size": effect_size,
            "confidence_interval": self.calculate_ci(scores_a, scores_b),
            "p_value": self.estimate_p_value(scores_a, scores_b)
        }

class CrossDomainValidator:
    """Validate prompt effectiveness across different domains"""
    
    def __init__(self):
        self.domains = ["web_design", "legal", "medical", "business"]
    
    def test_domain_transfer(self, base_prompt: str, source_domain: str, 
                           target_domains: List[str]) -> Dict[str, Any]:
        """Test how well prompts transfer between domains"""
        
        transfer_results = {}
        
        for target_domain in target_domains:
            # Adapt prompt to target domain
            adapted_prompt = self.adapt_prompt(base_prompt, source_domain, target_domain)
            
            # Test effectiveness
            effectiveness = self.evaluate_effectiveness(adapted_prompt, target_domain)
            
            transfer_results[target_domain] = {
                "adapted_prompt": adapted_prompt,
                "effectiveness_score": effectiveness,
                "transfer_success": effectiveness > 0.7  # Threshold
            }
        
        return transfer_results

class MetricsTracker:
    """Comprehensive performance metrics for prompt engineering"""
    
    def calculate_composite_score(self, metrics: Dict[str, float]) -> float:
        """Calculate overall prompt quality score"""
        weights = {
            "relevance": 0.3,
            "completeness": 0.25,
            "actionability": 0.25,
            "efficiency": 0.2
        }
        
        composite = 0
        for metric, weight in weights.items():
            composite += metrics.get(metric, 0) * weight
        
        return composite
