from langgraph.graph import StateGraph, START, END
from infra_metrics_analyzer.models.state import InfraState
from infra_metrics_analyzer.nodes.ingest import ingest
from infra_metrics_analyzer.nodes.analyse import analyse
from infra_metrics_analyzer.nodes.detect import detect
from infra_metrics_analyzer.nodes.recommend import recommend
from infra_metrics_analyzer.nodes.write import write


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