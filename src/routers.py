# src/routers.py
from src.state import JokeState

def score_router(state:JokeState):
    if state['score'] <= 70:
        return 'loop'
    else:
        return 'OK'
#추가과제) 2번 노드의 점수가 70점 아래면, 다시 1번 노드에서 농담을 생성하도록 함.(무한 루프 안빠지게 , 피드백 반영)