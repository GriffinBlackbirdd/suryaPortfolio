from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

# Initialize FastAPI app
app = FastAPI(title="Upendra Surya Portfolio")

# Get the current directory
BASE_DIR = Path(__file__).resolve().parent

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory=str(BASE_DIR)), name="static")

# Define templates directory (not using templates in this case, but could be added later)
templates = Jinja2Templates(directory=str(BASE_DIR))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serve the index.html file as the root endpoint
    """
    try:
        # Read the index.html file
        html_file_path = os.path.join(BASE_DIR, "index.html")
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading index.html: {str(e)}")

@app.get("/health", status_code=200)
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}

# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)