
function onFormSubmit(){

    var form = document.getElementById("formulario");
    var peso1 = document.getElementById("peso1");
    var peso2 = document.getElementById("peso2");
    var peso3 = document.getElementById("peso3");
    var aptosvotar1 = document.getElementById("categoria1aptosvotar");
    var aptosvotar2 = document.getElementById("categoria2aptosvotar");
    var aptosvotar3 = document.getElementById("categoria3aptosvotar");
    var cand1eleitor1 = document.getElementById("cand1eleitor1");
    var cand1eleitor2 = document.getElementById("cand1eleitor2");
    var cand1eleitor3 = document.getElementById("cand1eleitor3");
    var cand2eleitor1 = document.getElementById("cand2eleitor1");
    var cand2eleitor2 = document.getElementById("cand2eleitor2");
    var cand2eleitor3 = document.getElementById("cand2eleitor3");
    var cand3eleitor1 = document.getElementById("cand3eleitor1");
    var cand3eleitor2 = document.getElementById("cand3eleitor2");
    var cand3eleitor3 = document.getElementById("cand3eleitor3");
    var qtdcat = document.getElementById("categoria");
  
  
//  form.addEventListener('submit', function(e){
    console.log((peso1.value*cand1eleitor1.value)/categoria1aptosvotar.value + (peso2.value*cand1eleitor2.value)/categoria2aptosvotar + (peso3.value*cand1eleitor3.value)/categoria3aptosvotar);
    document.getElementById("Candidato1Resultado").value = (peso1.value*cand1eleitor1.value)/categoria1aptosvotar.value + (peso2.value*cand1eleitor2.value)/categoria2aptosvotar.value + (peso3.value*cand1eleitor3.value)/categoria3aptosvotar.value
    document.getElementById("Candidato2Resultado").value = (peso1.value*cand2eleitor1.value)/categoria1aptosvotar.value + (peso2.value*cand2eleitor2.value)/categoria2aptosvotar.value + (peso3.value*cand2eleitor3.value)/categoria3aptosvotar.value
    document.getElementById("Candidato3Resultado").value = (peso1.value*cand3eleitor1.value)/categoria1aptosvotar.value + (peso2.value*cand3eleitor2.value)/categoria2aptosvotar.value + (peso3.value*cand3eleitor3.value)/categoria3aptosvotar.value
   
  
    var votosCandidato1 = document.getElementById("Candidato1Resultado").value
    var votosCandidato2 = document.getElementById("Candidato2Resultado").value
    var votosCandidato3 = document.getElementById("Candidato3Resultado").value
  
    if (votosCandidato1.value > votosCandidato2.value)
      if (votosCandidato1.value > votosCandidato3.value)
        document.getElementById("Candidato1Resultado").style.color = "green";
      else
        document.getElementById("Candidato3Resultado").style.color = "green";
    else if (votosCandidato2.value > votosCandidato3.value)
      document.getElementById("Candidato2Resultado").style.color = "green";
    else
      document.getElementById("Candidato3Resultado").style.color = "green";
  
//    e.preventDefault();
//  });
  
	
}
