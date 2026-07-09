from typing_extensions import TypedDict
from typing import Literal
from langgraph.graph import StateGraph, START, END
import random

# ----------------------------
# State
# ----------------------------
class State(TypedDict):
    graph_info: str


# ----------------------------
# Nodes
# ----------------------------
def start_play(state: State):
    print("Start Play node called")
    return {
        "graph_info": state["graph_info"] + " I am planning to play"
    }


def cricket(state: State):
    print("Cricket node called")
    return {
        "graph_info": state["graph_info"] + " Cricket"
    }


def badminton(state: State):
    print("Badminton node called")
    return {
        "graph_info": state["graph_info"] + " Badminton"
    }


# ----------------------------
# Router
# ----------------------------
def random_play(state: State) -> Literal["cricket", "badminton"]:
    if random.random() > 0.5:
        return "cricket"
    return "badminton"


# ----------------------------
# Build Graph
# ----------------------------
graph = StateGraph(State)

graph.add_node("start_play", start_play)
graph.add_node("cricket", cricket)
graph.add_node("badminton", badminton)

graph.add_edge(START, "start_play")
graph.add_conditional_edges("start_play", random_play)
graph.add_edge("cricket", END)
graph.add_edge("badminton", END)

builder = graph.compile()
