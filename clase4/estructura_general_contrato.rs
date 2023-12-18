// Esta línea es para indicarle al compilador que no incluya la librería estándar de Rust.
// Esta trae demasiadas cosas que no necesitamos y hace que el contrato sea más grande de lo necesario.
#![no_std]

//Esta linea importa los elementos necesarios para la construccion de un Smart Contract para Soroban
//La macro contractimpl se usa para implementar el contrato, mientras que la macro log se usa para generar las bitacoras
// La variable Env es la que contiene el entorno de ejecución del contrato. Trae algunas variables equivalentes a las 
// msg.sender o msg.value de Ethereum
//Symbol es un tipo de dato que representa un string que es muy eficiente en el uso de memoria
use soroban_sdk::{contractimpl, log, Env, Symbol};

//Esto define una variable de tipo Symbol llamada counter
//Es el equivalente a las variables de estado en Ethereum
const COUNTER: Symbol = symbol_short!("COUNTER");

//Esto indica que vamos a definir un struct tipo Smart contract llamado IncrementContract
//Cumple una funcion analoga a contract xxxxxx {} de Solidity
#[contract]
pub struct IncrementContract;

//Esta es la implementacion misma del contrato
//Se usa la macro contractimpl para indicar que se va a implementar el contrato IncrementContract
//Las funciones aqui contenidas será exportadas como funciones del contrato
#[contractimpl]
impl IncrementContract {

    //Se define una funcion llamada increment que recibe como parametro el entorno de ejecucion del contrato y 
    //que retorna un entero de 32 bits sin signo
    //Esta funcion es el equivalente a una funcion setter en solidity
    pub fn increment(env: Env) -> u32 {
        
        
        //Declaramos una variable mutable de 32 bits sin signo llamada count
        //Se lee su valor desde el storage permanente del entorno de ejecucion
        //El unwrap_or(0) permite definir el valor en caso que la variable no esté definida
        let mut count: u32 = env.storage().instance().get(&COUNTER).unwrap_or(0); 

        //Una anotacion en la bitacora
        log!(&env, "count: {}", count);

        //Se incrementa el valor de contador en 1
        count += 1;

        // Se guarda el nuevo valor de contador en el storage permanente del entorno de ejecucion
        env.storage().instance().set(&COUNTER, &count);

        // Retornamos el valor del contador
        count
    }

    /// Esta funcion solo toma el valor guardado en el storage y lo devuelve
    // Equivale a un getter en solidity
    pub fn get_count(env: Env) -> u32 {
        env.storage().instance().get(&COUNTER).unwrap_or(0)
    }
}