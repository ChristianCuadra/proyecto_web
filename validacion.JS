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

        
        var contrasenna = document.getElementById("password1").value;
        if (contrasenna == "" || contrasenna == null){
            document.getElementById("spancontra").textContent = "Debe ingresar una contraseña.";
        }
        else{
            document.getElementById("spancontra").textContent = "";
        }


        if (contrasenna.length<8 && contrasenna.length>25){
            document.getElementById("spancontra").textContent = "La contraseña debe contener minimo 8 caracteres y máximo 25";
        }
        else{
            document.getElementById("spancontra").textContent ="";
        }





    }