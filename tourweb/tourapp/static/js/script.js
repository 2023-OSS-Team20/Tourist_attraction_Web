// 모든 부모 div 요소를 선택합니다.
const parentDivs = document.querySelectorAll(".span1");
const bcatTag = document.querySelectorAll(".bact1");

parentDivs.forEach(parentDiv => {
  const hiddenDiv = parentDiv.querySelector(".bcat1");

  parentDiv.addEventListener("mouseover", function() {
    hiddenDiv.style.display = "block";
  });

  parentDiv.addEventListener("mouseout", function() {
    hiddenDiv.style.display = "none";
  });
});

bcatTag.forEach(bcat => {
  const mcat = bact.querySelector(".bcat");

  bact.addEventListener("click", function() {
    mcat.style.display = "block";
  });
  bcat.addEventListener("mouseout", function() {
    mcat.style.display = "none";
  });
});