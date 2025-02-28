# Monitorador de atividade

Feito para expor o progresso do meu trabalho no meu site de portfólio: https://fe-fe.github.io/activity.

Script que verifica dados da janela em foco do Windows para extrair palavras-chave, como nome de ferramentas, tecnologias, etc., salva o tempo dedicado ao tema e estrutura esses dados em JSON.

Também permite que o JSON gerado seja convertido para uma variável JavaScript, para que os dados possam ser utilizados sem a necessidade de banco de dados ou aplicação backend (ex.: GitHub Pages).

A busca é feita procurando por tags de uma ou várias palavras (ex.: "Python" ou "Stack Overflow") dentro do título da página que está atualmente em uso, sendo possível adicionar novas tags ao programa atravéz das variáveis "tags" e "multiTags".

---

![pasta do projeto](README/screenshot.png)
