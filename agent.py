from pyouter.app import App
from pyouter.router import Router
from agent.comment import CommentAgent
from pyeff.shell import run_cmds
from pyeff.fs import current_dir

if __name__ == "__main__":
    """
    pip install -r requirements-dev.txt
    python agent.comment --token=...
    python agent.test
    python agent.publish

    TODO: chain agent.comment and agent.test
    """

    dir = current_dir(__file__)

    config = {}

    app = App(config=config)

    app.option("--token", dest="token", nargs="?", type=str, help="debug")

    app.use(
        router=Router(
            agent=Router(
                comment=CommentAgent(),
                test=lambda config, options: run_cmds(
                    [f"pip install {dir}", "cd src/tests && python test.py"]
                ),
                publish=lambda config, options: run_cmds(
                    [
                        "python setup.py bdist_wheel --universal",
                        "twine upload dist/* --verbos",
                    ]
                ),
            )
        )
    )

    app.run()
