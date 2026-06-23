# Deployment Strategy

## Deployment Environment

The Guided MVP will be deployed as a cloud-hosted web application for student and admin access.

### Components Deployed
- FastAPI backend
- React / Streamlit frontend
- ChromaDB vector store
- Retrieval and guardrail pipeline
- Logging and analytics services

---

## Primary Deployment Strategy

Guided will use a Blue-Green deployment strategy.

### Why Blue-Green

The system includes critical guardrail behavior that must reliably prevent direct-answer responses. Blue-Green deployment allows the team to deploy updates safely while maintaining a stable fallback environment.

Benefits:
- Minimal downtime during deployment
- Safe rollback if guardrails or retrieval fail
- Reduced risk during live demos and evaluations
- Ability to validate system behavior before full traffic switch

---

## Deployment Flow

### Blue Environment
Current stable production environment.

### Green Environment
New deployment version used for testing and validation before traffic is redirected.

### Release Process
1. Deploy updated system to Green environment
2. Run health checks and smoke tests
3. Validate retrieval and guardrail behavior
4. Redirect traffic from Blue to Green
5. Keep Blue available as rollback target

---

## Risk Management

### Highest-Risk Failure

The highest-risk failure is guardrail failure resulting in direct-answer generation.

### Mitigation
- Input and output guardrails validated during deployment
- Smoke-test prompts used to verify guided responses
- Stable rollback environment always maintained

---

## Rollback Strategy

If deployment issues occur:
1. Redirect traffic back to the Blue environment
2. Verify stable service operation
3. Investigate deployment logs and failure points
4. Re-deploy only after validation testing passes

---

## MVP Tradeoffs

The MVP prioritizes:
- Stability
- Fast iteration
- Low operational complexity

Tradeoffs accepted:
- Limited scalability during MVP phase
- Manual deployment oversight
- Simplified monitoring compared to production-scale systems

Future phases may expand:
- automated scaling
- advanced monitoring
- container orchestration
- production-grade analytics infrastructure