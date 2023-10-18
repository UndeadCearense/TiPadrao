# TiPadrao
Codes that i use daily at work, it involves routine automatizations with Selenium, PyAutoGui and other Python libraries


#Registro catraca:
This one i use to extract from IDSecure/ControliD system the students logfile record of the ticket gate, since the attedance control here its based on this mechanism, first the selenium access the server software trough the web navigator(Edge), 
them it get the raw log and pick only the first entry and the last exit of each student, after that converts it into a txt and its ready to upload to the attendance record system.

Esse serve para extrair o relatório de acessos das catracas do sistema do IDSecure/ControliD, o acesso do software é feito através de um endereço de ip, o controle de frequência dos alunos é feito através disso.
O selenium acessa o software e extrai o relatório bruto, depois disso ele escolhe apenas a primeira entrada e a última saída de cada aluno, depois converte em um txt e está pronto para carregar no sistema de registro de presença

#TemplateNotas:
This one i created to open the template student grade scores at Sponte Educacional system, was used to be a really repetitive task that took almost a week to finish it, since this one use most of selenium sources,
you cant just run it on background and go do other tasks at your job, now just took around 1 or 2 days to get this done.

Eu criei essa automatização para abrir os templates dos boletins das turmas no sistema Sponte Educacional, como são várias turmas o processo é repetitivo e isso me tomava quase uma semana de trabalho, 
agora como a automatização é feita através do selenium, eu deixo rodando em segundo plano e vou fazer minhas outras funções, leva no máximo 2 dias para acabar de abrir tudo.
