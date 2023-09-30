"""
Em Python, a importação é o processo de trazer módulos ou pacotes externos para o seu programa 
para que você possa usar suas funcionalidades. Os módulos e pacotes contêm funções, 
classes e variáveis que você pode usar para estender as capacidades do Python. 
"""
# 1. **Importação de Módulos:**
"""
Para importar um módulo, você usa a palavra-chave `import`, seguida do nome do módulo. 
Você pode acessar funções e variáveis do módulo usando a notação de ponto.
"""
import math

raiz_quadrada = math.sqrt(25)
print(raiz_quadrada)  # Isso imprimirá 5.0

# 2. **Importação com Alias:**
"""
Você pode dar um alias (apelido) ao módulo importado usando a palavra-chave `as`. 
Isso é útil quando você deseja simplificar o nome do módulo.
"""
import math as m
raiz_quadrada = m.sqrt(25)

# 3. **Importação de Funções ou Variáveis Específicas:**
"""
Em vez de importar um módulo inteiro, você pode importar funções ou variáveis específicas de um módulo.
"""
from math import sqrt

raiz_quadrada = sqrt(25)


# 4. **Importação de Todos os Itens de um Módulo:**
"""
Você também pode importar todos os itens de um módulo usando `*`, mas isso não é recomendado, 
pois pode poluir o namespace com muitos nomes.
"""
from math import *

# 5. **Importação de Pacotes:**
"""
Além de módulos individuais, você pode importar pacotes inteiros. Um pacote é uma coleção de 
módulos relacionados em um diretório.
"""
import pandas as pd  # Importa o pacote pandas com um alias "pd"


# 6. **Importação Condicional:**
"""
Às vezes, você pode querer importar um módulo apenas se certas condições forem atendidas. 
Você pode fazer isso usando a declaração `import` condicional.

if condicao:
    import modulo
"""    

# 7. **Módulo Principal (`__main__`):**
"""
Quando um arquivo Python é executado diretamente, ele é considerado o módulo principal e é atribuído 
o nome `__main__`. Isso permite que você escreva código que só é executado quando o arquivo 
é executado diretamente, não quando é importado como um módulo em outro arquivo.

if __name__ == "__main__":
    # Código a ser executado quando o arquivo é executado diretamente

A importação é uma parte fundamental da programação Python, pois permite que você reutilize 
código de outras fontes e organize seu código em módulos e pacotes para torná-lo mais limpo e modular.
"""