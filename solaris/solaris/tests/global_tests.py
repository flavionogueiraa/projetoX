# [RF001] Login no Sistema
# O sistema deve permitir que o usuário pré-cadastro efetue o
# login do sistema usando e-mail e senha.
# Fazer o teste do login e checar se o usuário tem o atributo
# is_authenticated como True

# [RF002] Redefinir Senha
# O sistema deve que o usuário redefina sua senha após o primeiro acesso ao sistema
# Não temos redefinição de senha, apenas recuperação de senha

# [RF003] Recuperar Senha
# O sistema deve permitir que o usuário insira o endereço de e-mail associado à sua conta
# para iniciar o processo de recuperação de senha.
# Usaremos teste caixa preta para testar isso? Acredito que sim.

# Não funcionais:
# [RNF001] Atividade de login
# O sistema de guardar a atividade de login dos usuários pela última vez de uso
# Ok, temos uns campos no admin para isso, podemos só tirar alguns prints.

# [RNF002] Logs do usuário
# O sistema deve registrar os logs do usuário.
# Ok, temos menus no admin para isso, podemos só tirar alguns prints.

# RNF005] Quantidade de usuário conectados
# O sistema deve suportar um número máximo de 100 usuários conectados simultaneamente.
# Talvez até consigamos logar 100 usuários, mas teremos que limitar o
# número máximo para 100? Meio estranho, não acham?
