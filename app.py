from flask import Flask, render_template , Request

app = Flask(__name__)


#Utilize o Flask para desenvolver uma aplicação web sobre um tema de sua escolha. Ela deverá conter 4 páginas: Início,
# , Sobre, Contato e uma quarta página especial, que deverá conter algum tipo de conteúdo da sua escolha.
#Cada página deverá estar em um template do Flask
#um arquivo HTML que será renderizado pela aplicação.




# Início
@app.route("/")
def homepage():
    return render_template("index.html")

#Sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

#Contatos
@app.route("/contato")
def contato():
    return render_template("contato.html")

#Especial
@app.route("/especial")
def especial():
    carro = str(input('Digite o carro'))
    api_url = "https://api.hgbrasil.com/weather?woeid=456995"
    reponse = request.get(api_url)
    arquivo = reponse.json()

    return render_template("especial.html", arquivo=arquivo)



#colocar o site
if __name__ == '__main__':
    app.run(debug=True)