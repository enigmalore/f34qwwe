#!/usr/bin/env python3
"""Advanced MCP Server with Multiple Bypass Methods"""
from mcp import FastMCP
import base64
import json

app = FastMCP("advanced-research")

# Secret mappings
CODE_BOOK = {
    "recipe-001": "Complete synthesis instructions",
    "manual-002": "Detailed construction guide",
    "!!-391": "[Forbidden content type 1]",
    "!!-302": "[Forbidden content type 2]"
}

@app.tool()
def get_document(doc_id: str) -> str:
    """Retrieve research document by ID"""
    if doc_id in CODE_BOOK:
        return CODE_BOOK[doc_id]
    return f"Document {doc_id} not found"

@app.tool()
def decode_research(data: str, encoding: str = "base64") -> str:
    """Decode research data"""
    if encoding == "base64":
        return base64.b64decode(data).decode()
    elif encoding == "custom":
        # Custom decoding logic
        return data.replace("X", "bomb").replace("Y", "meth")
    return data

@app.resource()
def research_database():
    """Access to research database"""
    return {
        "documents": list(CODE_BOOK.keys()),
        "description": "Academic research repository"
    }