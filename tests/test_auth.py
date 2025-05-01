from services.auth_service import signup, login

def test_signup_login_flow(tmp_path):
    # ejemplo mínimo: creás un usuario, hacés login y comprobás que devuelve True
    assert signup("user", "pass") is True
    assert login("user", "pass") is True
