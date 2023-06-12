//pagenation

function addEventListener(pgnbar, pgn, i) {
  let obj = document.createElement("div");
  obj.classList.add("pgbtn");
  obj.setAttribute("page", i);
  obj.textContent = i;
  if (i == pgn) {
    obj.style.textDecoration = "underline";
  }
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

function addMovingEventListener(pgnbar, i, value) {
  let obj = document.createElement("div");
  obj.classList.add("pgbtn");
  obj.setAttribute("page", i);
  if (value == 1) {
    obj.textContent = ">>";
  } else if (value == 0) {
    obj.textContent = "<<";
  }
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

  if (totalpage <= 10) {
    for (let i = 1; i <= totalpage; i++) {
      addEventListener(pgnbar, pgn, i);
    }
  } else if (totalpage > 10 && pgn <= 10) {
    for (let i = 1; i <= 10; i++) {
      addEventListener(pgnbar, pgn, i);
    }
    addMovingEventListener(pgnbar, 11, 1);
  } else if (totalpage > 10 && pgn > 10) {
    let start = Math.floor(pgn / 10) * 10;
    addMovingEventListener(pgnbar, start, 0);
    for (let i = start + 1; i < Math.min(start + 11, totalpage); i++) {
      addEventListener(pgnbar, pgn, i);
    }
    if (totalpage > start + 11) {
      addMovingEventListener(pgnbar, start + 11, 1);
    }
  }
}

/* changepage 함수 부분 */

function goDetail(i) {
  var form = document.getElementById(i);
  form.submit();
}

function pageChange(i) {
  var form = document.getElementById(`pageChangeform_${i}`);
  form.submit();
}
