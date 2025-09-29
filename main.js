import PDFDocument from 'pdfkit';
import fs from 'fs';
import { json } from 'stream/consumers';

function readJsonFile(filePath) {
    try {
        const data = fs.readFileSync(filePath, 'utf8');
        const jsonData = JSON.parse(data);
        return jsonData
    } catch (error) {
        console.error('Error reading or parsing JSON:', error);
    }
}



const doc = new PDFDocument({size: 'A3'});
doc.pipe(fs.createWriteStream('test.pdf'));

doc.fontSize(14);
const jsonData = readJsonFile('test.json');
const bingoSentenceData = readJsonFile('lorem_ipsum.json');
const myBingoCells = [["B","I","N","G","O"]]


// replace bingo numbers for sentences
for(let item of jsonData){
    let temp = []
    for(let ele of item){
        temp.push(bingoSentenceData[ele] ? bingoSentenceData[ele] : "Free")
    }
    myBingoCells.push(temp)
}

const tableData = myBingoCells


const cardSize = 25;

// CYMK color pallette arrays
const brightOrange = [0,72,100,0];
const yellow = [0,34,97,0];
const beige = [1,11,12,0];
const lightBlue = [71,10,0,0];
const purple = [20,40,0,0];
const slate = [90,77,62,95];

//left to right column
const column_color_order =[brightOrange,yellow,beige,lightBlue,purple]

doc.table({
    defaultStyle:{font: 'Times-Roman', align: 'center', textColor: slate, borderColor: slate
    },   
    columnStyles: (i) => {
        return {backgroundColor: column_color_order[i]};
    },
    rowStyles: (i) => {
        if (i === 0) return {font: 'Times-Bold', backgroundColor: beige};
    },

   data: tableData,
});


doc.end();