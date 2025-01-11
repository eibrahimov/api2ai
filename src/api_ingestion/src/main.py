"""Main entry point for the API ingestion service."""

import logging
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="API Ingestion Service",
    description="Service for ingesting and parsing API specifications",
    version="0.1.0",
)

class APISpec(BaseModel):
    """API specification model."""
    url: HttpUrl
    name: str
    description: Optional[str] = None
    auth_type: Optional[str] = None
    headers: Optional[Dict[str, str]] = None

@app.post("/api/v1/ingest")
async def ingest_api(spec: APISpec) -> Dict[str, str]:
    """Ingest an API specification.

    Args:
        spec: The API specification to ingest.

    Returns:
        A dictionary containing the status of the ingestion.

    Raises:
        HTTPException: If the API specification cannot be ingested.
    """
    try:
        logger.info(f"Ingesting API: {spec.name} from {spec.url}")
        # TODO: Implement API ingestion logic
        return {"status": "success", "message": f"API {spec.name} ingested successfully"}
    except Exception as e:
        logger.error(f"Error ingesting API: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)