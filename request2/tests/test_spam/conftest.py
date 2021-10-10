import pytest

from request2.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    # Tear Down
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()
    # Tear Down
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
