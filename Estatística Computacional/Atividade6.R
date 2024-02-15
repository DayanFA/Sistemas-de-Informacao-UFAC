conjunto1 <- c(8.7, 9.8, 10, 9.6, 8.5, 5.8, 6.3, 12.5, 8.8, 7.3, 12.5, 13.8, 4.8, 6.7, 8.3, 9.5, 10.5, 12.5, 12.5, 9.0, 14, 13, 9.5, 8)
conjunto2 <- c(9.3, 9.2, 9.5, 9.6, 8.8, 6.5, 7, 11.5, 8.9, 8, 11, 14, 5.5, 6.8, 8.5, 9, 10, 13, 12, 10, 12, 11, 10.5, 9.3)

origemPopulacao = function(amostra1, amostra2) {
  m = length(amostra1)
  n = length(amostra2)
  
  mediaX = mean(amostra1)
  mediaY = mean(amostra2)
  
  var1 = var(amostra1)
  var2 = var(amostra2)
  
  delta = 0
  tcal = ((mediaX-mediaY) - delta) / (sqrt(var1/m + var2/n))
  
  aux1 = (var1/m)
  aux2 = (var2/n)
  numerador = (aux1 + aux2)^2
  denominador = (((aux1^2)/(m-1)) + ((aux2^2)/(n-1)))
  gl = numerador / denominador
  
  p_valor = 2 * pt(abs(tcal), gl, lower.tail = FALSE)
  
  nivel_significancia = 0.05
  regiao_critica = qt(1 - nivel_significancia/2, gl)
  
  if (abs(tcal) > regiao_critica) {
    conclusao = "Rejeita-se H0, pois tcal está na região crítica."
  } else {
    conclusao = "Não há evidência estatística para rejeição de H0, portanto."
  }
  
  cat("Valor calculado de t:", tcal, "\n")
  cat("Graus de liberdade:", round(gl), "\n")
  cat("Valor p calculado:", p_valor, "\n")
  cat("Região Crítica:", c(-regiao_critica, regiao_critica), "\n")
  cat("Conclusão:", conclusao, "\n")
}

origemPopulacao(conjunto1, conjunto2)

resultadoTeste <- t.test(conjunto1, conjunto2, alternative = "two.sided")
print(resultadoTeste)