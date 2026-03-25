#!/bin/bash

# Cores para o output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Iniciando extração de dados da toMicroservices...${NC}"

# Loop pelos participantes
for p in 1 2 3
do
    echo -e "
${GREEN}Processando Participante $p...${NC}"
    
    # JPetStore
    # Verifique se o nome do arquivo JSON está correto (ex: jpetstore.json ou participant_1.json)
    if [ -f "result_study_case/participant_$p/jpetstore.json" ]; then
        python3 extract_tomicroservices.py result_study_case/participant_$p/jpetstore.json jpetstore p$p
    else
        echo "Aviso: Arquivo JPetStore para p$p não encontrado."
    fi

    # Spring PetClinic
    if [ -f "result_study_case/participant_$p/petclinic.json" ]; then
        python3 extract_tomicroservices.py result_study_case/participant_$p/petclinic.json spring-petclinic p$p
    else
        echo "Aviso: Arquivo PetClinic para p$p não encontrado."
    fi
done

echo -e "
${GREEN}Extração concluída!${NC}"
echo "Agora você pode rodar 'python3 main.py' para gerar as métricas."
