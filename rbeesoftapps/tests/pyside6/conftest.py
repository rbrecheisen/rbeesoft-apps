import importlib
import pytest


@pytest.fixture()
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test.sqlite3"
    monkeypatch.setenv("RBEESOFTAPPS_DB_URL", f"sqlite:///{db_path}")

    # Reload modules that contain singletons so they re-initialize with the test DB URL.
    # Adjust import paths to match your project layout exactly.
    import rbeesoftapps.pyside6.common.data.engine as engine_mod
    import rbeesoftapps.pyside6.common.data.session as session_mod
    import rbeesoftapps.pyside6.common.data.datamanager as dm_mod  # wherever DataManager lives

    importlib.reload(engine_mod)
    importlib.reload(session_mod)
    importlib.reload(dm_mod)

    yield db_path