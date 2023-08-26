export default function tableBasicSearch() {
  const attr = "js-table-search";
  const els = document.querySelectorAll(`[${attr}]`);
  const url = new URL(window.location);
  let filtersOBJ = GLOBAL.splitFilters(url.search);
  // console.log(attr, filtersOBJ)

  if (!els.length) return;

  els.forEach((i) => {
    const wrapper = i.closest(".input-container");
    const btn = wrapper.querySelector("button");
    const btnClear = wrapper.querySelector("svg");

    btnClear.addEventListener("click", () => {
      //não limpa a ordem de listagem com botao (x) em input de busca
      if (filtersOBJ.order) {
        filtersOBJ = {
          order: filtersOBJ.order,
        };
      } else {
        filtersOBJ = {};
      }

      const newFilters = GLOBAL.generateStringFilterFromObject(filtersOBJ);
      window.location.href = `${url.origin}${url.pathname}${newFilters}`;
    });

    btn.addEventListener("click", search(i));
    i.addEventListener("keyup", (e) => {
      if (e.keyCode === 13) {
        e.preventDefault();
        btn.click();
      }
      showBtnClearFilter(i, btnClear);
    });
  });

  function search(input) {
    return (e) => {
      const target = e.currentTarget;
      const btnClear = input.nextElementSibling;

      showBtnClearFilter(input, btnClear);

      if (filtersOBJ) {
        filtersOBJ["filter"] = input.value;
      } else {
        filtersOBJ = {};
        filtersOBJ["filter"] = input.value;
      }
      const { page, ...rest } = filtersOBJ;
      filtersOBJ = rest;
      const newFilters = GLOBAL.generateStringFilterFromObject(filtersOBJ);
      window.location.href = `${url.origin}${url.pathname}${newFilters}`;
    };
  }

  function showBtnClearFilter(input, btn) {
    if (input.value != "") {
      btn.classList.remove("hidden");
    } else {
      btn.classList.add("hidden");
    }
  }
}
