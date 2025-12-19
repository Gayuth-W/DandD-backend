function testGS(){
  const url="https://script.google.com/macros/s/AKfycbxiWDBX4EIhuMg30YVPq_rp37eM-U5Ok8DcpqdczY3ixGpEYo7N1pul2c0LI0KXrfYoZg/exec"

  fetch(url) 
    .then(d=>d.json())
    .then(d=>{
      document.getElementById("app").textContent=d[0].status;
    });

}


function addGS(){
  const url="https://script.google.com/macros/s/AKfycbxJQY-ie3AeqwFW7RMWftFhIHGf5jysfND9XAzVpDYzRV0XORiWXvE9C89H8iQk50cDKw/exec"

  fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'no-cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'omit', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    // referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify({name:"olivia"}) // body data type must match "Content-Type" header
  }); 

}

document.getElementById("btn2").addEventListener("click", addGS);

document.getElementById("btn").addEventListener("click", testGS);