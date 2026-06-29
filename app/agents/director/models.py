from pydantic import BaseModel


class MangaInput(BaseModel):
    filename: str
    page_url: str
    text_content: str = ""
