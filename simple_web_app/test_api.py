from fastapi.testclient import TestClient

from .main import app

# given
client = TestClient(app)


def test_read_main_should_return_status_200():
    # when
    response = client.get("/")
    # then
    assert response.status_code == 200


def test_read_main_response():
    # when
    response = client.get("/")
    # then
    assert response.json() == {
        "description": "This is just a dummy response. Your API is up and running!"
    }


def test_password_validation_misspelled_key_should_return_status_422():
    # given
    misspelled_key_password_dict = {"contnt": ""}
    # when
    response = client.post("/", json=misspelled_key_password_dict)
    # then
    assert response.status_code == 422


def test_password_validation_empty_str_password_should_return_status_400():
    # given
    empty_password_dict = {"content": ""}
    # when
    response = client.post("/", json=empty_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400


def test_password_validation_8_chars_good_password_should_return_status_201():
    # given
    good_password_dict = {"content": "aB1@cD2#"}
    # when
    response = client.post("/", json=good_password_dict)
    # then
    print(response.content)
    assert response.status_code == 201

def test_password_validation_7_chars_password_should_return_status_400():
    # given
    sus_password_dict = {"content": "aB1@cD2"}
    # when
    response = client.post("/", json=sus_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400

def test_password_validation_9_chars_good_password_should_return_status_201():
    # given
    good_password_dict = {"content": "aB1@cD2#a"}
    # when
    response = client.post("/", json=good_password_dict)
    # then
    print(response.content)
    assert response.status_code == 201

def test_password_validation__8_chars_with_no_digit_password_should_return_status_400():
    # given
    sus_password_dict = {"content": "C@Abc@A"}
    # when
    response = client.post("/", json=sus_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400

def test_8_chars_with_no_lower_case_password_should_return_status_400():
    # given
    sus_password_dict = {"content": "C@ABc@A"}
    # when
    response = client.post("/", json=sus_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400

def test_8_chars_with_no_especial_character_password_should_return_status_400():
    # given
    sus_password_dict = {"content": "1eAB1eAB"}
    # when
    response = client.post("/", json=sus_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400

def test_8_chars_with_no_upper_case_password_should_return_status_400():
    # given
    sus_password_dict = {"content": "c@abc@a1"}
    # when
    response = client.post("/", json=sus_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400

def test_8_chars_with_invalid_char_password_should_return_status_400():
    # given
    sus_password_dict = {"content": "aB1acD2b~"}
    # when
    response = client.post("/", json=sus_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400