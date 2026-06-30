from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.state import AssistantState
from app.nodes import (
    load_codebase,
    analyze_code
)

def build_graph():

    builder = StateGraph(
        AssistantState
    )

    builder.add_node(
        "load_codebase",
        load_codebase
    )

    builder.add_node(
        "analyze_code",
        analyze_code
    )

    builder.add_edge(
        START,
        "load_codebase"
    )

    builder.add_edge(
        "load_codebase",
        "analyze_code"
    )

    builder.add_edge(
        "analyze_code",
        END
    )

    return builder.compile()