# Legal Document Search Portal - Backend API

A production-ready Flask REST API backend for searching and retrieving legal documents. The API provides intelligent document search with relevance scoring, snippet extraction, and comprehensive error handling.

## Project Description

This Flask backend serves as the API layer for a Legal Document Search Portal, providing endpoints to search through 10 comprehensive legal documents covering various areas of law including contract law, employment rights, intellectual property, corporate governance, real estate, family law, tax compliance, data privacy, litigation, and business formation.

## Architecture Overview

The application follows a clean, modular architecture:

- **app.py**: Main Flask application with route handlers and error handling
- **config.py**: Configuration management with environment variable loading
- **src/documents.py**: In-memory document storage (10 legal documents)
- **src/utils.py**: Utility functions for relevance scoring and snippet extraction
- **tests/**: Comprehensive test suite with pytest

The backend uses in-memory document storage (no database required) and implements intelligent search algorithms for relevance scoring and snippet extraction.

## Setup Instructions

### Local Development Setup

#### 1. Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment support

#### 2. Clone and Navigate

```bash
cd backend
```

#### 3. Create Virtual Environment

```bash
python -m venv venv
```

#### 4. Activate Virtual Environment

**On Unix/macOS:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

#### 5. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 6. Create .env File

Create a `.env` file in the project root:

```env
PORT=3001
FRONTEND_URL=http://localhost:3000
DEBUG=True
FLASK_ENV=development
```

You can copy from the `.env.example` template:

```bash
cp .env.example .env
```

#### 7. Run the Application

**Option 1: Using the run script**
```bash
./run.sh
```

**Option 2: Direct Python execution**
```bash
python app.py
```

The server will start on `http://localhost:3001` (or the port specified in your `.env` file).

### Docker Setup

#### Build and Run with Docker

```bash
docker build -t legal-docs-backend .
docker run -p 3001:3001 --env-file .env legal-docs-backend
```

#### Using Docker Compose

```bash
docker-compose up --build
```

This will start the backend service on port 3001.

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Tests with Coverage

```bash
pytest --cov=src --cov=app --cov-report=html
```

### Run Specific Test Files

```bash
pytest tests/test_api.py
pytest tests/test_utils.py
```

### Run Specific Test Classes or Functions

```bash
pytest tests/test_api.py::TestGenerateEndpoint
pytest tests/test_api.py::TestGenerateEndpoint::test_generate_with_valid_query
```

## API Documentation

### Base URL

```
http://localhost:3001
```

### Endpoints

#### 1. Search Documents

**POST** `/api/generate`

Search documents by query and return scored results with snippets, sorted by relevance.

**Request Body:**
```json
{
  "query": "contract law"
}
```

**Success Response (200 OK):**
```json
{
  "query": "contract law",
  "results": [
    {
      "id": "doc1",
      "title": "Contract Law Fundamentals",
      "summary": "Contract law fundamentals cover offer, acceptance, consideration...",
      "relevance_score": 0.856,
      "snippet": "...document about contract law and legal agreements between parties..."
    }
  ],
  "count": 1
}
```

**Error Response (400 Bad Request) - Empty Query:**
```json
{
  "error": "Query parameter is required and cannot be empty"
}
```

**Error Response (400 Bad Request) - Invalid Query Type:**
```json
{
  "error": "Query parameter is required and must be a non-empty string"
}
```

**Error Response (400 Bad Request) - Missing Request Body:**
```json
{
  "error": "Request body is required"
}
```

**Example Request (cURL):**
```bash
curl -X POST http://localhost:3001/api/generate \
  -H "Content-Type: application/json" \
  -d '{"query": "employment rights"}'
```

**Example Request (Python):**
```python
import requests

response = requests.post(
    'http://localhost:3001/api/generate',
    json={'query': 'employment rights'}
)
data = response.json()
print(data)
```

**Example Request (JavaScript):**
```javascript
fetch('http://localhost:3001/api/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ query: 'intellectual property' })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

#### 2. Get Document by ID

**GET** `/api/documents/<id>`

Retrieve a specific document by its ID.

**Path Parameters:**
- `id` (string): Document ID (doc1, doc2, doc3, ..., doc10)

**Success Response (200 OK):**
```json
{
  "id": "doc1",
  "title": "Contract Law Fundamentals",
  "content": "Contract law forms the foundation of commercial and personal agreements...",
  "summary": "Contract law fundamentals cover offer, acceptance, consideration...",
  "relevance_score": 0.92
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Document with ID doc999 not found"
}
```

**Example Request (cURL):**
```bash
curl http://localhost:3001/api/documents/doc1
```

**Example Request (Python):**
```python
import requests

response = requests.get('http://localhost:3001/api/documents/doc1')
document = response.json()
print(document['title'])
```

#### 3. Health Check

**GET** `/api/health`

Check if the API is running and healthy.

**Success Response (200 OK):**
```json
{
  "status": "ok"
}
```

**Example Request (cURL):**
```bash
curl http://localhost:3001/api/health
```

### Available Documents

The API includes 10 pre-loaded legal documents:

1. **doc1** - Contract Law Fundamentals
2. **doc2** - Employment Rights Guide
3. **doc3** - Intellectual Property Overview
4. **doc4** - Corporate Governance Handbook
5. **doc5** - Real Estate Law Guide
6. **doc6** - Family Law Essentials
7. **doc7** - Tax Law Compliance
8. **doc8** - Data Privacy & GDPR
9. **doc9** - Litigation & Dispute Resolution
10. **doc10** - Business Formation Guide

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PORT` | Port number for the Flask server | `3001` | No |
| `FRONTEND_URL` | Frontend URL for CORS configuration | `http://localhost:3000` | No |
| `HOST` | Host address for the Flask server | `0.0.0.0` | No |
| `DEBUG` | Enable Flask debug mode | `True` | No |
| `FLASK_ENV` | Flask environment (development/production) | `development` | No |

## How It Works

### Relevance Scoring

The relevance score is calculated based on:
- Frequency of query terms in the document content
- Number of unique query terms matched
- Logarithmic scaling for better score distribution

Scores range from `0.0` (no match) to `1.0` (perfect match). Results are automatically sorted by relevance score in descending order.

### Snippet Extraction

Snippets are extracted by:
1. Finding the first occurrence of any query term in the document
2. Including context characters before and after the match (default: 50 characters)
3. Truncating to maximum length if needed (default: 200 characters)
4. Adding ellipsis (`...`) when content is truncated

### Document Storage

All documents are stored in-memory in `src/documents.py`. No database is required. Each document includes:
- `id`: Unique string identifier (doc1-doc10)
- `title`: Document title
- `content`: Full document text (200+ words)
- `summary`: Brief 1-2 sentence summary
- `relevance_score`: Pre-set relevance score (0.85-0.99) for testing

## Code Structure

```
backend/
├── app.py                 # Main Flask application
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── Dockerfile            # Docker container definition
├── docker-compose.yml    # Docker Compose configuration
├── run.sh                # Local development startup script
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── src/
│   ├── __init__.py
│   ├── documents.py      # In-memory document storage
│   └── utils.py          # Utility functions
└── tests/
    ├── __init__.py
    ├── test_api.py       # API endpoint tests
    └── test_utils.py     # Utility function tests
```

## Dependencies

- **flask** (3.0.0): Web framework
- **flask-cors** (4.0.0): Cross-Origin Resource Sharing support
- **python-dotenv** (1.0.0): Environment variable management
- **pytest** (7.4.3): Testing framework
- **pytest-cov** (4.1.0): Coverage reporting
- **gunicorn** (21.2.0): Production WSGI server
- **requests** (2.31.0): HTTP library for testing

## Error Handling

The API implements comprehensive error handling:

- **400 Bad Request**: Invalid or empty query, malformed JSON, invalid request format
- **404 Not Found**: Document ID not found, undefined routes
- **405 Method Not Allowed**: Incorrect HTTP method for endpoint
- **500 Internal Server Error**: Unexpected server errors

All error responses follow this format:
```json
{
  "error": "Error message description"
}
```

## CORS Configuration

CORS is configured to allow requests from the frontend. The allowed origin is configured via the `FRONTEND_URL` environment variable (default: `http://localhost:3000`).

## Production Deployment

### Using Gunicorn

The Dockerfile uses Gunicorn for production deployment:

```bash
gunicorn --bind 0.0.0.0:3001 --workers 4 --timeout 120 app:app
```

### Environment Variables for Production

Set these in your production environment:

```env
PORT=3001
FRONTEND_URL=https://your-frontend-domain.com
DEBUG=False
FLASK_ENV=production
```

### Health Checks

The Dockerfile includes a health check that pings `/api/health` every 30 seconds.

## Troubleshooting

### Port Already in Use

If port 3001 is already in use:

1. Change the `PORT` in your `.env` file
2. Or find and kill the process:
   ```bash
   # On Unix/macOS
   lsof -ti:3001 | xargs kill
   
   # On Windows
   netstat -ano | findstr :3001
   taskkill /PID <PID> /F
   ```

### Import Errors

If you encounter import errors:

1. Ensure virtual environment is activated
2. Verify dependencies are installed: `pip install -r requirements.txt`
3. Check you're running commands from the project root directory

### CORS Issues

If experiencing CORS errors:

1. Verify `FRONTEND_URL` in `.env` matches your frontend URL exactly
2. Restart the Flask server after changing `.env`
3. Check browser console for specific CORS error messages

### Test Failures

If tests fail:

1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Run tests with verbose output: `pytest -v`
3. Check that the Flask app is not running on the test port
4. Verify `.env` file exists and is properly configured

### Docker Issues

If Docker build fails:

1. Ensure Docker is running
2. Check Dockerfile syntax
3. Verify all files are in the correct location
4. Try rebuilding without cache: `docker build --no-cache -t legal-docs-backend .`

## Testing

The test suite includes:

- **API Endpoint Tests**: All endpoints with various scenarios
- **Error Handling Tests**: 400, 404, 405, 500 error responses
- **Utility Function Tests**: Relevance scoring, query matching, snippet extraction
- **Edge Case Tests**: Empty queries, invalid inputs, missing parameters

Run the full test suite to ensure everything works correctly before deployment.

## License

This project is provided as-is for educational and development purposes.
