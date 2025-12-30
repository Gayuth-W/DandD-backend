from pydantic import BaseModel

class PlayStageRequest(BaseModel):
  user_id: int
  project_id: int
  stage: int
  user_response: str


class PlayStageResponse(BaseModel):
  task_text: str
  matched: bool
  score_awarded: int
  total_score: int
  next_stage: int