Animação da Epicicloide com Controle de Velocidade

Este código, desenvolvido em Python utilizando as bibliotecas NumPy e Matplotlib, tem como objetivo criar uma animação interativa da curva epicicloide, aplicada no contexto do Teorema de Green.

A epicicloide é a trajetória de um ponto em uma circunferência menor que rola externamente sobre uma circunferência maior. A animação ilustra de forma clara como essa curva é formada, permitindo ao usuário observar a movimentação da circunferência menor, seu centro, e o ponto gerador da curva.

🔧 Funcionalidades do Código
Plotagem da circunferência maior: Representada com um raio fixo de 4 e estilo pontilhado branco.

Animação da circunferência menor: Com raio 1, que se desloca ao redor da maior, rotacionando enquanto rola.

Traçado dinâmico da epicicloide: O ponto gerador é destacado e seu caminho vai sendo desenhado ao longo do tempo.

Interface estilizada: Fundo escuro com elementos destacados em branco, verde e ciano, proporcionando boa visualização e contraste.

Controle de velocidade: Através de um slider interativo, o usuário pode aumentar ou diminuir a velocidade da animação em tempo real.

🚀 Componentes Visuais
Circunferência maior: Linha branca pontilhada.

Circunferência menor: Linha verde semi-transparente.

Centro da menor circunferência: Marcado com um ponto verde.

Ponto gerador da epicicloide: Destacado com um ponto branco.

Linha da epicicloide: Traçada em azul ciano.

🎛️ Interatividade
O slider controla o parâmetro de intervalo da animação (em milissegundos).

Quanto maior o valor do slider, mais lenta a animação; quanto menor, mais rápida.

📜 Aplicações
Demonstração visual de conceitos matemáticos como:

Teorema de Green, relacionado ao cálculo de áreas através de integrais de linha.

Entendimento prático de curvas paramétricas e movimentos compostos.

Ferramenta didática para ensino de geometria analítica, cálculo vetorial e física.
