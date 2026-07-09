# infra_metrics_analyzer

Pipeline d'analyse de métriques d'infrastructure basé sur LangGraph et GPT-4o.

## Stack

- Python 3.11+
- LangGraph — orchestration du pipeline
- OpenAI GPT-4o — génération de recommandations
- Pydantic v2 — validation des schémas
- Typer — CLI

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env
# renseigner OPENAI_API_KEY dans .env
```

## Usage

```bash
# Lancer le pipeline complet
python -m app.cli run

# Avec chemins personnalisés
python -m app.cli run --input rapport.json --output output.json

# Afficher les étapes d'exécution
python -m app.cli run --verbose

# Valider le fichier d'entrée sans exécuter le pipeline
python -m app.cli validate --input rapport.json

# Afficher les seuils de détection actifs
python -m app.cli rules
```

## Structure

```
infra_metrics_analyzer/
├── settings.py          # Configuration (LLM, chemins)
├── app/
│   ├── graph.py         # Définition du pipeline LangGraph
│   └── cli.py           # Commandes CLI
├── models/
│   ├── input.py         # Schéma de validation des snapshots entrants
│   ├── state.py         # État partagé entre les nœuds
│   └── output.py        # Schéma du rapport final
├── nodes/
│   ├── ingest.py        # Chargement et validation du JSON
│   ├── analyse.py       # Agrégation des métriques
│   ├── detect.py        # Détection d'anomalies par seuils
│   ├── recommend.py     # Génération de recommandations via LLM
│   └── write.py         # Validation et écriture du rapport
└── rules/
    └── thresholds.py    # Seuils de détection par métrique
```

## Pipeline

```
ingest → analyse → detect → recommend → write
```

## Configuration

| Variable | Défaut | Description |
|---|---|---|
| `OPENAI_API_KEY` | — | Clé API OpenAI (obligatoire) |
| `LLM_MODEL` | `gpt-4o` | Modèle utilisé |
| `LLM_TEMPERATURE` | `0.2` | Température de génération |
| `LLM_MAX_TOKENS` | `1024` | Tokens max par appel |
| `INPUT_FILE` | `rapport.json` | Fichier de métriques en entrée |
| `OUTPUT_FILE` | `output.json` | Rapport généré en sortie |

## Étendre le projet

- **Nouvelle métrique surveillée** : ajouter un champ dans `models/input.py` et une entrée dans `rules/thresholds.py`
- **Nouveau nœud** : créer un fichier dans `nodes/` et l'enregistrer dans `app/graph.py`
- **Changer de LLM** : modifier `LLM_MODEL` dans `.env`