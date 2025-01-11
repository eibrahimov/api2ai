FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
  curl \
  && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
COPY pyproject.toml .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY src/ai_agent_bridge /app/ai_agent_bridge

# Set environment variables
ENV PYTHONPATH=/app
ENV MODULE_NAME=ai_agent_bridge.src.main
ENV VARIABLE_NAME=app
ENV PORT=8003

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${PORT}/health || exit 1

# Run the application
CMD ["sh", "-c", "uvicorn ${MODULE_NAME}:${VARIABLE_NAME} --host 0.0.0.0 --port ${PORT} --reload"]