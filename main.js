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



const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('test.pdf'));

const json_data = readJsonFile('test.json');
const bingo_sentence_data = readJsonFile('lorem_ipsum.json');
const my_bingo_cells = [["B","I","N","G","O"]]


// replace bingo numbers for sentences
for(let item of json_data){
    let temp = []
    for(let ele of item){
        temp.push(bingo_sentence_data[ele] ? bingo_sentence_data[ele] : "Free")
    }
    my_bingo_cells.push(temp)
}

const table_data = my_bingo_cells


const card_size = 25;


doc.table({
    defaultStyle:{font: 'Times-Roman', align: 'center'},
    rowStyles: (i) => {
    return i < 1 ? { border: [0, 0, 1, 0], font:"Times-Bold" } : { border: false };
  },
   data: table_data,
});


doc.end();