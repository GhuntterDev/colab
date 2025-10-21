# 🔐 Sistema de Login - Avaliação de Colaboradores

## Visão Geral
O sistema de login foi implementado para controlar o acesso aos dados de avaliação de colaboradores, permitindo diferentes níveis de acesso baseados no tipo de usuário.

## Usuários Administrativos
**Acesso:** Todas as lojas

| Usuário | Senha | Descrição |
|---------|-------|-----------|
| GhtDev | 18111997 | Desenvolvedor principal |
| Monitoramento | Monitoramento | Usuário de monitoramento |

## Usuários de Loja
**Acesso:** Apenas à própria loja

| Usuário | Senha | Loja |
|---------|-------|------|
| Carioca | loja123 | Carioca |
| Santa Cruz | loja123 | Santa Cruz |
| Mesquita | loja123 | Mesquita |
| Nilópolis | loja123 | Nilópolis |
| Madureira | loja123 | Madureira |
| Bonsucesso | loja123 | Bonsucesso |
| Taboão | loja123 | Taboão |
| São Bernardo | loja123 | São Bernardo |
| Santo André | loja123 | Santo André |
| Mauá | loja123 | Mauá |
| MDC São Mateus | loja123 | MDC São Mateus |
| CDM São Mateus | loja123 | CDM São Mateus |

## Funcionalidades

### 🔒 Autenticação
- **Hash de senhas:** Utiliza bcrypt para segurança
- **Sessão persistente:** Login mantido durante a navegação
- **Logout:** Botão de sair na sidebar

### 👥 Controle de Acesso
- **Administradores:** Veem dados de todas as lojas
- **Usuários de loja:** Veem apenas dados da própria loja
- **Filtros automáticos:** Dados são filtrados automaticamente baseado no usuário

### 🛡️ Segurança
- Senhas são armazenadas como hash bcrypt
- Verificação de autenticação em todas as páginas
- Redirecionamento automático para login se não autenticado

## Como Usar

1. **Acesse o aplicativo**
2. **Faça login** com um dos usuários listados acima
3. **Navegue** pelos dados (filtrados automaticamente)
4. **Faça logout** usando o botão na sidebar

## Arquivos do Sistema

- `auth.py` - Sistema de autenticação
- `colab.py` - Aplicação principal (atualizada)
- `requirements.txt` - Dependências (inclui bcrypt)

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
streamlit run colab.py
```

## Notas de Segurança

- As senhas são armazenadas como hash bcrypt
- Cada hash é único (mesmo para senhas iguais)
- Não é possível recuperar a senha original do hash
- Para alterar senhas, gere novos hashes usando bcrypt
