from galeria.models import Fotografia

foto01 = Fotografia(nome="'Penhascos Cósmicos' na Nebulosa Carina",
                  legenda="webbtelescope.org / NASA / James Webb",
                  descricao="""O que se parece muito com montanhas escarpadas em uma noite enluarada é na 
                  verdade a borda de uma região jovem e próxima de formação de estrelas NGC 3324 na Nebulosa 
                  Carina. Capturada em luz infravermelha pela Near-Infrared Camera ( NIRCam ) no Telescópio 
                  Espacial James Webb da NASA, esta imagem revela áreas anteriormente obscurecidas do 
                  nascimento de estrelas.""",
                  foto="carina-nebula.png"
                  )

foto02 = Fotografia(nome="Buraco Negro",
                  legenda="Telescópios da Terra",
                  descricao="""Imagem gerada pela junção dos dados de vários telescópios da terra, 
                  chegando a melhor imagem já tirada de um buraco negro.""",
                  foto="buraco_negro.png"
                  )

foto02.save()


# usar em 'python manage.py shell'
