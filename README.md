# 📝 School Notes

Sistema web para lançamento e consulta de notas escolares.

Este projeto tem como objetivo praticar o desenvolvimento fullstack com Django + Django REST Framework no backend e React no frontend, aplicando boas práticas, autenticação com JWT e controle de acesso baseado em perfis.

---

## 🔧 Tecnologias

- Python 3.10+
- Django
- Django REST Framework
- SimpleJWT
- React.js (frontend em desenvolvimento)

---

## 📚 Funcionalidades (MVP)

- Autenticação JWT
- CRUD de:
  - Alunos
  - Disciplinas
  - Turmas
  - Notas
- Perfis de usuário:
  - **Professor**: pode lançar e editar notas apenas das disciplinas que ministra
  - **Secretário**: pode visualizar todos os dados

---

## 🚀 Estrutura atual

- `core/`: app principal com subpastas para organização (models, views, serializers, urls)
- `school_notes/`: configurações do projeto Django
- `venv/`: ambiente virtual (não incluído no repositório)
- `Documento de Visão – school-notes.md`: especificação inicial do projeto

---

## ✅ Status

- [x] Estrutura inicial criada
- [x] DRF e JWT instalados
- [x] Documento de Visão concluído
- [ ] Modelos e rotas em desenvolvimento

---

## 📌 Objetivo educacional

Este projeto tem fins de estudo e prática, com foco em APIs REST, autenticação, organização de código e integração backend + frontend. Todo o código segue convenções modernas para projetos Django.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
