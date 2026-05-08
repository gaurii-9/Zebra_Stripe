from fastapi import FastAPI
import mlflow
from engine import ZebraEngine

app = FastAPI(title="zebra_stripe: Fact-Verification Gateway")
zebra = ZebraEngine()

# MLflow tracking
mlflow.set_tracking_uri("sqlite:///zebra_audit.db")

@app.post("/verify")
async def verify(query: str, context: str):
    with mlflow.start_run(run_name="Zebra_Inference"):
        result = zebra.process_query(query, context)
        
        # Log to MLflow for professional audit trail
        mlflow.log_metric("faithfulness_score", result["trust_score"])
        mlflow.log_param("engine", "zebra_stripe_v1")
        
        # Hallucination Guardrail
        if result["trust_score"] < 0.85:
            return {
                "verdict": "REJECTED",
                "reason": "High Hallucination Risk",
                "score": result["trust_score"]
            }
        
        return {
            "verdict": "VERIFIED",
            "score": result["trust_score"],
            "data": result["response"]
        }