import pytest

from request2.spam.enviador_de_email import Enviador
from request2.spam.main import EnviadorDeSpam
from request2.spam.modelos import Usuario


@pytest.mark.parametrize('usuarios',
                         [
                             [
                               Usuario(nome='Raphael', email='raphamoraleng@gmail.com'),
                               Usuario(nome='Renzo', email='raphamoraleng@gmail.com')
                             ],
                             [
                               Usuario(nome='Raphael', email='raphamoraleng@gmail.com')
                             ]
                         ]
                         )
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('raphamoraleng@gmail.com',
                                   'Aprendendo Junto com a Python Pro',
                                   'Confira se está acertando')
    assert len(usuarios) == enviador.qtd_email_enviados
