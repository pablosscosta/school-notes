# 📘 Documento de Visão – School Notes

## 1. Nome do Projeto

**School Notes**

---

## 2. Descrição Geral

O School Notes é um sistema web para lançamento e consulta de notas escolares.\
Ele permite que professores registrem as notas de seus alunos em disciplinas específicas, organizadas por turma, e que secretários acompanhem o desempenho acadêmico.

---

## 3. Objetivo

Criar uma aplicação fullstack com backend em Django + DRF e frontend em React, permitindo o gerenciamento de alunos, turmas, disciplinas e lançamento de notas, com controle de acesso por perfil de usuário.

---

## 4. Atores do Sistema

- **Professor**: pode lançar e editar notas apenas das disciplinas que leciona.
- **Secretário**: pode visualizar todos os dados (alunos, notas, disciplinas, turmas).
- **(Futuramente)** Aluno: pode visualizar apenas suas notas.

---

## 5. Funcionalidades (MVP)

- Autenticação de usuário (login/logout)
- CRUD de:
  - Alunos
  - Disciplinas
  - Turmas
  - Notas
- Associação de:
  - Aluno → Turma
  - Disciplina → Professor
  - Nota → (Aluno + Disciplina)
- Permissões baseadas no tipo de usuário

---

## 6. Regras de Negócio

- Professores só podem lançar notas em disciplinas em que estão vinculados.
- Cada nota pertence a um único aluno e uma única disciplina.
- Secretários não podem alterar dados, apenas visualizar.

---

## 7. Tecnologias

- **Backend**: Django + Django REST Framework
- **Banco de Dados**: SQLite (para desenvolvimento local)
- **Frontend**: React.js
- **Autenticação**: Django Token Auth (ou JWT, a definir)

---

## 8. Futuras Extensões (fora do MVP)

- Cadastro de usuários via frontend
- Notificações por e-mail
- Exportação de boletins
- Interface para alunos
