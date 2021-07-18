var listaBare = [];
var obiecteBara = {};

class Bara {
    constructor(otel, diam, pas, lung, lungBuc, tip){
        this.otel = otel;
        this.diam = diam;
        this.pas = pas;
        this.lung = lung;
        this.lungBuc = lungBuc;
        this.tip = tip;
        this.nrBuc = this.lungBuc / this.pas;
    }

    calcBucati(){
        return this.nrBuc = this.lungBuc / this.pas;
    }

}

function getInfo() {
    var diam = document.getElementsByClassName('diam')[0].value;
    var pas = document.getElementsByClassName('pas')[0].value;
    var lung = document.getElementsByClassName('lungime')[0].value;
    var lungBuc = document.getElementsByClassName('lungimeBucati')[0].value;
    console.log(diam)
    console.log(lungBuc);
    var buc = lungBuc / pas;
    console.log(buc);
    listaBare.push([diam,lung]);
    console.log(listaBare);
}

//function to test various smaller elements
function tester() {
    var tabel = document.getElementsByClassName("tabelRezultate")[0];
    console.log(tabel.rows.length);
}



//function for html button, adds together all other functions
function clicker(){
    //checkBars(addToDB());
    var tabel = document.getElementsByClassName("tabelRezultate")[0];
    var nrRows = tabel.rows.length;

    displayBara(checkBars(addToDB()));



}

//creates new object with info from html
function addToDB () {
    var otel = document.getElementsByClassName('otel')[0].value;
    var diam = document.getElementsByClassName('diam')[0].value;
    var pas = document.getElementsByClassName('pas')[0].value;
    var lung = document.getElementsByClassName('lungime')[0].value;
    var lungBuc = document.getElementsByClassName('lungimeBucati')[0].value;
    var bara = new Bara(otel, diam, pas, lung, lungBuc, "bara");
    return bara;
}

// check if object exists in dictionary, add to dict if it doesn't, change nr of pcs if it does
function checkBars(bara){
    
    if (Object.keys(obiecteBara).length === 0){
        obiecteBara[Object.keys(obiecteBara).length + 1] = bara;
    } else {
        for (const [key, value] of Object.entries(obiecteBara)){
            if (value.otel === bara.otel && value.diam === bara.diam && value.lung === bara.lung && value.tip === bara.tip) {
                var selectedKey = key;
            }
        }
        if (selectedKey === undefined){
                obiecteBara[Object.keys(obiecteBara).length + 1] = bara;                        
        } else{
            obiecteBara[selectedKey].nrBuc = obiecteBara[selectedKey].nrBuc + bara.nrBuc;
        }    
    }
    return obiecteBara;
}


//create new row in table and display new object or change nr buc of existing object
function displayBara(obiecteBara){
    var tabel = document.getElementsByClassName("tabelRezultate")[0];
    
    if (tabel.rows.length === Object.keys(obiecteBara).length){
        var row = tabel.insertRow(parseInt(Object.keys(obiecteBara).length));
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        cell1.innerHTML = Object.keys(obiecteBara).length;
        cell1.classList.add("Marca_" + Object.keys(obiecteBara).length);
        cell2.innerHTML = obiecteBara[Object.keys(obiecteBara).length].tip;
        cell3.innerHTML = obiecteBara[Object.keys(obiecteBara).length].diam;
        cell4.innerHTML = obiecteBara[Object.keys(obiecteBara).length].lung;
        cell5.innerHTML = obiecteBara[Object.keys(obiecteBara).length].nrBuc;
        cell5.classList.add("nrBuc_" + Object.keys(obiecteBara).length);

    } else {
        for (const [key, value] of Object.entries(obiecteBara)){
            var cellUpdate = document.getElementsByClassName("nrBuc_" + key)[0];
            cellUpdate.innerHTML = value.nrBuc;

        }
    }
}