from unittest.mock import Mock

import pytest

from request2.spam.main import EnviadorDeSpam
from request2.spam.modelos import Usuario


@pytest.mark.parametrize('usuarios',
                         [
                             [
                                 Usuario(nome='Raphael', email='raphamoraleng@gmail.com'),
                                 Usuario(nome='Renzo', email='renzo@gmail.com')
                             ],
                             [
                                 Usuario(nome='Raphael', email='raphamoraleng@gmail.com')
                             ]
                         ]
                         )
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('raphamoraleng@gmail.com',
                                   'Aprendendo Junto com a Python Pro',
                                   'Confira se está acertando')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Raphael', email='raphamoraleng@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('rmoral1991@gmail.com',
                                   'Aprendendo Junto com a Python Pro',
                                   'Confira se está acertando')
    enviador.enviar.assert_called_once_with == ('rmoral1991@gmail.com',
                                                'raphamoraleng@gmail.com',
                                                'Aprendendo Junto com a Python Pro',
                                                'Confira se está acertando')
