from langchain_openai import ChatOpenAI

from app.prompts import SYSTEM_PROMPT
from app.code_reader import read_codebase


def get_llm():
    return ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

def load_codebase(state):

    codebase = read_codebase(
        state["repo_path"]
    )

    return {
        "codebase": codebase
    }
    
# def analyze_code(state):

#     llm = get_llm()

#     prompt = f"""
# Question:
# {state["question"]}

# Codebase:
# {state["codebase"]}
# """

#     response = llm.invoke(
#         [
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return {
#         "answer": response.content
#     }

def analyze_code(state):

    return {
        "answer":
        f"""
Repository loaded successfully.

Question:
{state['question']}

Characters read:
{len(state['codebase'])}

(OpenAI disabled because API quota has not been configured.)
        """
    }