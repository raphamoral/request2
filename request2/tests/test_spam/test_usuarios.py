from request2.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Raphael', email='raphamoraleng@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Raphael', email='raphamoraleng@gmail.com'),
                Usuario(nome='Renzo', email='raphamoraleng@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
