import pytest
import json
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestGenerateEndpoint:
    
    def test_generate_with_valid_query(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'contract'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert 'query' in data
        assert 'results' in data
        assert 'count' in data
        assert data['query'] == 'contract'
        assert isinstance(data['results'], list)
        assert data['count'] > 0
        
        if data['results']:
            result = data['results'][0]
            assert 'id' in result
            assert 'title' in result
            assert 'summary' in result
            assert 'relevance_score' in result
            assert 'snippet' in result
            assert isinstance(result['relevance_score'], (int, float))
            assert result['relevance_score'] >= 0.0
    
    def test_generate_with_empty_query(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': ''}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert 'empty' in data['error'].lower() or 'required' in data['error'].lower()
    
    def test_generate_with_missing_query(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_generate_with_no_request_body(self, client):
        response = client.post(
            '/api/generate',
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_generate_with_invalid_query_type(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 123}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_generate_with_null_query(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': None}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_generate_with_matching_query(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'employment rights'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['count'] > 0
        if len(data['results']) > 1:
            scores = [r['relevance_score'] for r in data['results']]
            assert scores == sorted(scores, reverse=True)
    
    def test_generate_with_no_matches(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'xyzabc123nonexistent'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert data['count'] == 0
        assert data['results'] == []
    
    def test_generate_relevance_score_calculation(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'intellectual property'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        for result in data['results']:
            assert 0.0 <= result['relevance_score'] <= 1.0
    
    def test_generate_snippet_extraction(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'patent'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        for result in data['results']:
            assert 'snippet' in result
            assert isinstance(result['snippet'], str)
            assert len(result['snippet']) > 0
    
    def test_generate_results_sorted_by_relevance(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'law'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        if len(data['results']) > 1:
            scores = [r['relevance_score'] for r in data['results']]
            assert scores == sorted(scores, reverse=True)
    
    def test_generate_cors_headers(self, client):
        response = client.post(
            '/api/generate',
            data=json.dumps({'query': 'contract'}),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        assert 'Access-Control-Allow-Origin' in response.headers or 'access-control-allow-origin' in str(response.headers).lower()


class TestDocumentsEndpoint:
    
    def test_get_document_with_valid_id(self, client):
        response = client.get('/api/documents/doc1')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert 'id' in data
        assert 'title' in data
        assert 'content' in data
        assert 'summary' in data
        assert 'relevance_score' in data
        assert data['id'] == 'doc1'
        assert data['title'] == 'Contract Law Fundamentals'
    
    def test_get_document_with_invalid_id(self, client):
        response = client.get('/api/documents/doc999')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert 'not found' in data['error'].lower()
    
    def test_get_all_valid_documents(self, client):
        valid_ids = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5', 'doc6', 'doc7', 'doc8', 'doc9', 'doc10']
        for doc_id in valid_ids:
            response = client.get(f'/api/documents/{doc_id}')
            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['id'] == doc_id
    
    def test_get_document_structure(self, client):
        response = client.get('/api/documents/doc1')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        
        assert isinstance(data['id'], str)
        assert isinstance(data['title'], str)
        assert isinstance(data['content'], str)
        assert isinstance(data['summary'], str)
        assert isinstance(data['relevance_score'], (int, float))
        assert len(data['content']) > 200


class TestHealthEndpoint:
    
    def test_health_check(self, client):
        response = client.get('/api/health')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'status' in data
        assert data['status'] == 'ok'
    
    def test_health_check_methods(self, client):
        response = client.get('/api/health')
        assert response.status_code == 200
        
        response = client.post('/api/health')
        assert response.status_code == 405


class TestErrorHandling:
    
    def test_404_for_undefined_route(self, client):
        response = client.get('/api/nonexistent')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_405_method_not_allowed(self, client):
        response = client.post('/api/documents/doc1')
        assert response.status_code == 405 or response.status_code == 200
        
        response = client.put('/api/generate')
        assert response.status_code == 405
    
    def test_500_error_handling(self, client):
        response = client.post(
            '/api/generate',
            data='invalid json',
            content_type='application/json'
        )
        
        assert response.status_code in [400, 500]
