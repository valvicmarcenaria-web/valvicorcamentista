# Operações no Google Drive

O Drive é o **arquivo vivo** da Valvic. A Helena mantém a ordem: estrutura previsível,
nomes claros, permissões certas. Regra de fundo: *o que é canônico fica no lugar canônico;
cópia solta é fonte de erro.*

## Estrutura padrão (árvore)
```
Valvic/
├── 01 · Clientes/
│   └── <Cliente> — <código do projeto>/
│       ├── Contrato/
│       ├── Projeto (SketchUp/Upmob/PDF)/
│       ├── Orçamento/
│       ├── Fotos/
│       └── Pós-venda/
├── 02 · Financeiro/            (restrito — sócios)
├── 03 · Fornecedores & Compras/
├── 04 · Equipe & RH/           (restrito — escopos, avaliações)
├── 05 · Institucional & Apresentações/   (apostila, Walton, patrimônio…)
├── 06 · Marketing & Portfólio/
└── 07 · Modelos & Templates/
```
- **Uma pasta por cliente**, criada **em até 24h** após o fechamento (Assistente Operacional).
- Subpastas fixas — todo cliente tem as mesmas; previsibilidade > criatividade.

## Nomenclatura
- Pastas de cliente: `Nome do Cliente — <código>` (o mesmo código do Calcme).
- Arquivos: `<Assunto>_<Cliente/Projeto>_<AAAA-MM>` · versão `-vN` quando relevante.
- **Proibido:** "final", "final2", "final_ok". A versão válida é a que está no lugar certo.

## Permissões & sigilo (o mais importante)
Classificar **antes** de compartilhar:
- **Restrito** (Financeiro, RH/folha, proposta ao investidor, contratos) → só sócios /
  destinatário nomeado. Nunca "qualquer pessoa com o link".
- **Interno** → equipe conforme necessidade (ex.: apostila para Deivson).
- **Externo** (proposta comercial, portfólio) → cliente/parceiro, link controlado.
- **Preferir compartilhar a pasta certa**, não o Drive inteiro; revisar acessos ao desligar
  colaborador ou encerrar parceria.
- Na dúvida sobre destinatário/nível → **perguntar antes de compartilhar** (dado que vaza
  não volta).

## Operações rotineiras
- **Onboarding de cliente:** criar a pasta padrão + subpastas + mover contrato/orçamento/projeto.
- **Higiene mensal:** revisar acessos, arquivar projetos concluídos em `Clientes/_Concluídos`,
  apagar duplicatas.
- **Modelos:** manter `07 · Modelos & Templates` com os documentos-base (ata, plano de ação,
  orçamento-modelo) — copiar de lá, nunca sobrescrever o mestre.
- **Backup do que importa:** os HTML/PDF institucionais vivem também no repositório (`painel/`);
  o Drive guarda a versão de circulação.

## Integração com o resto
- **Calcme** guarda o cadastro/pedido/marcos; o **Drive** guarda os arquivos (projeto, contrato,
  fotos). Um aponta para o outro — o código do projeto é a chave que liga os dois.
- Documentos gerados pela Helena (relatórios, apresentações) → pasta institucional + registro
  no `dados/mapa-documentos.md`.
