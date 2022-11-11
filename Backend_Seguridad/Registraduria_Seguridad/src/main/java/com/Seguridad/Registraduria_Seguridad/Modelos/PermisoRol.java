package com.Seguridad.Registraduria_Seguridad.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document
public class PermisoRol {

    @Id
    private String _id;

    @DBRef
    private Permiso permiso;
    @DBRef
    private  Rol rol;

    public String get_id() {
        return _id;
    }

    public Permiso getPermiso() {
        return permiso;
    }
    public void setPermiso(Permiso permiso) {
        this.permiso = permiso;
    }

    public Rol getRol() {
        return rol;
    }
    public void setRol(Rol rol) {
        this.rol = rol;
    }
}
