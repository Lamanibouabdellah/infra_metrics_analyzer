import json
from mistralai.client import Mistral
from infra_metrics_analyzer.models.state import InfraState
from infra_metrics_analyzer.settings import settings

_client = Mistral(api_key=settings.mistral_api_key)

_SYSTEM_PROMPT = """
You are an infrastructure optimization expert.
Given insights and anomalies from a server metrics report, generate a list of actionable recommendations.
Respond exclusively with a valid JSON array matching this schema:
[
  {
    "id": "string",
    "action": "string",
    "target": "string",
    "parameters": {},
    "benefit_estimate": "string"
  }
]
""".strip()


def recommend(state: InfraState) -> dict:
    """Generate recommendations from insights and anomalies via LLM."""

    user_content = json.dumps({
        "insights":  state["insights"],
        "anomalies": state["anomalies"],
    })

    response = _client.chat.complete(
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": user_content},
        ],
    )

    payload = json.loads(response.choices[0].message.content)
    recommendations = payload if isinstance(payload, list) else payload.get("recommendations", [])

    return {"recommendations": recommendations}