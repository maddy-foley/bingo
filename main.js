let bingo = {
    "B": 1,
    "I": 16,
    "N": 31,
    "G": 46,
    "O": 61
}


let j = -1

let myString = ""
for(let i = 0 ; i <15 ; i++){
    for(let key in bingo){
        process.stdout.write(key + " "+ (bingo[key] + i)+ " " )
    }
    process.stdout.write("\n");
}   
