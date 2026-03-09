from pydantic import BaseModel

#Define a Question model (To be used with FastAPI)

class Question(BaseModel):
    question: str

# TODO: define Answer model and any other