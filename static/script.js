 // Import missing functions
function getVals(){
    // Get slider values
    var parent = this.parentNode;
    var slides = parent.getElementsByTagName("input");
      var slide1 = parseFloat( slides[0].value );
      var slide2 = parseFloat( slides[1].value );
      console.log(slide1 + " " + slide2);
    // Neither slider will clip the other, so make sure we determine which is larger
    if( slide1 > slide2 ){ var tmp = slide2; slide2 = slide1; slide1 = tmp; }
    
    var displayElement = parent.getElementsByClassName("rangeValues")[0];
        displayElement.innerHTML = slide1 + " - " + slide2;
  }
  
  window.onload = function(){
    // Initialize Sliders
    var sliderSections = document.getElementsByClassName("range-slider");
        for( var x = 0; x < sliderSections.length; x++){
          var sliders = sliderSections[x].getElementsByTagName("input");
          for( var y = 0; y < sliders.length; y++ ){
            if( sliders[y].type ==="range" ){
              sliders[y].oninput = getVals;
              // Manually trigger event first time to display values
              sliders[y].oninput();
            }
          }
        }
  }


function drawShape(x, y, r, sides) {
    // move the canvas to the center position
    const canvas = document.getElementsByClassName('canv')[0];
    const ctx = canvas.getContext('2d');
    ctx.translate(x, y);

    for (let i = 0; i < sides; i++) {
      // calculate the rotation
      const rotation = ((Math.PI * 2) / sides) * i;

      // for the first point move to
      if (i === 0) {
        ctx.moveTo(r * Math.cos(rotation), r * Math.sin(rotation));
      } else {
        // for the rest draw a line
        ctx.lineTo(r * Math.cos(rotation), r * Math.sin(rotation));
      }
    }
  
      // close path and stroke it
      ctx.closePath();
      ctx.stroke();
      // reset the translate position
      ctx.resetTransform();
    }
function getHue(){
  var slides = document.getElementsByClassName("slider");
  var slide1 = parseFloat(slides[0].value); // Use parseFloat to convert slider value to a number
  var slide2 = parseFloat(slides[1].value); // Use parseFloat to convert slider value to a number
  console.log(slide1 + " " + slide2);
  return (slide1 + slide2) / 2;
}

function removeShapes(slidernum){
  var shapes = document.getElementsByClassName("shapes");
  console.log(shapes);
  for(var i = slidernum*4; i < slidernum*4 + 4 ; i++){
    shapes[i].style.display = "none";
  }
}
function getSides(slidernum){
  var sliders = document.getElementsByClassName("shapeNumber");
  var shapes = document.getElementsByClassName("shapes");
  console.log(shapes.length);
  console.log(sliders.length);
  removeShapes(slidernum);
  switch(parseInt(sliders[slidernum].value)){
    case 3:
      shapes[0+slidernum*4].style.display = "block";
      shapes[0+slidernum*4].style.filter = "hue-rotate("+getHue()+"deg) brightness(100%)";
      break;
    case 4:
      shapes[1+slidernum*4].style.display = "block";
      shapes[1+slidernum*4].style.filter = "hue-rotate("+getHue()+"deg)";
      break;
    case 5:
      shapes[2+slidernum*4].style.display = "block";
      shapes[2+slidernum*4].style.filter = "hue-rotate("+getHue()+"deg)";
      break;
    case 6:
      shapes[3+slidernum*4].style.display = "block";
      shapes[3+slidernum*4].style.filter = "hue-rotate("+getHue()+"deg)";
      break;
    
  }
}