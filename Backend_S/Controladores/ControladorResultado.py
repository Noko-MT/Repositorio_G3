from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Modelos.Resultado import Resultado

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, inforesultado, id_mesa, id_candidato):
        resultado = Resultado(inforesultado)
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultado.mesa = mesa
        resultado.candidato = candidato
        return self.repositorioResultado.save(resultado)

    def update(self, infoResultado, id_resultado, id_mesa, id_candidato):
        resultado = Resultado(self.repositorioResultado.findById(id_resultado))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultado.numero_votos = infoResultado['numero_votos']
        resultado.mesa = mesa
        resultado.candidato = candidato
        return self.repositorioResultado.save(resultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    def show(self, id):
        resultado = Resultado(self.repositorioResultado.findById(id))
        return resultado.__dict__
