
   #하위페이지 시작
   <!DOCTYPE html>
<html>
<head>
  <title>하위 페이지 1</title>
</head>
<body>
  <h1>하위 페이지 1</h1>
  <p>.</p>
</body>
</html>


...
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <style>
    #info {
      display: none;
    }
  </style>
</head>
<body>
  <button onclick="showInfo()"></button>
  <div id="info"></div>

  <script>
    function showInfo() {
      var infoDiv = document.getElementById("info");
      if (infoDiv.style.display === "none") {
        infoDiv.style.display = "block";
      } else {
        infoDiv.style.display = "none"; 
      }
    }
  </script>
</body>
</html>
...
<div>
    <a href="#1">name</a>
</div>

<p id="1" style="margin-top:1500px;">name</p>


