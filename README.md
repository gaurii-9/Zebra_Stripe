🦓 Zebra_Stripe: The Sovereign RAG & Verification Gateway
Zebra_Stripe is a clinical-grade, locally-hosted Retrieval-Augmented Generation (RAG) gateway. It doesn't just generate answers; it audits them. By utilizing a dual-model "Stripe" architecture, it ensures that every response is factually anchored in your private data, eliminating hallucinations at the source.

🛡️ The core philosophy: "Audit via Entailment"

In a production AI environment, "plausibility" is the enemy of "truth." Zebra_Stripe enforces a Fact-First Mandate by separating the Creator (LLM) from the Auditor (NLI). It treats every AI response as a hypothesis that must be proved against a retrieved context before it is ever rendered to the user.

🏗️ Technical Architecture (The Deep-Tech Stack)

This system is engineered for sovereignty and hardware acceleration, optimized specifically for Apple Silicon via the PyTorch MPS (Metal Performance Shaders) backend.

The Brain (SLM): Gemma-2 via Ollama, serving as the high-reasoning local generator.

The Memory (Vector DB): ChromaDB for high-dimensional semantic indexing and retrieval.

The Auditor (NLI): DeBERTa-v3-Large running on PyTorch, specifically tuned for MNLI to calculate logical entailment.

The Ledger (MLOps): MLflow integration for persistent audit trails and faithfulness tracking.

🚦 Visualizing the Workflow

Execution & Evidence

ite_start]**Factual Alignment Audit: Successful hallucination detection confirmed via NLI entailment scoring.:** 
   (.assets/01_Verification_Gateway.jpg.png)

   
  


MacBook with Apple Silicon (M1/M2/M3).

Ollama (with gemma2 pulled).

Python 3.12+.

Execution Sequence:

Ignite the Brain: ollama run gemma2

Start the Auditor: mlflow ui --backend-store-uri sqlite:///zebra_audit.db

Launch the Gateway: uvicorn app:app --reload

📊 Performance & Governance

Zebra_Stripe isn't just a project; it's a statement on AI Ethics. By keeping the entire stack local (ChromaDB + PyTorch + Gemma), we ensure that sensitive data never leaves the machine, while the MLflow integration provides the "receipts" needed for enterprise-grade AI auditing.

⚖️ Copyright & Originality

The architectural logic, the "Stripe" verification protocol, and the integration of NLI with RAG pipelines are original constructs. This project avoids generic AI prose, focusing instead on human-centric engineering and rhythmic technical flow.

Engineered with precision by Gauri.
