from pydantic_settings import BaseSettings, SettingsConfigDict


class Setings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", # Can be replaced with an invalid path/string
    )
    TG_TOKEN: str


    @property
    def tg_token(self):
        return f"{self.TG_TOKEN}"


    

setings = Setings()