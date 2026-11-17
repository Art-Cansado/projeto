from app import app


def test_pagina_de_tarefas_exibe_os_dados_da_api():
    with app.test_client() as client:
        tarefas = client.get("/").get_json()
        pagina = client.get("/tarefas")

    assert pagina.status_code == 200
    assert pagina.mimetype == "text/html"

    html = pagina.get_data(as_text=True)
    for tarefa in tarefas:
        assert tarefa["title"] in html
        assert f'type="checkbox" value="{tarefa["id"]}"' in html
