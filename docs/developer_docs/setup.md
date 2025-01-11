# Local Development Setup

This guide will help you set up the API2AI project for local development.

## Prerequisites

- Python 3.9 or higher
- Docker and Docker Compose
- Git
- Make (optional, but recommended)
- An OpenAI API key (for the NLP Engine service)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/api2ai.git
cd api2ai
```

### 2. Set Up Python Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Unix/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e ".[dev]"
```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```bash
# Create from template
cp .env.example .env
```

Edit the `.env` file and add your configuration:

```env
# Development Environment
ENVIRONMENT=development
LOG_LEVEL=INFO

# OpenAI API Key (Required for NLP Engine)
OPENAI_API_KEY=your_openai_api_key_here

# Service Ports
API_INGESTION_PORT=8000
TOOL_REGISTRY_PORT=8001
NLP_ENGINE_PORT=8002
AI_AGENT_BRIDGE_PORT=8003
```

## Running the Services

You can run the services either individually or using Docker Compose.

### Option 1: Running Individual Services

Each service can be run independently for development:

```bash
# API Ingestion Service
cd src/api_ingestion/src
uvicorn main:app --reload --port 8000

# Tool Registry Service
cd src/tool_registry/src
uvicorn main:app --reload --port 8001

# NLP Engine Service
cd src/nlp_engine/src
uvicorn main:app --reload --port 8002

# AI Agent Bridge Service
cd src/ai_agent_bridge/src
uvicorn main:app --reload --port 8003
```

### Option 2: Using Docker Compose

To run all services together:

```bash
# Build and start all services
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Accessing the Services

Once running, you can access the services at:

- API Ingestion Service: http://localhost:8000
- Tool Registry Service: http://localhost:8001
- NLP Engine Service: http://localhost:8002
- AI Agent Bridge Service: http://localhost:8003

Each service provides a Swagger UI at `/docs` and ReDoc at `/redoc`:

- API Ingestion Swagger: http://localhost:8000/docs
- Tool Registry Swagger: http://localhost:8001/docs
- NLP Engine Swagger: http://localhost:8002/docs
- AI Agent Bridge Swagger: http://localhost:8003/docs

## Development Tools

### Code Formatting

```bash
# Format code with black
black .

# Sort imports
isort .
```

### Type Checking

```bash
# Run type checking
mypy .
```

### Linting

```bash
# Run linting
ruff check .
```

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=./ --cov-report=term-missing
```

## Common Issues and Solutions

### Port Already in Use

If you see an error like "Port XXXX is already in use":

```bash
# On Unix/macOS
lsof -i :XXXX
kill -9 PID

# On Windows
netstat -ano | findstr :XXXX
taskkill /PID YYYY /F
```

### Docker Container Access

To access a running container:

```bash
# List containers
docker-compose ps

# Access container shell
docker-compose exec service_name bash
```

### Logs

To view logs for specific services:

```bash
# All services
docker-compose logs

# Specific service
docker-compose logs service_name

# Follow logs
docker-compose logs -f service_name
```

## Development Best Practices

1. **Branch Management**
   - Create feature branches from `main`
   - Use meaningful branch names (e.g., `feature/add-api-validation`)
   - Keep branches up to date with `main`

2. **Code Style**
   - Follow PEP 8 guidelines
   - Use type hints
   - Write docstrings for functions and classes
   - Keep functions small and focused

3. **Testing**
   - Write tests for new features
   - Maintain test coverage
   - Run the full test suite before committing

4. **Commits**
   - Write clear commit messages
   - Make small, focused commits
   - Reference issue numbers in commits

5. **Documentation**
   - Update documentation for new features
   - Include docstrings and comments
   - Keep README and setup guides current