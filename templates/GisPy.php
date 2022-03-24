<!DOCTYPE html>
<!-- Created by CodingLab |www.youtube.com/CodingLabYT-->
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8">
    <title> GiS Analytics </title>
    <link rel="stylesheet" href="index.css">
    <!-- <script src="myscripts.js"></script> -->
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
   </head>
<body onload="rgbOrMulti()">
<!-- Javascript for tabs -->
<script type="text/javascript">


function rgbOrMulti() {
   if ((document.getElementById("redBand").files.length) != 0 && (document.getElementById("greenBand").files.length) != 0 && (document.getElementById("blueBand").files.length) != 0) {
     document.getElementById("selecDiv").style.visibility = "visible";
   } else if((document.getElementById("redtif").files.length) != 0 && (document.getElementById("greentif").files.length) != 0 && (document.getElementById("bluetif").files.length) != 0) {
     document.getElementById("selecDiv").style.visibility = "visible";
   } else{
     document.getElementById("selecDiv").style.visibility = "hidden";
   }
}

function openMap(evt, GisChoice) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace("active", "");
  }
  document.getElementById(GisChoice).style.display = "block";
  evt.currentTarget.className += "active";
}
</script>
<!-- css code for tabs file -->
<style>
body {font-family: Arial;}

/* Style the tab */
.tab {
  overflow: hidden;
  border: 1px solid #ccc;
  width:inherit; 
  text-align: center;
  background-color:lightgreen;
}

/* Style the buttons inside the tab */
.tab button {
  background-color: inherit;
  float: inherit;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
  font-size: 17px;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: greenyellow;
}

/* Create an active/current tablink class */
.tab button.active {
  background-color:darkseagreen;
}

/* Style the tab content */
.tabcontent {
  display: none;
  padding: 6px 12px;
  -webkit-animation: fadeEffect 1s;
  animation: fadeEffect 1s;
}

/* Fade in tabs */
@-webkit-keyframes fadeEffect {
  from {opacity: 0;}
  to {opacity: 1;}
}

@keyframes fadeEffect {
  from {opacity: 0;}
  to {opacity: 1;}
}
fieldset{
  overflow: hidden;
  border: 1px solid #ccc;
  width:inherit; 
  display:inline
}
legend {
    background-color: #000;
    color: #fff;
    padding: 3px 6px;
}
</style>

  <section class="nav">
    <?php
    include 'nav.php';
    ?> 
  </section>
<section class="home-section container">
<div class="text">GiS Analytics</div>
<div class="home-section">
      
<div class="tab" >
  <button class="tablinks" onclick="openMap(event, 'RGB')">RGB</button>
  <button class="tablinks" onclick="openMap(event, 'Multi-Spectral')">Multi-Spectral</button>
</div>
<!-- file selection -->
<div id="RGB" class="tabcontent">
<h3>R G B Camera</h3>
<div style="padding: 14px 16px;">
<form>
<p>Red tif</p>
<input type="file" name="RedBand" accept=".tif" id="redBand" onchange="rgbOrMulti();"/>
</form>
<form>
<p>Green tif</p>
<input type="file" name="GreenBand" accept=".tif" id="greenBand" onchange="rgbOrMulti();"/>
</form>
<form>
<p>Blue tif</p>
<input type="file" name="BlueBand" accept=".tif" id="blueBand" onchange="rgbOrMulti();"/>     
</div>
</div>

<div id="Multi-Spectral" class="tabcontent">
<h3>Multi-Spectral</h3>
<div style="padding: 14px 16px;">
<form>
<p>Red tif</p>
<input type="file"  name="RedTif" accept=".tif" id="redtif">
</form>
<form>
  <p>Green tif</p>
  <input type="file"  name="GreenTif" accept=".tif" id="greentif">
</form>
<form>
  <p>Blue tif</p>
   <input type="file" name="BlueTif" accept=".tif" id="bluetif">
</form>
<form>
  <p>Red Edges</p>
  <input type="file"  name="RedEdgeTif" accept=".tif" id="redEdgetif">
</form>
<form>
  <p>Near Infrared </p>
  <input type="file" name="NIRTif" accept=".tif" id="NIRtif">
</form>
</div>
</div>

<!-- pop out selection -->
<div id="selecDiv">
<fieldset>
  <legend>Option Selection</legend>
  <br>
<fieldset>
  <legend>Indices Option</legend>
<input type="checkbox" id="NDRE" name="indices" value="NDRE">
  <label for="NDRE"> NDRE</label>
  <input type="checkbox" id="NDVI" name="indices" value="NDVI">
  <label for="NDVI"> NDVI</label>
  <input type="checkbox" id="GLF" name="indices" value="GLF">
  <label for="GLF"> GLF</label>
  <input type="checkbox" id="OSVI" name="indices" value="OSVI">
  <label for="OSVI"> OSVI</label>
  <input type="checkbox" id="SAVA" name="indices" value="SAVA">
  <label for="SAVA"> SAVA</label>
</fieldset>
<br><br>
<p>Upload Vector in file:</p>
<select id="vectors">
  <option value="KML">.KML</option>
  <option value="KMZ">.KMZ</option>
  <option value="gison">.gison</option>
  <option value="shape">.shape</option>
  <option value="geopackage">.geopackage</option>
</select>
<br><br>
<fieldset>
  <legend>Output</legend>
<input type="checkbox" id="Raster" name="output" value="Raster">
  <label for="Raster"> Raster</label>
  <input type="checkbox" id="Dipped" name="output" value="Dipped">
  <label for="Dipped"> Dipped Raster</label>
  <input type="checkbox" id="test3" name="output" value="test3">
  <label for="test3"> test3</label>
  <input type="checkbox" id="test4" name="output" value="test4">
  <label for="test4"> test4</label>
  <input type="checkbox" id="test5" name="output" value="test5">
  <label for="test5"> test5</label>
</fieldset>
<br>
<input type="submit" value="Done"></submit>
</fieldset>

</div>  
</section>
</body>
</html>
