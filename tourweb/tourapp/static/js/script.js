const parentDivs = document.querySelectorAll(".span1");

parentDivs.forEach((parentDiv) => {
  const hiddenDiv = parentDiv.querySelector(".bcat1");
  const mcats = hiddenDiv.querySelectorAll(".mcat");

  parentDiv.addEventListener("mouseover", function () {
    hiddenDiv.style.display = "block";
  });

  parentDiv.addEventListener("mouseleave", function () {
    hiddenDiv.style.color = "black";
    hiddenDiv.style.display = "none";
    mcats.forEach((mcat) => {
      mcat.style.display = "none";
    });
  });

  hiddenDiv.addEventListener("click", function () {
    hiddenDiv.style.color = "white";
    mcats.forEach((mcat) => {
      mcat.style.display = "block";
    });
  });
});

window.addEventListener("load", function () {
  var logo = this.document.getElementById("logo");
  logo.classList.add("logo_visible");
});

//pagenation

let totalpage = Math.ceil(parseInt(data.response.body.numOfRows) / 12);

const pgnbar = document.getElementsById(".btnlist");
for (i = 1; i <= 2; i++) {
  totalpage.innerHTML();
}
