// It uses data_handler.js to visualize elements
import { dataHandler } from "./data_handler.js";

export let dom = {
    init: function () {
        // This function should run once, when the page is loaded.
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function(boards){
            dom.showBoards(boards);
        });
    },
    showBoards: function (boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also

        let currentBoard = null
        let boardList = '';

        for(let board of boards){
            boardList += `
                <details data-id="${board.id}" class="boardContent">
                    <summary><div class="item list" style="display: inline">${board.title}</div></summary>
                </details>`;
        }

        const outerHtml = `
            <div class="board-container data">
                ${boardList}
            </div>
        `;

        let boardsContainer = document.querySelector('#boards');
        boardsContainer.innerHTML = ''
        boardsContainer.insertAdjacentHTML("beforeend", outerHtml);


        document.querySelector(".board-container").addEventListener("click", (e) => {
            if (!e.target.classList.contains("item")){return}
            if (currentBoard){currentBoard.innerHTML = currentBoard.firstChild.value}
            currentBoard = e.target
            e.target.innerHTML = `<input class="renameBoard" value="${e.target.innerHTML}">`
            e.target.firstChild.onchange = (e) => {
                dataHandler.renameBoard(e.currentTarget.value, e.currentTarget.parentNode.dataset['id'], null)
                e.currentTarget.parentNode.innerHTML = e.currentTarget.value
                currentBoard = null
            };
        });

        let boardContents = document.querySelectorAll(".boardContent")
        boardContents.forEach(content => {
           content.addEventListener("toggle", (e) => {
                dataHandler.getCardsByBoardId(e.target.dataset.id, (id, content) => {
                    dom.loadCards(id, content)
                });
           });
        });
    },
    loadCards: function (boardId, content) {
        console.log(content, boardId)
    },
    showCards: function (cards) {
        // shows the cards of a board
        // it adds necessary event listeners also
    },
    // here comes more features
};
