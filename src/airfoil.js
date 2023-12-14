import { Matrix } from 'ml-matrix';
import * as fs from 'fs';
console.log("Hello Airfoil!");

var showPrints = true;

function prt(msg) {
    if (showPrints)
        console.log(msg);
}

function arr2Mat(arr){
    
}

// ==================================================


var Vinf = 1;
var AoA = 5;

// Get Airfoil Coordinates
let fsRead = fs.readFileSync('NACA0012.csv', "utf8");
let airfoilData = d3.csvParse(fsRead);

var XB = airfoilData.map(function (d) { return d.x });
var YB = airfoilData.map(function (d) { return d.y });

XB.reverse();
YB.reverse();

prt(XB);
prt(YB);

var numPts = XB.length;
var numPan = numPts - 1;

prt(numPts);
prt(numPan);

var XC = Matrix.zeros(numPan, 1);
var YC = Matrix.zeros(numPan, 1);

var S = Matrix.zeros(numPan, 1);

var phiD = Matrix.zeros(numPan, 1);

for(var i = 0; i < numPan; i++){
    XC.set(i,1, 0.5*(XB.get(i,1)+XB.get(i+1,1)));
}