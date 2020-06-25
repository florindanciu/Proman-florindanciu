import { dom } from "./dom.js";
import {dataHandler} from "./data_handler.js";

// This function is to initialize the application
function init() {
    // init data
    dom.init();
    // loads the boards to the screen
    dom.loadBoards();

    document.getElementById("newBoardBtn").addEventListener("click", () => {
        document.querySelector("#addBoardDiv").classList.toggle("hidden")
    });

    document.getElementById("saveBoard").addEventListener("click", () => {
        let newTitle = document.querySelector("#newBoard").value
        dataHandler.createNewBoard(newTitle, (data) => {
            dom.loadBoards();
        });
        document.querySelector("#addBoardDiv").classList.toggle("hidden");
    });
}

init();
