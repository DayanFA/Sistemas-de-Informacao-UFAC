library(ggplot2)

pesoAntes <- c(185, 194, 213, 198, 244, 162, 211, 273, 178, 192, 181, 209)
pesoDepois <- c(168, 177, 196, 180, 229, 144, 197, 252, 161, 178, 161, 193)

analiseAmostras = function(amostraAntes, amostraDepois, alfa, delta) {
  cat("Resumo da amostra antes:", "\n")
  print(summary(amostraAntes))
  cat("\nResumo da amostra depois:", "\n")
  print(summary(amostraDepois))
  
  dados <- data.frame(
    Amostra = c(rep("Amostra Antes", length(amostraAntes)), rep("Amostra Depois", length(amostraDepois))),
    Valor = c(amostraAntes, amostraDepois)
  )
  
  cat("\nGráfico Box Plot das amostras impresso", "\n")
  print(ggplot(dados, aes(x = Amostra, y = Valor, fill = Amostra)) +
          geom_boxplot(color = "blue", width = 0.5) +
          labs(title = "Box Plot: Amostras Antes e Depois",
               y = "Valores") +
          theme_bw()
  )
  
  cat("\nFunção t.test:")
  print(t.test(x = amostraAntes, y = amostraDepois, alternative="two.sided", paired = TRUE, mu = delta, conf.level= (1 - alfa)))
  
  diferenca <- amostraAntes - amostraDepois
  n <- length(diferenca)
  d <- mean(diferenca)
  dp <- sd(diferenca)
  tcal <- (d - delta) / (dp / sqrt(n))
  rc <- qt(1 - alfa / 2, df = n - 1)
  
  cat("Tamanho da amostra:", n, "\n")
  cat("Média amostral:", d, "\n")
  cat("Desvio Padrão:", dp, "\n")
  cat("Tcal:", tcal, "\n")
  cat("Região de Aceitação: (", -rc, ",", rc, ")\n")
}
qt(0.05, df=11)

analiseAmostras(pesoAntes, pesoDepois, 0.10, 20)