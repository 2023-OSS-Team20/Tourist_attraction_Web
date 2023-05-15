// 모든 부모 div 요소를 선택합니다.
const parentDivs = document.querySelectorAll(".span1");

parentDivs.forEach(parentDiv => {
  const hiddenDiv = parentDiv.querySelector(".bcat1");

  parentDiv.addEventListener("mouseover", function() {
    hiddenDiv.style.display = "block";
    parantDiv.style.opacity = "0,5";
  });

  parentDiv.addEventListener("mouseout", function() {
    hiddenDiv.style.display = "none";
    parantDiv.style.opacity = "1"; 
  });
});
