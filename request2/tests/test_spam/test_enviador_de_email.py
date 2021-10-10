import pytest

from request2.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['raphamoraleng@gmail.com', 'raphamoral@hotmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(destinatario, 'rmoral1991@gmail.com', 'Curse', 'Treinoo focado')

    assert destinatario in resultado


@pytest.mark.parametrize('remetente', ['ale_moral.com', 'raphamoraleng'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente, 'raphamoraleng@gmail.com', 'Curse', 'Treinoo focado')
