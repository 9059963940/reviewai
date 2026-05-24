from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from github_service import get_pr_files
from ai_reviewer import review_code

app = FastAPI()

# ✅ FIX: CORS SETUP
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/review")
def review(owner: str, repo: str, pr: int):

    files = get_pr_files(owner, repo, pr)

    if isinstance(files, dict) and "error" in files:
        return files

    files = files[:2]

    results = []

    for file in files:
        patch = file.get("patch")

        if patch:
            ai_review = review_code(patch)
            results.append({
                "file": file.get("filename"),
                "review": ai_review
            })

    return results