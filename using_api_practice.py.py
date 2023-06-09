* {
  margin: 0;       // 여백설정
  padding: 0;
}

header {            // 해더 스타일
  height: 50px;  
  position: relative;   // 상대적 위치설정
  top: 0;
  opacity: 0.8;    // 투명도 
  backdrop-filter: blur(30px);  // 흐리게
  background-color: blue;
  padding-left: 32px;    
  padding-right: 32px;
  display: flex;       // 좌우정렬
  justify-content: space-between;
  align-items: center;
  color: black;
}

header > a {    
  color: wheat;
}
a {
  text-decoration: none;  // 밑줄 x 
}
ul {
  list-style-type: none;   // 
  padding: 0;
}

li {
  display: inline-block;
  margin-left: 16px;
  font-size: 18px;
  font-weight: bold;
}

.info {
  height: 15vh;
}
.itemDiv {
  height: 140px;
  width: 200px;
  margin: 10px;
  position: relative;
  display: inline-block;
  border: 1px solid burlywood;
  font-size: 15px;
  text-align: center;
  border-radius: 5px;
  cursor: pointer;
}

.itemDiv:hover {
  box-shadow: 1px 1px 3px 1px skyblue;
}

.itemDiv:hover > .listTitle {
  text-decoration: underline;
}

.imgwrap {
  position: relative;
  width: 100%;
  height: 100px;
}

img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100px;
}

.listTitle {
  margin: 0 auto;
  width: 120px;
  height: auto;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-top: 8px;
}

.listwrap {
  width: 905px;
  margin: 0 auto;
}

.infowrapper > .dummy {
  display: inline-block;
  height: 15vh;
}

.infowrapper {
  text-align: center;
  margin-top: 30px;
}

.infoNumber {
  text-align: center;
}

.search {
  margin-top: 5vh;
}

.body {
  background-image: url("../image/bg1.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

.btnBack {
  width: 50px;
  height: 50px;
  background-color: red;
  cursor: pointer;
}

.btnBack:hover {
  background-color: #fff;
}

.btnlist {
  display: flex;
  justify-content: center;
}

.pgbtn {
  text-align: center;
  font-size: 24px;
  /*display*/
  position: relative;
  margin-left: 5px;
  margin-right: 5px;
  width: 35px;
  height: 35px;
  line-height: 35px;
  display: inline-block;
  cursor: pointer;
}

.pgbtn:hover {
  transform: translateY(-2px);
}


