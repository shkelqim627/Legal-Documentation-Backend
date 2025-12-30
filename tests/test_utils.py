import pytest
from src.utils import compute_mock_relevance, matches_query, extract_snippet


class TestComputeMockRelevance:
    
    def test_relevance_with_matching_terms(self):
        query = "contract agreement"
        content = "This document is about contract law and legal agreements between parties."
        
        score = compute_mock_relevance(query, content)
        
        assert isinstance(score, float)
        assert 0.0 <= score <= 1.0
        assert score > 0.0
    
    def test_relevance_with_no_matches(self):
        query = "xyzabc123"
        content = "This document is about contract law and legal agreements."
        
        score = compute_mock_relevance(query, content)
        
        assert score == 0.0
    
    def test_relevance_with_empty_query(self):
        query = ""
        content = "This is some content."
        
        score = compute_mock_relevance(query, content)
        
        assert score == 0.0
    
    def test_relevance_with_empty_content(self):
        query = "test query"
        content = ""
        
        score = compute_mock_relevance(query, content)
        
        assert score == 0.0
    
    def test_relevance_with_multiple_occurrences(self):
        query = "contract"
        content = "contract contract contract contract contract"
        
        score = compute_mock_relevance(query, content)
        
        assert score > 0.0
        assert score <= 1.0
    
    def test_relevance_case_insensitive(self):
        query = "CONTRACT"
        content = "This is about contract law."
        
        score1 = compute_mock_relevance(query, content)
        score2 = compute_mock_relevance(query.lower(), content)
        
        assert score1 == score2
        assert score1 > 0.0
    
    def test_relevance_with_partial_word_matches(self):
        query = "contract"
        content = "This document discusses contracting and contractual obligations."
        
        score = compute_mock_relevance(query, content)
        
        assert score > 0.0
    
    def test_relevance_score_range(self):
        query = "test"
        content = "test " * 100
        
        score = compute_mock_relevance(query, content)
        
        assert 0.0 <= score <= 1.0


class TestMatchesQuery:
    
    def test_matches_with_single_term(self):
        query = "contract"
        content = "This document is about contract law."
        
        assert matches_query(query, content) is True
    
    def test_matches_with_multiple_terms(self):
        query = "contract agreement"
        content = "This document is about contract law and legal agreements."
        
        assert matches_query(query, content) is True
    
    def test_no_match(self):
        query = "xyzabc123"
        content = "This document is about contract law."
        
        assert matches_query(query, content) is False
    
    def test_empty_query(self):
        query = ""
        content = "This is some content."
        
        assert matches_query(query, content) is False
    
    def test_empty_content(self):
        query = "test"
        content = ""
        
        assert matches_query(query, content) is False
    
    def test_case_insensitive_matching(self):
        query = "CONTRACT"
        content = "This is about contract law."
        
        assert matches_query(query, content) is True
    
    def test_partial_word_matching(self):
        query = "contract"
        content = "This discusses contracting and contractual obligations."
        
        assert matches_query(query, content) is True
    
    def test_multiple_query_terms_partial_match(self):
        query = "contract employment"
        content = "This document discusses contract law."
        
        assert matches_query(query, content) is True


class TestExtractSnippet:
    
    def test_snippet_extraction_with_match(self):
        content = "This is a long document about contract law and legal agreements between parties."
        query = "contract"
        
        snippet = extract_snippet(content, query)
        
        assert isinstance(snippet, str)
        assert len(snippet) > 0
        assert "contract" in snippet.lower()
    
    def test_snippet_with_context(self):
        content = "This is a long document. Here we discuss contract law in detail. More content follows."
        query = "contract"
        
        snippet = extract_snippet(content, query, context_chars=20)
        
        assert "contract" in snippet.lower()
        assert len(snippet) > len(query)
    
    def test_snippet_with_ellipsis(self):
        content = "This is a very long document with lots of content. " * 10
        content += "Here we discuss contract law. " * 10
        query = "contract"
        
        snippet = extract_snippet(content, query, max_length=100)
        
        assert len(snippet) <= 100 + len("...") * 2
    
    def test_snippet_with_no_match(self):
        content = "This is a document about employment law and workers' rights."
        query = "xyzabc123"
        
        snippet = extract_snippet(content, query)
        
        assert isinstance(snippet, str)
        assert len(snippet) > 0
    
    def test_snippet_max_length(self):
        content = "This is a very long document. " * 20
        query = "document"
        
        snippet = extract_snippet(content, query, max_length=50)
        
        assert len(snippet) <= 50 + len("...") * 2
    
    def test_snippet_empty_content(self):
        content = ""
        query = "test"
        
        snippet = extract_snippet(content, query)
        
        assert snippet == ""
    
    def test_snippet_empty_query(self):
        content = "This is some content about various topics."
        query = ""
        
        snippet = extract_snippet(content, query)
        
        assert isinstance(snippet, str)
        assert len(snippet) > 0
    
    def test_snippet_case_insensitive(self):
        content = "This document discusses CONTRACT law and legal agreements."
        query = "contract"
        
        snippet = extract_snippet(content, query)
        
        assert "contract" in snippet.lower() or "CONTRACT" in snippet
    
    def test_snippet_context_around_match(self):
        content = "Beginning of document. Here we discuss contract law in great detail. End of document."
        query = "contract"
        
        snippet = extract_snippet(content, query, context_chars=30)
        
        assert "contract" in snippet.lower()
        assert len(snippet) > 30
