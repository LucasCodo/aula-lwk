import lwk

network = lwk.Network.mainnet()  # Definindo rede principal
# Definindo Frase semente
seed_phrase = []  # Adicione suas palavras
mnemonic = lwk.Mnemonic(" ".join(seed_phrase))  # Instanciando objeto mnemonico
client = network.default_electrum_client()  # Instanciando conexão com a blockchain
signer = lwk.Signer(mnemonic, network)  # Instanciando signer
desc = signer.wpkh_slip77_descriptor()  # Capturando descritor para watch-only

wollet = lwk.Wollet(network, desc, datadir=None)  # Definindo wallet watch-only
update = client.full_scan(wollet)  # Buscando atualizações da wallet
wollet.apply_update(update)  # Aplicando atualizações na wallet watch-only
print("Balanço atual:", wollet.balance())  # Mostrando o balanço dos assets da wallet


builder = network.tx_builder()  # Instanciando o construtor de transações
# Definindo o asset da transação
asset = network.policy_asset()  # ou seu asset. ex: '6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d'
# Definindo o endereço da transação; Troque pelo endereço de sua preferencia
address = lwk.Address("lq1qqdccaarjrrk605s0tc9pp7may6d5pe4rlpf0dt75m479ly5y4a228q3v8s2n9n9rnyfzez3tmmx38tetkh8qchd5dtghqsy2m")
asset_amount = 1000  # Definindo o valor da transação
builder.add_recipient(address, asset_amount, asset)  # Adicionando os parametros ao contrutor de transações
unsigned_pset = builder.finish(wollet)  # Criando Transação não assinada
signed_pset = signer.sign(unsigned_pset)  # Assinando transação
finalized_pset = wollet.finalize(signed_pset)  # Finalizando Transação
tx = finalized_pset.extract_tx()  # Extraindo transação
txid = client.broadcast(tx)  # Transmitindo transação

wollet.wait_for_tx(txid, client)  # Aguardando as confirmações da Transação na blockchain
print("Balanço atual:", wollet.balance())  # Mostrando o balanço dos assets da wallet
