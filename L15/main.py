from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

wikipedia.set_lang("ru")

app = FastAPI()

class SummaryResponse(BaseModel):
    topic: str
    summary: str

class SearchResponse(BaseModel):
    query: str
    results: list[str]

class ExtractRequest(BaseModel):
    topic: str
    sentences: int

class ExtractResponse(BaseModel):
    topic: str
    content: str

@app.get("/summary/{topic}", response_model=SummaryResponse)
def get_summary_by_path(topic: str):
    text = wikipedia.summary(topic, sentences=2)
    return SummaryResponse(topic=topic, summary=text)

@app.get("/search", response_model=SearchResponse)
def search_articles(query: str):
    results = wikipedia.search(query)
    return SearchResponse(query=query, results=results)

@app.post("/extract", response_model=ExtractResponse)
def extract_text(req: ExtractRequest):
    text = wikipedia.summary(req.topic, sentences=req.sentences)
    return ExtractResponse(topic=req.topic, content=text)

# uvicorn main:app --reload

