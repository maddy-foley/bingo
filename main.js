import PDFDocument from 'pdfkit';
import fs from 'fs';
import { json } from 'stream/consumers';
import myPalettes from './themes/card_themes.js';

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
const jsonData = readJsonFile('data/test.json');
const bingoSentenceData = readJsonFile('data/lorem_ipsum.json');
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



doc.table({
    defaultStyle:{font: 'Times-Roman', align: 'center', textColor: myPalettes.test.textColor,rowStyles: {minHeight: 100}},   
    columnStyles: (i) => {
        // doc.roundedRect(i*100, i*100, 100, 100, .3);
        return {backgroundColor: myPalettes.test.columns[i]};
    },
    rowStyles: (i) => {
        if (i === 0) return {font: 'Times-Bold'};
    },

   data: tableData,
});

doc.stroke();
doc.end();