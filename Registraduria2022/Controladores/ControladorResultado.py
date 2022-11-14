from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

class ControladorResultado():
    def __init__(self):#CONSTRUCTOR
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):#OPTENER TODOS LOS DATOS
        return self.repositorioResultado.findAll()

    def create(self, infoResultado, id_candidato, id_mesa):#CREAR UN DOCUMENTO EN EL MODELO
        resultado = Resultado(infoResultado)
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.repositorioResultado.save(resultado)

    def update(self, id_resultado, infoResultado, id_candidato, id_mesa):#ACTUALIZAR DATOS DEL MODELO
        resultado = Resultado(self.repositorioResultado.findById(id_resultado))
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultado.numero_votos = infoResultado['numero_votos']
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.repositorioResultado.save(resultado)

    def delete(self, id): # BORRAR DATOS DEL MODELO
        return self.repositorioResultado.delete(id)

    def show(self, id): # CONSULTAR UN DATO ESPECIFICO DEL MODELO
        resultado = Resultado(self.repositorioResultado.findById(id))
        return resultado.__dict__