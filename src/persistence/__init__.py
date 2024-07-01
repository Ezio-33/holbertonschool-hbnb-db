""" This module is responsible for selecting the repository
to be used based on the environment variable REPOSITORY_ENV_VAR."""

import os

from src.persistence.repository import Repository

repo: Repository

if os.getenv(key="MY_ENV_VAR") == "db":
    from src.persistence.db import DBRepository

    repo = DBRepository()
elif os.getenv("MY_ENV_VAR") == "file":
    from src.persistence.file import FileRepository

    repo = FileRepository()
elif os.getenv("MY_ENV_VAR") == "pickle":
    from src.persistence.pickled import PickleRepository

    repo = PickleRepository()
else:
    from src.persistence.memory import MemoryRepository

    repo = MemoryRepository()

print(f"Using {repo.__class__.__name__} as repository")
