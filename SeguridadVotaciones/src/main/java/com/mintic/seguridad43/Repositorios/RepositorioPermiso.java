package com.mintic.seguridad43.Repositorios;

import com.mintic.seguridad43.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermiso extends MongoRepository<Permiso, String> {
    @Query("{'url': ?0, 'metodo': ?1}")
    Permiso getPermiso(String url, String metodo);
}
