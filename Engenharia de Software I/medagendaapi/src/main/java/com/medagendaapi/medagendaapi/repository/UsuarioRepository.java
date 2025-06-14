package com.medagendaapi.medagendaapi.repository;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import com.medagendaapi.medagendaapi.model.Usuario;

public interface UsuarioRepository extends JpaRepository<Usuario, Long> {

    @Query("""
            SELECT u from Usuario u
            WHERE u.nomeUsuario LIKE %:termoBusca%
            """)
    List<Usuario> busca(String termoBusca);


    
}
