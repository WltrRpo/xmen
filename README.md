# REST API for test


Python + Flask + MySQL
Deployed at Heroku


Se cuentan con dos servicios, mutant y stats, así:        - mutant (https://xmen-dna-test.herokuapp.com/mutant ) por vía POST recibe un JSON con un string.          responde un status 200 ok si el ADN es mutante, o un status 403 si no es mutante.        - stats (https://xmen-dna-test.herokuapp.com/stats) por vía GET responde 3 datos:          count_human_dna: cantidad de humanos
          count_mutant_dna: cantidad de mutantes
          ratio: porción de mutantes sobre todas las muestras