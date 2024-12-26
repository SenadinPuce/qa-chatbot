from langgraph.graph import START, StateGraph
from utils.state import State
from workflow.actions import execute_query, generate_answer, write_query

graph_builder = StateGraph(State).add_sequence(
    [write_query, execute_query, generate_answer]
)
graph_builder.add_edge(START, "write_query")
graph = graph_builder.compile()
