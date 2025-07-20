from typing import TypedDict, List, Optional

class GraphState(TypedDict):
    image_path: str
    user_question: str
    image_caption: Optional[str]
    vision_tags: Optional[List[str]]
    external_facts: Optional[str]
    final_answer: Optional[str]