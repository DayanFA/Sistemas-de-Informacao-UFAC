# Instalar o pacote ggplot2
install.packages("ggplot2")

# Carregar pacote necessário
library(ggplot2)

# a) Inicialmente gere um conjunto de dados proveniente de uma população normal
# com média e desvio padrão especificado. [Considere inicialmente um valor médio
# populacional de 100, desvio padrão de 10 e tamanho da amostra de 20];

media_populacional <- 100
desvio_padrao <- 10
tamanho_amostra <- 20
dados <- rnorm(tamanho_amostra, media_populacional, desvio_padrao)

# b) Faça um box plot usando o pacote ggplot2 de modo que neste a média esteja
# destacada;

ggplot() +
  geom_boxplot(aes(y=dados), width=0.5) +
  geom_point(aes(x=1, y=mean(dados)), color="red", size=4) +
  theme_minimal()

# c)  Utilize função específica para soltar os resumos numéricos que forneçam: média,
# desvio padrão, mínimo, máximo e os quartis.

resumo <- summary(dados)
cat("Média: ", mean(dados), "\n")
cat("Desvio padrão: ", sd(dados), "\n")
cat("Mínimo: ", resumo[1], "\n")
cat("Máximo: ", resumo[6], "\n")
cat("Quartis: ", resumo[2:5], "\n")

# # d) Na sequência, faça uma function que a partir de um conjunto de dados e um nível
# de confiança especificado, forneça as estimativas pontuais e construa um IC para
# cada um dos seguintes parâmetros populacionais: média, variância e desvio padrão
# [suponha que não se conheça nenhum dos parâmetros populacionais]. Esta função
# deve ter como saída um texto explicativo indicando qual o resultado de cada
# intervalo. Por exemplo: “A estimativa pontual para a média é ...”; “ O IC para a média
# a Gama% é ....”.

estimativas_e_ic <- function(dados, confianca) {
  media <- mean(dados)
  variancia <- var(dados)
  desvio_padrao <- sd(dados)
  
  erro_padrao <- desvio_padrao / sqrt(length(dados))
  z <- qnorm((1 + confianca) / 2)
  ic_media <- c(media - z * erro_padrao, media + z * erro_padrao)
  
  n <- length(dados)
  ic_variancia <- c((n - 1) * variancia / qchisq((1 + confianca) / 2, df=n-1),
                    (n - 1) * variancia / qchisq((1 - confianca) / 2, df=n-1))
  
  ic_desvio_padrao <- sqrt(ic_variancia)
  
  cat("A estimativa pontual para a média é ", media, "\n")
  cat("O IC para a média a ", confianca * 100, "% é ", ic_media, "\n")
  cat("A estimativa pontual para a variância é ", variancia, "\n")
  cat("O IC para a variância a ", confianca * 100, "% é ", ic_variancia, "\n")
  cat("A estimativa pontual para o desvio padrão é ", desvio_padrao, "\n")
  cat("O IC para o desvio padrão a ", confianca * 100, "% é ", ic_desvio_padrao, "\n")
}

# Usar a função para um nível de confiança de 95%
estimativas_e_ic(dados, 0.95)

