from pydantic import BaseModel, HttpUrl


# Data required to add a website
class WebsiteCreate(BaseModel):
    name: str
    url: HttpUrl
    project_id: int


# Data returned by the API
class WebsiteResponse(BaseModel):
    id: int
    name: str
    url: str
    project_id: int

    model_config = {
        "from_attributes": True
    }