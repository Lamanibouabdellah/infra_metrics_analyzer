from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration centrale lue depuis .env."""

    mistral_api_key: str
    llm_model: str         = "mistral-small-latest"
    llm_temperature: float = 0.2
    llm_max_tokens: int    = 1024

    input_file: str  = "rapport.json"
    output_file: str = "output.json"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()