from pydantic import BaseModel, Field

class StructuredJoke(BaseModel):
  score : int = Field(description='농담의 재미도에 대한 점수 0~100사이의 값으로')
  feedback : str = Field(description='농담에 대한 피드백')