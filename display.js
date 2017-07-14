// Width & Height
var w = 700;
var h = 500;
var barPadding = 3;
var color = ["#c2e5ec", "#ecc9c2", "#c2ecde", "#e5ecc2"];

d3.csv("static/data.csv", function(dataset) {
    dataset.forEach(function(d) {
        d.stars = +d.stars;
        console.log(dataset);
        });
    
    var svg = d3.select("td")
    .append("svg")
    .attr("width", w)
    .attr("height", h);
    
    // find max stars value to scale graph
    var max = d3.max(dataset, function(d) {
        return d.stars;
    });
    
    var scale = d3.scaleLinear()
        .domain([0, max])
        .range([0, h]);
    
    // bars
    svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("x", function(d, i) {
        return i * (w / dataset.length); 
    })
    .attr("y", function(d) {
        return h - scale(d.stars);
    })
    .attr("width", w / dataset.length - barPadding)
    .attr("height", function(d) {
        return d.stars;
    })
    .attr("fill", function(d, i) {
        return color[i % 4];
    });
        
    // bar labels
    svg.selectAll("text")
        .data(dataset)
        .enter()
        .append("text")
        .attr("fill", "black")
        .text(function (d) {
            return (d.langName + " - " + d.stars);
        })
        .attr("transform", function(d,i) {
        var xText = i * (w / dataset.length) + 18;
        var yText = h - 15;
        return "translate(" + xText + "," + yText + "), rotate(-90)";
      });
});
