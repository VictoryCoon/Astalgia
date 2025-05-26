function ajax(method, url, data) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        if (method === 'GET') {
            if(data.length != 0){
                url += `/${encodeURIComponent(data)}`;
            }
        }
        document.getElementById("curtain").style.display = "flex";
        xhr.open(method, "/"+url, true);
        if (method === 'POST') {
            xhr.setRequestHeader('Content-type','application/json');
            xhr.send(JSON.stringify({data:data}));
        } else {
            xhr.send();
        }
        xhr.onload = () => {
            if (xhr.status === 200) {
                resolve(xhr.response);
                document.getElementById("curtain").style.display = "none";
            } else {
                reject(new Error(`HTTP error! status: ${xhr.status}`));
                document.getElementById("curtain").style.display = "none";
            }
        };
        xhr.onerror = () => {
            reject(new Error("Network error"));
            document.getElementById("curtain").style.display = "none";
        };
    });
}