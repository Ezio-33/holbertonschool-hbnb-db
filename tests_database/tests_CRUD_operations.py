import pytest
from manage import DataManager
from src.models.user import User


def test_save_user_to_db(test_client, init_db):
    data_manager = DataManager()
    user = User(email="dbtest@example.com",
                password="password",
                first_name="Test", last_name="User")

    with test_client.application.app_context():
        data_manager.save_user(user)

    saved_user = User.query.filter_by(email="dbtest@example.com").first()
    assert saved_user is not None
    assert saved_user.email == "dbtest@example.com"

def test_save_user_to_file(file_repo, mocker):
    data_manager = DataManager()
    user = User(id="file_user1",
                email="filetest@example.com",
                password="password",
                first_name="File",
                last_name="User")

    mocker.patch("src.manage.app.config", {"USE_DATABASE": False})
    mocker.patch("src.persistence.FileRepository", return_value=file_repo)

    data_manager.save_user(user)

    saved_user = file_repo.get("user", "file_user1")
    assert saved_user is not None
    assert saved_user.email == "filetest@example.com"
