import { dom } from "./dom.js";
import {dataHandler} from "./data_handler.js";

// This function is to initialize the application
function init() {
    // init data
    dom.init();
    // loads the boards to the screen
    dom.loadBoards();

    document.getElementById("saveBoard").addEventListener("click", () => {
        let newTitle = document.querySelector("#newBoard").value
        dataHandler.createNewBoard(newTitle, (data) => {
            dom.loadBoards();
        });
        document.querySelector("#addBoardDiv").classList.toggle("hidden");
    });

    function flashFlaskTimeout () {
        let message = document.querySelector('.alert');
        if (message) {
            setTimeout(function () {
            message.remove();
            }, 2000)
        }
    }

    flashFlaskTimeout();
}

init();
