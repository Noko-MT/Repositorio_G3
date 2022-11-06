package com.Seguridad.Registraduria_Seguridad.Repositorios;

import com.Seguridad.Registraduria_Seguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol, String> {

}
