//pagenation

function pgnator(tc, pgn) {
  const totalpage = Math.ceil(tc / 12);
  const pgnbar = document.getElementById("btnlist");

  if (totalpage < 10) {
    for (let i = 1; i <= totalpage; i++) {
      let obj = document.createElement("div");
      obj.classList.add("pgbtn");
      obj.setAttribute("page", i);
      obj.textContent = i;
      pgnbar.appendChild(obj);
    }
  }
}
