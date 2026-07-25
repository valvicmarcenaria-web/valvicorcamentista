# Artefato — Dossiê Walton

Painel-índice cronológico dos documentos preparados para a conversa com o investidor.
Publicado como artefato privado em claude.ai.

**URL:** https://claude.ai/code/artifact/68479e40-30a3-4d7e-89d2-29ef01935f12

## Como atualizar

O painel embute os PDFs da pasta `painel/` como data URI — ou seja, ele carrega a
versão dos arquivos no momento em que é gerado. Sempre que um documento do Walton
for revisado:

1. Regerar o HTML (o script lê os PDFs e monta a página):
   ```
   cd painel/artefatos && python3 gerar-dossie-walton.py
   ```
   O script espera um `docs.json` ao lado, com a lista de documentos, os metadados
   (título, pergunta que responde, formato, datas, tags) e o PDF já em base64.

2. Republicar **o mesmo caminho de arquivo** para manter a mesma URL. Publicar um
   caminho diferente cria um artefato novo.

## Ordem

Os documentos aparecem do mais recente para o mais antigo — a ordem cronológica é
a própria estrutura da página (o trilho à esquerda). Ao acrescentar um documento
novo, ele entra no topo da lista em `docs.json`.

## Sigilo

O painel reúne material **restrito** (remuneração e posição financeira). O artefato
nasce privado; só é compartilhado se alguém usar o menu de compartilhamento da página.
