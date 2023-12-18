#instalar rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# IMPORTANTE: reiniciar la shell
#instalar paquete wasm
rustup target add wasm32-unknown-unknown
#instalar soroban
cargo install --locked --version 20.0.0-rc.4.1 soroban-cli
#activar el autocompletar
echo "source <(soroban completion --shell bash)" >> ~/.bashrc
#instalar la testnet de Soroban
soroban config network add --global testnet \
  --rpc-url https://soroban-testnet.stellar.org:443 \
  --network-passphrase "Test SDF Network ; September 2015"

#configurar una identidad
soroban config identity generate --global pato
#ver la llave publica asociada
soroban config identity address pato

#pedir tokens de la testnet
curl "https://friendbot.stellar.org/?addr=$(soroban config identity address pato)"




#crear una nueve libreria cargo
#esto crea una nuevo paquete: hello-world, con una carpeta src y una confifguracion toml
cargo new --lib hello-world
