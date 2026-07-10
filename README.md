# infra_metrics_analyzer

Pipeline d'analyse de métriques d'infrastructure basé sur LangGraph et Mistral AI.

## Stack

- Python 3.11+
- LangGraph — orchestration du pipeline
- Mistral AI (`mistral-small-latest`) — génération de recommandations
- Pydantic v2 — validation des schémas
- Typer — CLI
- pytest — tests unitaires

## Installation

```bash
pip install -e .
pip install -r requirements.txt
cp .env.example .env
# renseigner MISTRAL_API_KEY dans .env
```

## Usage

```bash
# Lancer le pipeline complet
python -m infra_metrics_analyzer.app.cli run --input data/rapport.json --output data/output.json

# Afficher les étapes d'exécution
python -m infra_metrics_analyzer.app.cli run --verbose

# Valider le fichier d'entrée sans exécuter le pipeline
python -m infra_metrics_analyzer.app.cli validate --input data/rapport.json

# Afficher les seuils de détection actifs
python -m infra_metrics_analyzer.app.cli rules
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Structure

```
infra_metrics_analyzer/
├── src/
│   └── infra_metrics_analyzer/
│       ├── settings.py          # Configuration (LLM, chemins)
│       ├── app/
│       │   ├── graph.py         # Définition du pipeline LangGraph
│       │   └── cli.py           # Commandes CLI
│       ├── models/
│       │   ├── input.py         # Schéma de validation des snapshots entrants
│       │   ├── state.py         # État partagé entre les nœuds
│       │   └── output.py        # Schéma du rapport final
│       ├── nodes/
│       │   ├── ingest.py        # Chargement et validation du JSON
│       │   ├── analyse.py       # Agrégation des métriques
│       │   ├── detect.py        # Détection d'anomalies par seuils
│       │   ├── recommend.py     # Génération de recommandations via LLM
│       │   └── write.py         # Validation et écriture du rapport
│       └── rules/
│           └── thresholds.py    # Seuils de détection par métrique
│
├── tests/
│   ├── conftest.py              # Fixtures partagées
│   ├── test_models/
│   │   ├── test_input.py
│   │   └── test_output.py
│   └── test_nodes/
│       ├── test_analyse.py
│       ├── test_detect.py
│       └── test_write.py
│
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## Pipeline

```
ingest → analyse → detect → recommend → write
```

## Configuration

| Variable | Défaut | Description |
|---|---|---|
| `MISTRAL_API_KEY` | — | Clé API Mistral (obligatoire) |
| `LLM_MODEL` | `mistral-small-latest` | Modèle utilisé |
| `LLM_TEMPERATURE` | `0.2` | Température de génération |
| `LLM_MAX_TOKENS` | `1024` | Tokens max par appel |
| `INPUT_FILE` | `rapport.json` | Fichier de métriques en entrée |
| `OUTPUT_FILE` | `output.json` | Rapport généré en sortie |

## Étendre le projet

- **Nouvelle métrique surveillée** : ajouter un champ dans `models/input.py` et une entrée dans `rules/thresholds.py`
- **Nouveau nœud** : créer un fichier dans `nodes/` et l'enregistrer dans `app/graph.py`
- **Changer de LLM** : modifier `LLM_MODEL` dans `.env`