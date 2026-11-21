from pydantic import BaseModel


# Data required to create a project
class ProjectCreate(BaseModel):
    name: str
    description: str | None = None


# Data returned by the API
class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    user_id: int

    model_config = {
        "from_attributes": True
    }