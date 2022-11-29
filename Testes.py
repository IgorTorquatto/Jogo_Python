import jogo
import MOD_1
import MOD_2

def test_tela():
    assert jogo.TELA_MENU_ALTURA != 0
    assert jogo.TELA_MENU_LARGURA != 0
    assert jogo.TELA_JOGO_ALTURA != 0
    assert jogo.TELA_JOGO_LARGURA != 0

def test_velocidade_incial():
    assert jogo.VELOCIDADE_INICIAL == 0

def test_musica():
    assert jogo.MUSICA_JOGO == "audios/musica.ogg"

def test_button():
    assert MOD_1.Button != False

def test_recs():
    assert MOD_2.WIDTH != 0
    assert MOD_2.WIDTH != 0
