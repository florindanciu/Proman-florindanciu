// import { dom } from "./dom.js";
window.addEventListener('DOMContentLoaded', (event) => {

    const newBoardBtn = document.querySelector("#newBoardBtn")
    console.log(newBoardBtn)
    let boardsDiv = document.getElementById("boards")

    // This function is to initialize the application
    // function init() {
    //     // init data
    //     dom.init();
    //     // loads the boards to the screen
    //     dom.loadBoards();
    //
    // }

    getData('/get-boards')

    newBoardBtn.addEventListener("click", () => {
        let title = `<input placeholder="Board title" id="boardTitle">`
        let save = `<button id="save">Save</button>`
        document.body.innerHTML += `<div id="addBoardForm">${title} ${save}</div>`

        document.getElementById("save").addEventListener("click", () => {
            postData('/add_board', {'title': document.getElementById("boardTitle").value});
            setTimeout(function(){ getData('/get-boards') }, 1000);
        });
    });


    function getData(url){
        let lst = document.querySelector(".list")
        let content = ''
        fetch(url)
                .then((response) => response.json())
                .then((data) => {
                    data.forEach((item) => {
                        content += `<li>${item.title}</li>`
                    })
                    lst.innerHTML = content
                });
    };


    async function postData(url = '', data = {}) {
        const response = await fetch(url, {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
              'Content-Type': 'application/json'
            },
            redirect: 'follow',
            referrerPolicy: 'no-referrer',
            body: JSON.stringify(data)
        });
        return response.json();
    };

    // init();

});