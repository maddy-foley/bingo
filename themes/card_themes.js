
// cmyk as an array is used to build color styling with pdfkit.
const myCMYKColors = {
    mauve: [12,31,0,10],
    yellow: [1,13,95,0],
    tangerine: [0,50,80,0],
    orange: [0,60,100,0],
    limeGreen: [30,4,80,0],
    darkViolet: [80,100,0,50]
}

const myPalettes = {
    test: {
        columns: [myCMYKColors.mauve,myCMYKColors.yellow,myCMYKColors.tangerine,myCMYKColors.orange,myCMYKColors.limeGreen],
        textColor: myCMYKColors.darkViolet,
        
    }
}

export default myPalettes;