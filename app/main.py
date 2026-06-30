import typer
from dotenv import load_dotenv

load_dotenv()

from app.graph import build_graph

app = typer.Typer()


@app.command()
def ask(
    repo: str,
    question: str
):

    graph = build_graph()

    result = graph.invoke(
        {
            "repo_path": repo,
            "mode": "ask",
            "question": question,
            "codebase": "",
            "testsprite_output": "",
            "failures": "",
            "answer": ""
        }
    )

    print()
    print(result["answer"])
    print()


if __name__ == "__main__":
    app()