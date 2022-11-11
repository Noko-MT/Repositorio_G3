package com.Seguridad.Registraduria_Seguridad.Controladores;

import com.Seguridad.Registraduria_Seguridad.Modelos.Permiso;
import com.Seguridad.Registraduria_Seguridad.Modelos.PermisoRol;
import com.Seguridad.Registraduria_Seguridad.Modelos.Rol;
import com.Seguridad.Registraduria_Seguridad.Repositorios.RepositorioPermiso;
import com.Seguridad.Registraduria_Seguridad.Repositorios.RepositorioPermisoRol;
import com.Seguridad.Registraduria_Seguridad.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permiso-rol")
public class ControladorPermisoRol {

    @Autowired
    private RepositorioPermisoRol miRepositorioPermisoRol;
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;
    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("")
    public List<PermisoRol> index() {
        return this.miRepositorioPermisoRol.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisoRol create(@PathVariable String id_rol, @PathVariable String id_permiso) {
        PermisoRol permisoRol = new PermisoRol();
        Rol rol = this.miRepositorioRol.findById(id_rol).orElse(null);
        Permiso permiso = this.miRepositorioPermiso.findById(id_permiso).orElse(null);
        if (rol != null && permiso != null) {
            permisoRol.setRol(rol);
            permisoRol.setPermiso(permiso);
            return this.miRepositorioPermisoRol.save(permisoRol);
        } else {
            return null;
        }
    }

    @PutMapping("{id_permiso_rol}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisoRol update(@PathVariable String id_permiso_rol, @PathVariable String id_rol, @PathVariable String id_permiso) {
        PermisoRol permisoRol = this.miRepositorioPermisoRol.findById(id_permiso_rol).orElse(null);
        Rol rol = this.miRepositorioRol.findById(id_rol).orElse(null);
        Permiso permiso = this.miRepositorioPermiso.findById(id_permiso).orElse(null);
        if (permisoRol != null && rol != null && permiso != null) {
            permisoRol.setRol(rol);
            permisoRol.setPermiso(permiso);
            return this.miRepositorioPermisoRol.save(permisoRol);
        } else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        PermisoRol permisoRol = this.miRepositorioPermisoRol.findById(id).orElse(null);
        if (permisoRol != null) {
            this.miRepositorioPermisoRol.delete(permisoRol);
        }
    }

    @GetMapping("{id}")
    public PermisoRol show(@PathVariable String id) {
        PermisoRol permisoRol = this.miRepositorioPermisoRol.findById(id).orElse(null);
        return permisoRol;
    }

}
