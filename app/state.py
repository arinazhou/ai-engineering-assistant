from typing import TypedDict
class AssistantState(TypedDict):
    repo_path: str
    mode: str
    question: str

    codebase: str
    testsprite_output: str
    failures: str
    answer: str