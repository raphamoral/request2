import pytest

from request2.spam.db import Conexao
from request2.spam.modelos import Usuario


@pytest.fixture
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


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Raphael')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Raphael'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
