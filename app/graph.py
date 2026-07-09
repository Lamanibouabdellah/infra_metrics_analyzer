from langgraph.graph import StateGraph, START, END
from models.state import InfraState
from nodes.ingest import ingest
from nodes.analyse import analyse
from nodes.detect import detect
from nodes.recommend import recommend
from nodes.write import write


def build_graph():
    graph = StateGraph(InfraState)

    graph.add_node("ingest",    ingest)
    graph.add_node("analyse",   analyse)
    graph.add_node("detect",    detect)
    graph.add_node("recommend", recommend)
    graph.add_node("write",     write)

    graph.add_edge(START,       "ingest")
    graph.add_edge("ingest",    "analyse")
    graph.add_edge("analyse",   "detect")
    graph.add_edge("detect",    "recommend")
    graph.add_edge("recommend", "write")
    graph.add_edge("write",     END)

    return graph.compile()