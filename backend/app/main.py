from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="NanoSkool Backend", version="0.1.0")

# CORS for local dev (vite on 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AssessmentItem(BaseModel):
    id: str
    prompt: str
    type: str  # mcq, short_answer
    options: Optional[List[str]] = None


class Submission(BaseModel):
    user_id: str
    item_id: str
    answer: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/assessment/items")
def get_items() -> List[AssessmentItem]:
    return [
        AssessmentItem(id="q1", prompt="What is 2+2?", type="mcq", options=["3", "4", "5"]).model_dump(),
        AssessmentItem(id="q2", prompt="List three uses for a paperclip.", type="short_answer").model_dump(),
    ]


@app.post("/assessment/submit")
def submit(submission: Submission):
    # Placeholder scoring logic
    score = 1.0 if (submission.item_id == "q1" and submission.answer.strip() == "4") else 0.5
    return {"ok": True, "score": score}


@app.get("/progress/{user_id}")
def progress(user_id: str):
    # Dummy progress card data
    radar = {
        "Communication": 0.7,
        "Creativity": 0.9,
        "Collaboration": 0.65,
        "Coding": 0.75,
        "Critical Thinking": 0.68,
        "Care": 0.8,
    }
    return {"user_id": user_id, "creativity_index": 0.82, "skills": radar}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
