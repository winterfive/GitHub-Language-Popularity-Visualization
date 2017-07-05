'''TODO'''

//Width and height
var w = 700;
var h = 300;

// var dataset = [];

// Convert csv to d3 dataset
d3.csv("data.csv", function(data) {
  console.log(data[0]);
});

dataset = "data.csv";

//Create SVG element
var svg = d3.select("plot")
			.append("svg")
			.attr("width", w)
			.attr("height", h);

svg.selectAll("circle")
   .data(dataset)
   .enter()
   .append("circle")
   .attr("cx", function(d) {
		return d.x;
   })
   .attr("cy", function(d) {
	   return d.y;
   })
   .attr("r", function(d) {
	   return d.r;
   });
