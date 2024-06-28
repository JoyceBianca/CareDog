document.addEventListener("DOMContentloaded", function() {
    document.getElementById("loginPagina").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/loginRota", true);
        console.log("Java Script")
        xhr.onreadystatechange = function () {
            if(xhr.readyState == 4 && xhr.status == 200) {
                var data = JSON.parse(xhr.responseText);
                document.getElementById("result").textContent = data.message;
            }
        };
        xhr.send();
    });
});