# Projeto Flask com testes no GitHub Actions

Este projeto foi adaptado do codigo enviado, sem alterar a logica de `app.py`.
O arquivo `.venv` foi removido do pacote: o GitHub Actions instala as dependencias
usando `requirements.txt` em cada execucao.

## O que sera testado

- Resposta HTTP 200 no endpoint `GET /`.
- Existencia das duas tarefas e seu conteudo.
- Resposta no formato JSON.
- Verificacao de sintaxe Python.

## Quando os testes rodam

- A cada envio (`push`) de codigo.
- Ao abrir ou atualizar um Pull Request.
- Manualmente pela aba **Actions** (botao **Run workflow**).
- Automaticamente a cada 6 horas: cron `17 */6 * * *` em UTC
  (aproximadamente 21h17, 03h17, 09h17 e 15h17 em Fortaleza/Sao Luis).

> Execucoes agendadas podem sofrer atrasos. O agendamento so funciona na
> branch padrao do repositorio (como `main`) e nao deixa o servidor ligado.

## Como publicar

1. Crie um repositorio no GitHub.
2. Extraia o ZIP recebido.
3. Envie **o conteudo da pasta** ao repositorio (nao envie apenas o ZIP).
4. Confirme que `.github/workflows/testes.yml` existe na raiz do repositorio,
   no mesmo nivel de `app.py` e `requirements.txt`.
5. Abra **Actions -> Testes automaticos do Flask -> Run workflow** para testar.
6. Clique na execucao para consultar os logs e baixar o artefato
   `resultado-dos-testes` (relatorio XML de testes).

## Testes locais

```sh
python -m pip install -r requirements.txt
python -m pytest -v
```

## Rodar o servidor localmente

```sh
python app.py
```

Acesse `http://localhost:5000/`. Esse comando executa o Flask no ambiente
onde o comando foi iniciado; o GitHub Actions nao e um servico de hospedagem.
