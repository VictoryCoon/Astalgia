const xhr = new XMLHttpRequest() //객체 인스턴스 생성

function ajax(method,url,data){
    xhr.open(method, url, true);
    if(method == 'POST'){
        xhr.setRequestHeader('Content-type', 'application/json');
        xhr.send("data="+data);
    }else{
        xhr.send();
    }
    xhr.onload = () => {
        if (xhr.status == 200) {
            console.log(xhr.response);
            console.log("통신 성공");
        } else {
            console.log("통신 실패");
        }
    }
}