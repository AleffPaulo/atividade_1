from flask import Flask, jsonify

app = Flask(__name__)

# Lista estatica de filmes
filmes = [
    {
        "id": 1,
        "titulo": "O Poderoso Chefao",
        "descricao": "A historia da familia mafiosa Corleone atraves dos olhos do patriarca Vito Corleone e seu filho Michael.",
        "ano": 1972,
        "diretor": "Francis Ford Coppola"
    },
    {
        "id": 2,
        "titulo": "Pulp Fiction",
        "descricao": "As vidas de dois assassinos da mafia, um boxeador, um gangster e sua esposa, e um par de bandidos se entrelacam em quatro historias de violencia e redencao.",
        "ano": 1994,
        "diretor": "Quentin Tarantino"
    },
    {
        "id": 3,
        "titulo": "A Origem",
        "descricao": "Um ladrao que rouba segredos corporativos atraves do uso da tecnologia de compartilhamento de sonhos recebe a tarefa inversa de plantar uma ideia na mente de um CEO.",
        "ano": 2010,
        "diretor": "Christopher Nolan"
    },
    {
        "id": 4,
        "titulo": "Clube da Luta",
        "descricao": "Um trabalhador de escritorio insone e um fabricante de sabao formam um clube de luta clandestino que evolui para algo muito mais.",
        "ano": 1999,
        "diretor": "David Fincher"
    },
    {
        "id": 5,
        "titulo": "Matrix",
        "descricao": "Um hacker descobre a verdade chocante sobre a realidade e seu papel na guerra contra seus controladores.",
        "ano": 1999,
        "diretor": "Lana e Lilly Wachowski"
    }
]

@app.route('/')
def home():
    return jsonify({"message": "Ola, bem-vindo a minha API de Catalogo de Filmes!"})

@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify({"filmes": filmes})

@app.route('/filmes/<int:filme_id>', methods=['GET'])
def obter_filme(filme_id):
    filme = next((f for f in filmes if f['id'] == filme_id), None)
    if filme:
        return jsonify({"filme": filme})
    return jsonify({"erro": "Filme nao encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
