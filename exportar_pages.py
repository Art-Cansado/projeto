from pathlib import Path

from app import app


def exportar_pagina():
    with app.test_client() as client:
        resposta = client.get("/tarefas")

    if resposta.status_code != 200:
        raise RuntimeError(f"Falha ao exportar a página: HTTP {resposta.status_code}")

    pasta = Path("site")
    pasta.mkdir(exist_ok=True)
    (pasta / "index.html").write_bytes(resposta.data)


if __name__ == "__main__":
    exportar_pagina()
