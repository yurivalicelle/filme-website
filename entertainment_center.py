# -*- coding: utf-8 -*-
"""This module is in charge of initializing the information of my favorite films and opens a web
page.

Here you can see relevant information about the films, such as their titles, posters and even see
their trailers.

"""
import media
import fresh_tomatoes

public_enemies = media.Movie(
    "Inimigos Públicos",
    '''Os federais tentam derrubar os famosos bandidos americanos John Dillinger, Baby Face
     Nelson e Pretty Boy Floyd durante uma onda de crimes nos anos 1930.''',
    "https://i.ytimg.com/vi/uayBjuU_RPM/movieposter.jpg",
    "https://www.youtube.com/watch?v=ZJnFKOdv27I")

the_lighthouse = media.Movie(
    "O Farol",
    '''Dois guardiões do farol tentam manter sua sanidade enquanto moravam em uma remota e
     misteriosa ilha da Nova Inglaterra na década de 1890.''',
    "https://br.web.img3.acsta.net/pictures/19/12/03/16/59/4821553.jpg",
    "https://www.youtube.com/watch?v=rwExUiQzCD0")

gladiator = media.Movie(
    "Gladiador",
    '''Um ex-general romano se propõe a vingar-se contra o imperador corrupto que assassinou sua
     família e o enviou para a escravidão.''',
    "https://i.ytimg.com/vi_webp/b7nFZaEJ0NI/movieposter.webp",
    "https://www.youtube.com/watch?v=2ExwBe4msUw")

moana = media.Movie(
    "Moana: Um Mar de Aventuras",
    '''Na Polinésia Antiga, quando uma terrível maldição incorrida pelo Semideus Maui chega à ilha
     de Moana, ela responde ao chamado do oceano para procurar o Semideus para consertar as coisas.
    ''', "https://i.ytimg.com/vi_webp/85WM7lBEc6o/movieposter.webp",
    "https://www.youtube.com/watch?v=85WM7lBEc6o")

the_irishman = media.Movie(
    "O Irlandês",
    '''Um velho lembra-se de seu tempo pintando casas para seu amigo Jimmy Hoffa nos anos 50-70.''',
    "https://br.web.img3.acsta.net/pictures/19/09/17/11/32/2399182.jpg",
    "https://www.youtube.com/watch?v=L78AvuU1FLg")

the_silence_of_the_lambs = media.Movie(
    "O Silêncio dos Inocentes",
    '''Um jovem cadete do FBI deve receber a ajuda de um assassino canibal encarcerado e
     manipulador para ajudar a capturar outro assassino em série, um louco que cuida de suas
     vítimas.''',
    "https://images-na.ssl-images-amazon.com/images/I/61OC483MaQL._AC_SX569_.jpg",
    "https://www.youtube.com/watch?v=8Qsq6DrYDxE")

fight_club = media.Movie(
    "Clube da Luta",
    '''Um trabalhador de escritório insone e uma saboneteira do diabo podem cuidar de um clube de
     luta subterrâneo que evolui para algo muito, muito maior.''',
    "https://i.ytimg.com/vi_webp/GGgmCKpc5KA/movieposter.webp",
    "https://www.youtube.com/watch?v=GGgmCKpc5KA")

scott_pilgrim_vs_the_world = media.Movie(
    "Scott Pilgrim Contra o Mundo",
    '''Scott Pilgrim deve derrotar os sete ex-namorados de sua nova namorada para conquistar seu
     coração.''', "https://i.ytimg.com/vi_webp/TxPF0QVxJ2o/movieposter.webp",
    "https://www.youtube.com/watch?v=NPfaM_moVnA")

scarface = media.Movie(
    "Scarface",
    '''Em 1980, em Miami, um determinado imigrante cubano assume um cartel de drogas e sucumbe à
     ganância.''',
    "https://www.gstatic.com/tv/thumb/v22vodart/7539/p7539_v_v8_ab.jpg",
    "https://www.youtube.com/watch?v=nE-7e6w-hi4")

se7en = media.Movie(
    "Seven: Os Sete Crimes Capitais",
    '''Dois detetives, um novato e um veterano, caçam um serial killer que usa os sete pecados
     capitais como motivo.''',
    "https://br.web.img3.acsta.net/pictures/210/124/21012465_2013061319170245.jpg",
    "https://www.youtube.com/watch?v=JXgOWdG5wqU")

movies = [
    public_enemies, the_lighthouse, gladiator, moana, the_irishman,
    the_silence_of_the_lambs, fight_club, scott_pilgrim_vs_the_world, scarface,
    se7en
]

fresh_tomatoes.open_movies_page(movies)
