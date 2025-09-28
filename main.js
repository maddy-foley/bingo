import PDFDocument from 'pdfkit';
import fs from 'fs';

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

const data = readJsonFile('test.json');
console.log(data)
doc.table({
  rowStyles: (i) => {
    if (i % 2 === 0) return { backgroundColor: "#ccc" };
  },
  data: data,
})
doc.end();