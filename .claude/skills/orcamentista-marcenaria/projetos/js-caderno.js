
  const encolhe = (caixa, alvo, piso) => {
    const f = caixa.querySelector(alvo); if (!f) return;
    f.style.zoom = 1;
    const cs = getComputedStyle(caixa);
    const alt = caixa.clientHeight - parseFloat(cs.paddingTop)
                                   - parseFloat(cs.paddingBottom);
    const pede = f.scrollHeight;
    if (pede > alt) f.style.zoom = Math.max(piso, alt / pede);
  };
  const MM = 96 / 25.4;
  const sobra = (low, f) => {
    const cs = getComputedStyle(low);
    return low.clientHeight - parseFloat(cs.paddingTop)
                            - parseFloat(cs.paddingBottom) - f.scrollHeight;
  };
  // ⭐ quem cede é a FOTO, não o corpo do texto: o caderno tem de ter um
  //   tamanho de letra só, e a faixa é que desce até a lista caber.
  const caberBanda = (w) => {
    const band = w.querySelector('.band'), low = w.querySelector('.low'),
          f = low && low.querySelector('.fitw');
    if (!band || !f) return;
    f.style.zoom = 1;
    const piso = 62 * MM;
    for (let i = 0; i < 30; i++) {
      const s = sobra(low, f);
      if (s >= 0) break;
      const h = band.getBoundingClientRect().height;
      if (h <= piso) break;
      band.style.height = Math.max(piso, h + s - 1) + 'px';
    }
    // ⛔ E SE NEM COM OS DOIS COUBER, A FAIXA CEDE O RESTO. Sem este
    //   terceiro passo o bloco estourava o padding e o `overflow:hidden`
    //   o cortava só na borda da folha — a barrinha do bloco de
    //   acabamentos saía por baixo do fio do rodapé, 1,6 mm de sujeira
    //   que só aparece com lupa e que eu já tinha dado por resolvida uma
    //   vez sem medir.
    let s = sobra(low, f);
    if (s < 0) {
      f.style.zoom = Math.max(.90, (low.clientHeight + s) / low.clientHeight);
      const chao = 48 * MM;
      for (let i = 0; i < 30; i++) {
        s = sobra(low, f);
        if (s >= 0) break;
        const h = band.getBoundingClientRect().height;
        if (h <= chao) break;
        band.style.height = Math.max(chao, h + s - 1) + 'px';
      }
    }
  };
  const caber = () => {
    // ⛔ a coluna ENTREGA leva quatro etapas e transbordava a caixa: o
    //   `overflow:hidden` não resolvia, só cortava o fio divisor na borda
    //   da folha, 1,9mm por baixo do rodapé. Encolhe na origem.
    document.querySelectorAll('.proc').forEach(pr => {
      pr.style.zoom = 1;
      if (pr.scrollHeight > pr.clientHeight)
        pr.style.zoom = Math.max(.85, pr.clientHeight / pr.scrollHeight);
    });
    document.querySelectorAll('.amb-txt').forEach(c => encolhe(c, '.fit', .62));
    document.querySelectorAll('.pad.apertada').forEach(c => encolhe(c, '.fitp', .80));
    document.querySelectorAll('.ambw').forEach(caberBanda);
  };
caber();