import pytest
from api_yandex import create_folder


class TestYandexApi:

    token_yandex = ' ' #указать Яндекс токен

    def setup(self):
        print('setup')

    # 201 - папка успешно создана, 409 - Ресурс (папка с таким именем) уже существует
    @pytest.mark.parametrize(('token_yandex', 'folder_name', 'result'), [(token_yandex, 'new_folder', 201), (token_yandex, 'new_folder', 409)])
    def test_api_yandex_folder_name(self, token_yandex, folder_name, result):
        assert create_folder(token_yandex, folder_name) == result

    # 401 - Не авторизован (неверный токен)
    @pytest.mark.parametrize(('token_yandex', 'folder_name', 'result'), [('faketoken', 'new_folder_1', 401)])
    def test_api_yandex_token(self, token_yandex, folder_name, result):
        assert create_folder(token_yandex, folder_name) == result

    def teardown(self):
        print('teardown')

    def teardown_class(self):
        print('class teardown')