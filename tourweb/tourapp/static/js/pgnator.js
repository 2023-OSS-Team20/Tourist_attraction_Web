//pagenation

function addEventListener(pgnbar, i) {
  let obj = document.createElement("div");
  obj.classList.add("pgbtn");
  obj.setAttribute("page", i);
  obj.textContent = i;
  obj.setAttribute("onclick", `pageChange(${i})`);
  var url = "/pageChange/";

  // GET 요청을 보내기 위한 form 생성
  var form = document.createElement("form");
  form.setAttribute("method", "GET");
  form.setAttribute("action", url);
  form.setAttribute("id", `pageChangeform_${i}`);

  // hidden 태그 생성 및 id 값을 전달
  var input = document.createElement("input");
  input.setAttribute("type", "hidden");
  input.setAttribute("name", "pnum");
  input.setAttribute("value", i); // div 태그의 id 값을 hidden 태그의 value로 전달
  form.appendChild(input);

  obj.appendChild(form);
  pgnbar.appendChild(obj);
}

function pgnator(tc, pgn) {
  const totalpage = Math.ceil(tc / 12);
  const pgnbar = document.getElementById("btnlist");

  if (totalpage < 10) {
    for (let i = 1; i <= totalpage; i++) {
      addEventListener(pgnbar, i);
    }
  } else if (totalpage >= 10 && pgn < 10) {
    for (let i = 1; i <= 9; i++) {
      addEventListener(pgnbar, i);
    }
  } else {
    let start = Math.floor(pgn / 10) * 10;
    for (let i = start; i < start + 10; i++) {
      addEventListener(pgnbar, i);
    }
  }
}

/* changepage 함수 부분 */

function goDetail() {
  var form = document.getElementById("form");
  form.submit();
}

function pageChange(i) {
  var form = document.getElementById(`pageChangeform_${i}`);
  form.submit();
}
