function doPost(e){

  const ss=SpreadsheetApp.getActiveSpreadsheet();
  const ws =ss.getSheetByName("Sheet3");

  const headers=ws.getRange(1, 1, 1, ws.getLastColumn()).getValues()[0];
  const headersCopy=headers.slice();
  headersCopy.shift();
  headers.shift();//This is going to remove the ID column which is the first column
  headers.sort();

  const body=e.postData.contents;
  const bodyJSON=JSON.parse(body);
  const headersPassed=Object.keys(bodyJSON).sort();

  let jsonResponse={status:200, message:"Posted successfully"};

  if(!compare_(headers, headersPassed)){
    jsonResponse={status:500, message:"Something went wrong..."};
    return ContentService
      .createTextOutput(JSON.stringify(jsonResponse))
      .setMimeType(ContentService.MimeType.JSON); 
  }
  
  const ids=ws.getRange(2, 1, ws.getLastRow(), 1).getValues();
  const aod=headersCopy.map(h=>bodyJSON[h]);
  let newID=getMax_(ids)+1;

  aod.unshift(newID);

  ws.appendRow(aod);
  
  return ContentService
    .createTextOutput(JSON.stringify(jsonResponse))
    .setMimeType(ContentService.MimeType.JSON);  
}


function doGet(){
  const ss =SpreadsheetApp.getActiveSpreadsheet();
  const ws =ss.getSheetByName("Sheet3");
  const data=ws.getRange("A1").getDataRegion().getValues();
  const headers=data.shift();

  const jsonArray=data.map(r=>{
    let obj={};
    headers.forEach((h, i)=>{
      obj[h]=r[i]
    });
    return obj
  });

  const response = [{status:200, data: jsonArray}]

  return ContentService
    .createTextOutput(JSON.stringify(response))
    .setMimeType(ContentService.MimeType.JSON);
}

function compare_(arr1, arr2){
  if(arr1.length!==arr2.length) return false;

  for(let i=0; i<arr1.length;++i){
    if(arr1[i]!==arr2[i]) return false;
  }

  return true;
}

function getMax_(arr){
  let max=0;
  arr.forEach(r =>{
    if(r[0]>max) max=r[0];
  });

  return max;
}