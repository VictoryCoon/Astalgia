const xhr = new XMLHttpRequest();

function ajax(method, url, data) {
    return new Promise((resolve, reject) => { // Promise 반환
        if (method === 'GET') {
            if(data.length != 0){
                url += `/${encodeURIComponent(data)}`;
            }
        }
        console.log(url);
        xhr.open(method, url, true);
        if (method === 'POST') {
            xhr.setRequestHeader('Content-type','application/json');
            xhr.send(JSON.stringify({data:data}));
        } else {
            xhr.send();
        }
        xhr.onload = () => {
            if (xhr.status === 200) {
                resolve(xhr.response);
            } else {
                reject(new Error(`HTTP error! status: ${xhr.status}`));
            }
        };
        xhr.onerror = () => {
            reject(new Error("Network error"));
        };
    });
}

/*
function ajax(method,url,data){
    if(method == 'GET'){
        url += `/${encodeURIComponent(data)}`;
    }
    xhr.open(method, url, true);
    if(method == 'POST'){
        xhr.setRequestHeader('Content-type', 'application/json');
        xhr.send(JSON.stringify({data: data}));
    }else{
        xhr.send();
    }
    xhr.onload = () => {
        if (xhr.status == 200) {
            console.log("Success");
            return xhr.response;
        } else {
            console.log("Failed");
            return false;
        }
    }
}*/