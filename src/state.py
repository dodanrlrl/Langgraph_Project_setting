# src/state.py
from langgraph.graph import MessagesState
from pydantic import BaseModel, Field

class JokeState(MessagesState):
  score : int
  feedback : str
  test : str
  answer : str