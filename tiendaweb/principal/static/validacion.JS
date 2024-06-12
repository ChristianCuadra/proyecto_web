function validar(){
        var nombre = document.getElementById("nombre1").value;
        if (nombre == "" || nombre == null){
            document.getElementById("spannombre").textContent="Debe ingresar un nombre";
        }
        else{
            document.getElementById("spannombre").textContent="";
        }

        var apellido = document.getElementById("apellido1").value;
        if (apellido == "" || apellido == null){
            document.getElementById("spanapellido").textContent="Debe ingresar un apellido";
        }
        else{
            document.getElementById("spanapellido").textContent="";
        }

        var email =  document.getElementById("email1").value;
        if (email == "" || email == null){
            document.getElementById("spancorreo").textContent = "Debe ingresar un correo";
        }
        else{
            document.getElementById("spancorreo").textContent ="";
        }

        var usuario =  document.getElementById("usuario").value;
        if (usuario == "" || usuario == null){
            document.getElementById("spanusuario").textContent = "Debe ingresar un usuario";
        }
        else{
            document.getElementById("spanusuario").textContent ="";
        }

        
        var contrasenna = document.getElementById("password1").value;
        if (contrasenna == "" || contrasenna == null){
            document.getElementById("spancontra").textContent = "Debe ingresar una contraseña.";
        }
        else{
            document.getElementById("spancontra").textContent = "";
            var largo = contrasenna.length;
            if(largo<8 || largo>25){
                document.getElementById("spancontra").textContent = "La contraseña debe tener minimo 8 caracteres y máximo 25.";
            }
            else{
                document.getElementById("spancontra").textContent = "";
            }
        }

        var contrasenna2 = document.getElementById("password2").value;
        if (contrasenna2 == "" || contrasenna2 == null){
            document.getElementById("spancontras").textContent = "Debe ingresar una contraseña.";
        }
        else{
            document.getElementById("spancontras").textContent = "";
            var largo = contrasenna2.length;
            if(largo<8 || largo>25){
                document.getElementById("spancontras").textContent = "La contraseña debe tener minimo 8 caracteres y máximo 25.";
            }
            else{
                document.getElementById("spancontras").textContent = "";
            }
        }


}