document.addEventListener("DOMContentloaded", function() {
    document.getElementById("loginButton").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/loginRota", true);
        xhr.onreadystatechange = function () {
            if(xhr.readyState == 4 && xhr.status == 200) {
                var data = JSON.parse(xhr.responseText);
                document.getElementById("result").textContent = data.message;
            }
        };
        xhr.send();
    });
});