# src/nodes.py
from src.state import JokeState
from src.output_schema import StructuredJoke
from langchain.chat_models import init_chat_model

llm = init_chat_model('openai:gpt-4.1-mini')

def make_joke(state:JokeState):
  prompt = f'''입력된 주제를 바탕으로 농담을 생성해줘 피드백이 있다면 피드백을 반영하도록 해.
  입력된 주제: {state['messages'][-1]}
  피드백: {state['feedback']}
  '''
  result = llm.invoke(prompt)
  return{'messages': result}


def evaluate_joke(state:JokeState):
  structured_llm = llm.with_structured_output(StructuredJoke)

  prompt = f'''입력된 농담에 대해서 평가를 해서 점수와 피드백을 해줘
  입력된 농담 : {state['messages'][-1].content}

  출력되는 값은
  - score
  - feedback
  두가지야.

  '''
  result = structured_llm.invoke(prompt)
  return{'score': result.score, 'feedback': result.feedback, 'test' : result}




def make_answer(state:JokeState):
  result = f'''
농담 : {state['messages'][-1].content}
점수 : {state['score']}
피드백 : {state['feedback']}
테스트 : {state['test']}
'''
  return{'answer': result}
