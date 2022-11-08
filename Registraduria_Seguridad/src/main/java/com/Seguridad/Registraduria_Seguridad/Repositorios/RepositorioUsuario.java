package com.Seguridad.Registraduria_Seguridad.Repositorios;

import com.Seguridad.Registraduria_Seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario, String> {
}
