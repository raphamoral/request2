from request2.spam.enviador_de_email import Enviador
from request2.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails('raphamoraleng@gmail.com','Aprendendo Junto com a Python Pro', 'Confira se está acertando')
