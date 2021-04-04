import pytest
from code import people, shelf, add_shelf, add, delete, move, list_docs, documents, directories


class TestCode:

    def setup(self):
        print('setup')

    def test_check_docs_list(self):
        assert list_docs() == [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
    ]

    @pytest.mark.parametrize(('doc_number', 'result'),[('11-2','Геннадий Покемонов'), ('1234', False)])
    def test_find_people(self, doc_number, result):
        assert people(doc_number) == result

    @pytest.mark.parametrize(('doc_number', 'result'),[('11-2','1'), ('1234', False)])
    def test_find_shelf(self, doc_number, result):
        assert shelf(doc_number) == result

    @pytest.mark.parametrize(('doc_number', 'doc_type', 'doc_name', 'shelf_number', 'result'), [('11-2', 'invoice', 'Valisi', '1', False), ('1234', 'passport', 'Alisa', '4', False), ('1234', 'passport', 'Alisa', '1', True)])
    def test_add_doc(self, doc_number, doc_type, doc_name, shelf_number,result ):
        assert add(doc_number, doc_type, doc_name, shelf_number) == result

    @pytest.mark.parametrize(('doc_number', 'result'),[('10006',True), ('11-3', False)])
    def test_delete_doc(self, doc_number, result):
        assert delete(doc_number) == result

    @pytest.mark.parametrize(('doc_number', 'shelf_number', 'result'),[('11-2', '1', False), ('1234', '1', False),('11-2', '3', True), ('11-2', '4', False)])
    def test_move_doc(self, doc_number, shelf_number, result):
        assert move(doc_number, shelf_number) == result

    @pytest.mark.parametrize(('shelf_number', 'result'), [('1', False), ('4', True)])
    def test_add_shelf(self, shelf_number, result):
        assert add_shelf(shelf_number) == result

    def teardown(self):
        print('teardown')

    def teardown_class(self):
        print('class teardown')
