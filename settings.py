# ============================================================
# settings.py
# Configuration centrale de l'application.
# Lue depuis les variables d'environnement (fichier .env).
# Importée comme singleton : from settings import settings
# ============================================================

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Toute la configuration technique en un seul endroit.
    Pydantic Settings valide les types au démarrage de l'app
    et lève une erreur explicite si une variable obligatoire manque.
    """

    # ── LLM ──────────────────────────────────────────────────
    openai_api_key: str
    llm_model: str       = "gpt-4o"
    llm_temperature: float = 0.2
    llm_max_tokens: int  = 1024

    # ── Chemins fichiers ──────────────────────────────────────
    input_file: str  = "rapport.json"
    output_file: str = "output.json"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Singleton — importé partout avec : from settings import settings
settings = Settings()