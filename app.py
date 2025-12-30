from flask import Flask, request, jsonify
from flask_cors import CORS
from typing import Dict, List, Any, Tuple
import config
from src.documents import get_all_documents, get_document_by_id
from src.utils import compute_mock_relevance, matches_query, extract_snippet

app = Flask(__name__)

cors_origins = config.Config.get_cors_origins()
CORS(app, 
     origins=cors_origins,
     allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'OPTIONS'],
     supports_credentials=False,
     max_age=3600)


@app.route('/api/generate', methods=['POST', 'OPTIONS'])
def generate_search_results() -> Tuple[Dict[str, Any], int]:
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid request format"}), 400
        
        query = data.get('query', '')
        
        if not query or not isinstance(query, str):
            return jsonify({"error": "Query parameter is required and must be a non-empty string"}), 400
        
        query = query.strip()
        
        if not query:
            return jsonify({"error": "Query parameter cannot be empty"}), 400
        
        all_documents = get_all_documents()
        scored_documents: List[Dict[str, Any]] = []
        
        for doc in all_documents:
            if matches_query(query, doc['content']):
                relevance_score = compute_mock_relevance(query, doc['content'])
                snippet = extract_snippet(doc['content'], query)
                
                result_doc = {
                    "id": doc['id'],
                    "title": doc['title'],
                    "summary": doc['summary'],
                    "relevance_score": relevance_score,
                    "snippet": snippet
                }
                
                scored_documents.append(result_doc)
        
        scored_documents.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        return jsonify({
            "query": query,
            "results": scored_documents,
            "count": len(scored_documents)
        }), 200
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/documents/<document_id>', methods=['GET', 'OPTIONS'])
def get_document(document_id: str) -> Tuple[Dict[str, Any], int]:
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        document = get_document_by_id(document_id)
        
        if document is None:
            return jsonify({"error": f"Document with ID {document_id} not found"}), 404
        
        return jsonify(document), 200
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/health', methods=['GET', 'OPTIONS'])
def health_check() -> Tuple[Dict[str, str], int]:
    if request.method == 'OPTIONS':
        return '', 204
    
    return jsonify({"status": "ok"}), 200


@app.errorhandler(404)
def not_found(error) -> Tuple[Dict[str, str], int]:
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error) -> Tuple[Dict[str, str], int]:
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(error) -> Tuple[Dict[str, str], int]:
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(
        host=config.Config.HOST,
        port=config.Config.PORT,
        debug=config.Config.DEBUG
    )