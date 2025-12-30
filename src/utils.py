from typing import Dict, List, Tuple
import math


def compute_mock_relevance(query: str, document_content: str) -> float:
    if not query or not document_content:
        return 0.0
    
    query_lower = query.lower()
    doc_lower = document_content.lower()
    query_terms = query_lower.split()
    
    if not query_terms:
        return 0.0
    
    total_matches = 0
    for term in query_terms:
        count = doc_lower.count(term)
        total_matches += count
    
    if total_matches == 0:
        return 0.0
    
    base_score = min(total_matches / (len(query_terms) * 10), 1.0)
    relevance_score = min(1.0, math.log(1 + base_score * 10) / math.log(11))
    
    return round(relevance_score, 3)


def matches_query(query: str, document_content: str) -> bool:
    if not query or not document_content:
        return False
    
    query_lower = query.lower()
    doc_lower = document_content.lower()
    query_terms = query_lower.split()
    
    for term in query_terms:
        if term in doc_lower:
            return True
    
    return False


def extract_snippet(content: str, query: str, max_length: int = 200, context_chars: int = 50) -> str:
    if not content or not query:
        return content[:max_length] if content else ""
    
    query_lower = query.lower()
    content_lower = content.lower()
    query_terms = query_lower.split()
    
    best_position = -1
    for term in query_terms:
        pos = content_lower.find(term)
        if pos != -1:
            best_position = pos
            break
    
    if best_position == -1:
        snippet = content[:max_length]
        if len(content) > max_length:
            snippet += "..."
        return snippet
    
    start = max(0, best_position - context_chars)
    end = min(len(content), best_position + len(query_terms[0]) + context_chars)
    
    snippet = content[start:end]
    
    if start > 0:
        snippet = "..." + snippet
    
    if end < len(content):
        snippet = snippet + "..."
    
    if len(snippet) > max_length:
        match_in_snippet = best_position - start
        ideal_start = max(0, match_in_snippet - max_length // 2)
        ideal_end = min(len(snippet), ideal_start + max_length)
        snippet = snippet[ideal_start:ideal_end]
        
        if ideal_start > 0:
            snippet = "..." + snippet
        if ideal_end < len(content):
            snippet = snippet + "..."
    
    return snippet
