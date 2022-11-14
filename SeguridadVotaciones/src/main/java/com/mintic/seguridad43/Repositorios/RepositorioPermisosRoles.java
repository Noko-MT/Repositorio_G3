package com.mintic.seguridad43.Repositorios;

import com.mintic.seguridad43.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles, String> {
    @Query("{'permiso.$id':ObjectId(?0),'rol.$id':ObjectId(?1)}")
    PermisosRoles getPermisosRoles(String id_permiso, String id_rol);
}
