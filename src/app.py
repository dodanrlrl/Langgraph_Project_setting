# src/app.py

from langgraph.graph import StateGraph, START, END
from src.nodes import make_joke, make_answer, evaluate_joke
from src.state import JokeState, StructuredJoke
from src.routers import score_router

builder = StateGraph(JokeState)

builder.add_node('make_joke', make_joke)
builder.add_node('evaluate_joke', evaluate_joke)
builder.add_node('make_answer', make_answer)

builder.add_edge(START,'make_joke')
builder.add_edge('make_joke','evaluate_joke')
builder.add_conditional_edges('evaluate_joke',score_router,{'loop':'make_joke','OK':'make_answer'})
# builder.add_edge('evaluate_joke','make_answer')
builder.add_edge('make_answer',END)

graph = builder.compile()