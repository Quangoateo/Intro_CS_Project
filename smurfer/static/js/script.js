// fetch data from server
async function fetchData() {
    url = "/loadData";
    const tableBody = document.getElementById("loadTableBody");
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    // if table already has elements from last call, deletes all
    tableBody.innerHTML ='';
    // create new rows of table
    for (const row of data) 
    {
        const rowElement = document.createElement("tr");
        const innerText = '<td>' + row['id'] + '</td><td>' + row['name'] + '</td><td>' + row['intake'] + '</td><td>' + row['date'] + '</td><td>';
        rowElement.innerHTML = innerText;
        tableBody.appendChild(rowElement);  
    }
}
// call the function every 1 second= 1k milliseconds    
setInterval(fetchData, 1000)


