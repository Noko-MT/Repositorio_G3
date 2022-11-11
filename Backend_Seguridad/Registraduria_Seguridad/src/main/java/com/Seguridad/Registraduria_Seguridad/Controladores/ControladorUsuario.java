package com.Seguridad.Registraduria_Seguridad.Controladores;

import com.Seguridad.Registraduria_Seguridad.Modelos.Rol;
import com.Seguridad.Registraduria_Seguridad.Modelos.Usuario;
import com.Seguridad.Registraduria_Seguridad.Repositorios.RepositorioRol;
import com.Seguridad.Registraduria_Seguridad.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/usuarios")
public class ControladorUsuario {

    @Autowired
    private RepositorioUsuario miRepositorioUsuario;
    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("")
    public List<Usuario> index() {return this.miRepositorioUsuario.findAll();}

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Usuario create (@RequestBody Usuario infoUsuario) {
        infoUsuario.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
        return this.miRepositorioUsuario.save(infoUsuario);
    }

    @PutMapping("{id}")
    public Usuario update(@PathVariable String id, @RequestBody Usuario infoUsuario) {
        Usuario usuario = this.miRepositorioUsuario.findById(id).orElse(null);
        if (usuario != null){
            usuario.setSeudonimo(infoUsuario.getSeudonimo());
            usuario.setCorreo(infoUsuario.getCorreo());
            usuario.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
            return this.miRepositorioUsuario.save(usuario);
        }else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        Usuario usuario = this.miRepositorioUsuario.findById(id).orElse(null);
        if (usuario != null){
            this.miRepositorioUsuario.delete(usuario);
        }
    }

    @GetMapping("{id}")
    public Usuario show(@PathVariable String id) {
        Usuario usuario = this.miRepositorioUsuario.findById(id).orElse(null);
        return usuario;
    }

    @PutMapping("{id_usuario}/rol/{id_rol}")
    public Usuario setRol(@PathVariable String id_usuario, @PathVariable String id_rol) {
        Usuario usuario =this.miRepositorioUsuario.findById(id_usuario).orElse(null);
        Rol rol = this.miRepositorioRol.findById(id_rol).orElse(null);
        if (usuario != null && rol != null) {
            usuario.setRol(rol);
            return this.miRepositorioUsuario.save(usuario);
        } else {
            return null;
        }
    }

    //Validar correo y contraseña
    @PostMapping("/validate")
    public Usuario validate(@RequestBody Usuario infoUsuario, final HttpServletResponse response) throws IOException {
        Usuario usuario = this .miRepositorioUsuario.getUserByEmail(infoUsuario.getCorreo());
        if (usuario != null) {
            if (usuario.getContrasena().equals(convertirSHA256(infoUsuario.getContrasena()))) {
                usuario.setContrasena("");
                return usuario;
            } else {
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
                return null;
            }
        } else {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
    //Cifrado contraseña
    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        }
        catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for(byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
