# page-sku
Responsável pelo modelo base de um produto scrapeado.  

# install
`pip install git+https://github.com/la-catalog/page-sku.git`  

# model
* _id
    * Identificador único do sku.
* product
    * Identificador do produto, ou seja, aquela familia de skus.
* code
    * Código usado pelo marketplace para representar aquele sku.
        * Cuidado:
            * Este código pode estar na URL.
            * Este código pode estar pelo HTML da página.
            * O código da URL pode não ser o código do SKU.
            * O código da URL pode representar um grupo de SKUs.
        * Exemplos:
            * Amazon usa o código do sku deles na URL.  
                * https://www.amazon.com.br/dp/B072C67WDN
                    * Código: B072C67WDN
            * Rihappy deixa o código do sku deles no HTML.
                * https://www.rihappy.com.br/dino-papa-tudo-elka/p
                    * Código: 100127502
    * Caso não encontre, utilizar o código na URL.
* name
    * Nome do sku.
* brand
    * Marca do sku.
* description
    * Descrição do sku.
* gtin
    * GTIN do sku.
* prices
    * Preços do sku, ou seja, pode possuir preço com e sem desconto.
* segments
    * Segmentos do sku, caminhando do segmento mais externo para o mais interno (mais específico).
* attributes
    * Atributos do sku, sem remoção de nenhum atributo que já esteja em outra categoria do sku.
* measurement
    * Quaisqueres medidas relacionadas ao sku.
* package
    * Quaisqueres medidas relacionadas ao sku dentro do pacote.
* rating
    * Avaliação do produto após ser convertida para números.
    * **Contexto**: cada marketplace pode avaliar da maneira que desejar então é necessário converter para números para melhor conseguir avaliar no futuro.
    * **Exemplos**:
        * Sistema nota de 1,2,3,4 e 5
            * 1 => 1.0 (min)
            * 2 => 2.0
            * 3 => 3.0
            * 4 => 4.0
            * 5 => 5.0 (max)
        * Sistema Like & Dislike
            * Like => 0.0 (min)
            * Dislike => 1.0 (max)
        * Sistema 😠😟😕😐🙂😃😁
            * 😠 => -3.0 (min)
            * 😟 => -2.0
            * 😕 => -1.0
            * 😐 => 0.0
            * 🙂 => 1.0
            * 😃 => 2.0
            * 😁 => 3.0 (max)
    * Não é preciso tratar zero como o minímo valor, pode usar número negativos para melhor representação.
* audios
    * URLs de aúdios do sku.
* images
    * URLs de imagens do sku.
* videos
    * URLs de videos do sku.
* variations
    * URLs de variações do sku.
* sources
    * URLs visitados para formar esse sku.
* links
    * URLs para outros skus, pois dentro de uma página podemos descobrir outros skus para serem scrapeados.
* marketplace
    * Nome do marketplace seguindo o padrão [snake_case](https://en.wikipedia.org/wiki/Snake_case).
* metadata
    * [Dados que providência informações sobre os dados do sku](https://en.wikipedia.org/wiki/Metadata).

# reference

["A norma diz que as medidas devem ser colocadas na ordem: comprimento x largura x altura (ou profundidade)."](https://www.diferenca.com/comprimento-largura-e-altura/#:~:text=A%20norma%20diz%20que%20as,x%20altura%20(ou%20profundidade).)