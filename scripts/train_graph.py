"""Builds and exports the ISO/IEC cross-reference dependency graph."""
from knowledge_base.graph_builder import StandardGraphBuilder

def generate_standard_graph():
    builder = StandardGraphBuilder()
    
    # Add nodes
    builder.add_standard("27001", "Information Security Management", "Security")
    builder.add_standard("27002", "Information Security Controls", "Security")
    builder.add_standard("42001", "Artificial Intelligence Management", "AI")
    builder.add_standard("22989", "AI Concepts and Terminology", "AI")
    
    # Add relationships
    builder.add_reference("27002", "27001", "SUPPORTS")
    builder.add_reference("22989", "42001", "PREREQUISITE")
    
    builder.export_graph("knowledge_base/standard_graph.json")
    print("Standard cross-reference graph successfully exported.")

if __name__ == "__main__":
    generate_standard_graph()
