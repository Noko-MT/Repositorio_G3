package com.Seguridad.Registraduria_Seguridad.Repositorios;

import com.Seguridad.Registraduria_Seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository<Permiso, String> {
}
