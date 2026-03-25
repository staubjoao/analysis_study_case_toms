import json
import os
import sys

# Mapeamento para nomes de pastas amigáveis
OBJECTIVE_MAP = {
    "CohesionPerMicroserviceArchitecture": "cohesion",
    "CouplingPerMicroserviceArchitecture": "coupling",
    "FunctionalityPerMicroserviceArchitecture": "functionality",
    "OverheadMaxPerMicroserviceArchitecture": "overhead",
    "ReusePerMicroserviceArchitecture": "reuse",
    "BestTradeOffIdealPointDistance": "best_tradeoff"
}

def shorten_name(full_name):
    """
    Converte 'org.mybatis.jpetstore.domain.Account.getZip' 
    em 'Account.getZip'
    """
    if not full_name:
        return "unknown"
    # Lida com casos especiais como _star_t_
    if "_star_t_" in full_name:
        return full_name
        
    parts = full_name.split('.')
    if len(parts) >= 2:
        return f"{parts[-2]}.{parts[-1]}"
    return full_name

def extract_decompositions(json_file, app_name, participant_id):
    if not os.path.exists(json_file):
        print(f"Erro: Arquivo {json_file} nao encontrado.")
        return

    with open(json_file, 'r') as f:
        data = json.load(f)

    tool_name = f"tomicroservices_{participant_id}"

    # O JSON de entrada é uma lista de execuções (uma para cada métrica/objetivo)
    for entry in data:
        metric_full_name = entry.get("metric")
        objective = OBJECTIVE_MAP.get(metric_full_name, metric_full_name.lower())
        
        microservices_list = entry.get("microservices", [])
        num_partitions = len(microservices_list) # Aqui ele pega a quantidade de MS dessa solução específica
        
        decomposition_dict = {}
        
        for ms in microservices_list:
            # Garante o nome microservice0, microservice1...
            ms_id = ms.get("id").lower() 
            
            components = []
            # Usamos um set para evitar duplicatas de IDs dentro do mesmo microserviço
            seen_ids = set()
            
            for comp in ms.get("components", []):
                short_name = shorten_name(comp.get("name"))
                if short_name not in seen_ids:
                    components.append({"id": short_name})
                    seen_ids.add(short_name)
            
            decomposition_dict[ms_id] = components

        # Montar a estrutura final exatamente como solicitado
        final_output = {
            "tool": {
                "decomposition": decomposition_dict
            }
        }

        # Caminho: data/decompositions/jpetstore/tomicroservices_1/4_partitions/cohesion/
        target_dir = f"data/decompositions/{app_name}/{tool_name}/{num_partitions}_partitions/{objective}"
        os.makedirs(target_dir, exist_ok=True)
        
        target_file = os.path.join(target_dir, "method_decomposition.json")
        with open(target_file, 'w') as f:
            json.dump(final_output, f, indent=4)
        
        print(f"✅ Exportado: {objective} ({num_partitions} partições) em {target_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python extract_tomicroservices.py [arquivo.json] [nome_da_app] [id_participante]")
    else:
        extract_decompositions(sys.argv[1], sys.argv[2], sys.argv[3])