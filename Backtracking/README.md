# Algoritmo Backtracking
O algoritmo de Backtracking é uma técnica de resolução de problemas que lida com a busca sistemática de soluções 
através da exploração de todas as possibilidades, testando cada uma delas para determinar se atende aos critérios 
de solução ou se deve ser descartada. Esse algoritmo é frequentemente usado para resolver problemas de busca, 
otimização, quebra-cabeças e problemas de decisão em que é preciso fazer escolhas em várias etapas para alcançar 
uma solução.

A ideia central do Backtracking é construir uma solução passo a passo, tomando decisões em cada etapa e, 
quando uma decisão leva a um beco sem saída (ou seja, não é possível continuar a construir uma solução válida), 
o algoritmo volta atrás (retorna à etapa anterior) e tenta outra opção. Isso é feito recursivamente até que 
todas as opções tenham sido exploradas ou até que uma solução válida seja encontrada.

Aqui estão os passos básicos para entender como funciona o algoritmo de Backtracking:

1 - Comece em uma etapa inicial e defina o estado inicial.

2 - Faça uma escolha para a etapa atual, como selecionar um valor, um movimento, ou tomar uma decisão específica.

3 - Verifique se a escolha feita na etapa atual é válida, ou seja, se não viola nenhuma restrição 
ou critério de solução.

4 - Se a escolha feita na etapa atual for válida, avance para a próxima etapa e repita os passos 2 a 4 recursivamente.

5 - Se a escolha na etapa atual não for válida, faça um "backtrack" para a etapa anterior e tente outra 
opção ou variação.

6 - Repita os passos 2 a 5 até encontrar uma solução válida ou até explorar todas as opções possíveis.

7 - Quando uma solução válida é encontrada ou todas as opções são exploradas sem sucesso, 
o algoritmo termina e fornece a solução encontrada (se houver uma) ou indica que não há solução possível.

O algoritmo de Backtracking é especialmente útil quando o espaço de busca é grande e não é eficiente examinar 
todas as opções possíveis de forma exaustiva. Ele ajuda a evitar a busca em ramos da árvore de decisões que 
são claramente inviáveis, economizando tempo e recursos computacionais.

Exemplos comuns de problemas resolvidos com o algoritmo de Backtracking incluem o problema das N Rainhas, 
Sudoku, labirintos, quebra-cabeças de palavras cruzadas e muitos outros desafios de busca e decisão.