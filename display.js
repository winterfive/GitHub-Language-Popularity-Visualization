// Width & Height
var w = 700;
var h = 500;
var barPadding = 3;
   
d3.csv("static/data.csv", function(dataset) {
    
    var svg = d3.select("td")
    .append("svg")
    .attr("width", w)
    .attr("height", h);
    
    svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("x", function(d, i) {
        return i * (w / dataset.length); 
    })
    .attr("y",  function(d) {
        return h - d.stars;
    })
    .attr("width", w / dataset.length - barPadding)
    .attr("height", function(d) {
        return d.stars;
    })
    .attr("fill", "#e9e2da");
        
    svg.selectAll("text")
        .data(dataset)
        .enter()
        .append("text")
        .attr("fill", "black")
        .text(function (d) {
            return d.langName;
        })
        .attr("transform", function(d,i) {
        var xText = i * (w / dataset.length) + 20;
        // var yText = h - yScale(d.v);
        var yText = h - 15;
        return "translate(" + xText + "," + yText + "), rotate(-90)";
      });
});
