"""PyTest Config File."""

import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def change_cwd():
    os.chdir(f"{os.getcwd()}/molecule/default")
