from pydantic import BaseModel


class SettingsSchema(BaseModel):
    PROJECT_ID: str = "0"
