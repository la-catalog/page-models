# page-models
Responsável por diversos modelos usados pelos scrapers.  

# install
`pdm add git+https://github.com/la-catalog/page-models.git`  

# SKU
* _id
    * **Descrição**: Identificador único do SKU.
* code
    * **Descrição**: Código usado pelo marketplace para representar aquele SKU.
    * **Atenção**:
        * Este código pode estar na URL.
        * Este código pode estar pelo HTML da página.
        * O código da URL pode não ser o código do SKU.
        * O código da URL pode representar um grupo de SKUs.
    * **Exemplos**:
        * Amazon usa o código do SKU deles na URL.  
            * https://www.amazon.com.br/dp/B072C67WDN
            * Código: B072C67WDN
        * Rihappy deixa o código do SKU deles no HTML.
            * https://www.rihappy.com.br/dino-papa-tudo-elka/p
            * Código: 100127502
* product
    * **Descrição**: Código usado pelo marketplace para representar aquela familia de SKUs.
* name
    * **Descrição**: Nome do SKU.
* brand
    * **Descrição**: Marca do SKU.
* description
    * **Descrição**: Descrição do SKU.
* gtin
    * **Descrição**: GTIN do SKU.
* ncm
    * **Descrição**: NCM do SKU.
* prices
    * **Descrição**: Preços do SKU, ou seja, pode possuir preço com e sem desconto.
* segments
    * **Descrição**: Segmentos do SKU, caminhando do segmento mais externo para o mais interno (mais específico).
* attributes
    * **Descrição**: Atributos do SKU, sem remoção de nenhum atributo que já esteja em outra categoria do SKU.
* measurement
    * **Descrição**: Quaisqueres medidas relacionadas ao SKU.
* package
    * **Descrição**: Quaisqueres medidas relacionadas ao SKU dentro do pacote.
* rating
    * **Descrição**: Avaliação do produto após ser convertida para números.
    * **Atenção**: Cada marketplace pode avaliar da maneira que desejar então é necessário converter para números para melhor conseguir avaliar no futuro. Não é preciso tratar zero como o minímo valor, pode usar número negativos para melhor representação.
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
* audios
    * **Descrição**: URLs de aúdios do SKU.
* images
    * **Descrição**: URLs de imagens do SKU.
* videos
    * **Descrição**: URLs de videos do SKU.
* variations
    * **Descrição**: URLs de variações do SKU.
* sources
    * **Descrição**: URLs visitados para formar esse SKU.
* links
    * **Descrição**: URLs para outros SKUs, pois dentro de uma página podemos descobrir outros SKUs para serem scrapeados.
* marketplace
    * **Descrição**: Nome do marketplace seguindo o padrão [snake_case](https://en.wikipedia.org/wiki/Snake_case).
* metadata
    [Dados que providência informações sobre os dados do SKU](https://en.wikipedia.org/wiki/Metadata).

# reference
["A norma diz que as medidas devem ser colocadas na ordem: comprimento x largura x altura (ou profundidade)."](https://www.diferenca.com/comprimento-largura-e-altura/#:~:text=A%20norma%20diz%20que%20as,x%20altura%20(ou%20profundidade).)
