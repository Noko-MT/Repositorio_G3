package com.Seguridad.Registraduria_Seguridad.Repositorios;

import com.Seguridad.Registraduria_Seguridad.Modelos.PermisoRol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermisoRol extends MongoRepository<PermisoRol, String>{
}
