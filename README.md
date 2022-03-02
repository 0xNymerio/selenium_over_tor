# Selenium Over Tor
POC to test automated web requisitions over Tor.

# Contexto
O [Beco do Exploit](https://www.becodoexploit.com/) iniciou o projeto [Beco.py](https://github.com/h41stur/beco.py), sendo um treinamento para a comunidade sobre Python, abordando as bases/fundamentos da linguagem e funcionalidades básicas do dia a dia, como: O.O, Sockets, conexões com um DB, Flask API e Web scraping.

A cereja do bolo é que, como é feito para a comunidade, em todo o percurso foi abordado do Python com uma ótica ofensiva. Sairam boas idéias dos papos em aula, perspectivas diferentes, entendendo alguns conceitos e impactos diferentes, no final não é apenas aprender python, mas sim a comunidade compartilhando conhecimento e experiências entre si.

Dado o contexto, após aprendermos sobre Selenium, ficou o estudo de tentar aplicar o crawler passando pela rede Tor. Fiz só o basico para coletar o IP normal e o IP em rede Tor, mas entendendo os fundamentos, posso amplicar o crawler para outras direções.

Aqui o ponto chave de aprendizado é entender como o Selenium funciona na unha, criando um profile para adicionarmos uma rota de proxy, subir o serviço Tor localmente e enviar as requisições. O objetivo não é reinventar a roda, mas sim entender como configurar um proxy encima do Selenium e naturalmente ampliando o pensamento ofensivo pela experiência adquirida.

Enjoy!

