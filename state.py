from typing import TypedDict, List, Optional

class GraphSharedState(TypedDict): #Use a Typed dictionary to enforce type checking 
    image_path: str #This syntax declares a key named "image_caption" (so a string) whose value is str i.e string is expected in the dict.
    user_question: str
    image_caption: Optional[str]
    parsed_question: Optional[str]
    vision_tags: Optional[List[str]]
    external_facts: Optional[str]
    final_answer: Optional[str]