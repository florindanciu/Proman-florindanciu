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

        for (let board of boards) {
            boardList += `
                <details id='board-${board.id}' data-id="${board.id}" class="boardContent">
                    <summary>
                        <div class="item list" style="display: inline">${board.title}</div>
                        <div class='add-status-btn'><input type="button" value="new"></div>
                    </summary>
                    <div class='container'></div>
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
                if (e.target.open) {
                    dataHandler.getCardsByBoardId(e.target.dataset.id, (id, content) => {
                        dom.loadCards(id, content)    
                    });
                }
           });
        });

        document.querySelectorAll('.add-status-btn').forEach((btn) => {
            btn.addEventListener('click', (e) => {
                let parent = e.target.parentNode.parentNode.parentNode;
                dataHandler.createNewStatus(parent.dataset.id, dom.loadBoards);
            });
        });
    },
    loadCards: function (boardId, content) {
        let cardContainer = document.querySelector('#board-' + boardId).lastElementChild;
        let statuses = content.statuses;

        let boardContent = `<div class='row'>`;
        let cardContent = `<div class='row'>`;
        for (let status of statuses) {
            boardContent += `
            <div class='col-sm'>
                <div class='status-title' data-col='${status.id}'>${status.title}</div>
                <div class='add-card-btn' data-board='${status.board_id}' data-col='${status.id}'><input type="button" value="new"></div>
            </div>
            `
            cardContent += `
            <div class='col-sm'>
            <div id='c${boardId}-${status.id}' class='card-container' data-col='${status.id}'></div>
            </div>
            `
        }
        boardContent += `</div>`;
        cardContent += `</div>`;
        
        cardContainer.innerHTML = boardContent;
        cardContainer.innerHTML += cardContent;
        
        
        
        let containers = {};
        for (let status of statuses) {
            containers[status.id] = document.querySelector('#c' + boardId + '-' + status.id);
        }
        for (let card of content.cards) {
            let cardHTML = `
            <div id='card-${card.id}' class='card' data-board='${card.board_id}' draggable='true'>
                <div class='card-title' data-id='${card.id}'>${card.title}</div>
            </div>
            `
            containers[card.status_id].innerHTML += cardHTML;
        }
            
        function allowDrop(event) {
            let card = document.getElementById(event.dataTransfer.getData('card'))
            if (card.dataset.board == event.currentTarget.id.slice(1, event.currentTarget.id.indexOf('-'))) {
                event.preventDefault();
            }
        }
        function drop(event) {
            let card = event.dataTransfer.getData('card');
            card = document.getElementById(card);
            event.currentTarget.appendChild(card);
            event.preventDefault();
            dataHandler.moveCard(card.id.slice(5), event.currentTarget.dataset['col'], () => {});
        }
        function drag(event) {
            event.dataTransfer.setData('card', event.currentTarget.id);
        }
        
        for (let i in containers) {
            containers[i].addEventListener('dragover', allowDrop);
            containers[i].addEventListener('drop', drop);
        }
        document.querySelectorAll('.card').forEach((card) => {
            card.addEventListener('dragstart', drag);
        });


        let currentTitle;

        document.querySelectorAll('.status-title').forEach((status) => {
            status.addEventListener('click', (e) => {
                if(currentTitle && currentTitle != e.currentTarget) { currentTitle.innerHTML = currentTitle.firstChild.value; }
                currentTitle = e.currentTarget;
                e.target.innerHTML = `<input type='text' class="renameStatus" value="${e.target.innerHTML}">`
                e.target.firstChild.addEventListener('change', (e) => {
                    dataHandler.renameStatus(e.target.parentNode.dataset.col, e.target.value, () => {});
                    e.target.parentNode.innerHTML = e.target.value;
                    currentTitle = null;
                });
            });
        });

        document.querySelectorAll('.add-card-btn').forEach((btn) => {
            btn.addEventListener('click', (e) => {
                dataHandler.createNewCard(e.target.parentNode.dataset.board, e.target.parentNode.dataset.col, dom.loadBoards);
            });
        });

        let currentCard;

        document.querySelectorAll('.card-title').forEach((card) => {
            card.addEventListener('click', (e) => {
                if(currentCard && currentCard != e.currentTarget) { currentCard.innerHTML = currentCard.firstChild.value; }
                currentCard = e.currentTarget;
                e.target.innerHTML = `<input type='text' class="renameCard" value="${e.target.innerHTML}">`
                e.target.firstChild.addEventListener('change', (e) => {
                    dataHandler.renameCard(e.target.parentNode.dataset.id, e.target.value, () => {});
                    e.target.parentNode.innerHTML = e.target.value;
                    currentCard = null;
                });
            });
        });
    }
    
    // here comes more features
};
