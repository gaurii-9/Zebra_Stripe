import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from langchain_community.llms import Ollama

class ZebraEngine:
    def __init__(self):
        # Local LLM: Gemma-2 (Sovereign AI)
        self.llm = Ollama(model="gemma2")
        
        # NLI Layer: Hallucination Detector (DeBERTa-v3 is gold standard)
        self.tokenizer = AutoTokenizer.from_pretrained("cross-encoder/nli-deberta-v3-large")
        self.model = AutoModelForSequenceClassification.from_pretrained("cross-encoder/nli-deberta-v3-large")

    def verify_grounding(self, context, answer):
        """Check if the answer is factually supported by the context."""
        inputs = self.tokenizer(answer, context, return_tensors="pt", truncation=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
            # Entailment score (higher = more truthful)
            probs = torch.softmax(logits, dim=-1)
            return probs[0][0].item()

    def process_query(self, query, context):
        # 1. Generate Response
        response = self.llm.invoke(f"Context: {context}\nQuestion: {query}\nAnswer based ONLY on context:")
        
        # 2. Verify Response (The 'Stripe' Check)
        trust_score = self.verify_grounding(context, response)
        
        return {"response": response, "trust_score": trust_score}
    