// this object contains the functions which handle the data and its reading/writing
// feel free to extend and change to fit your needs

// (watch out: when you would like to use a property/function of an object from the
// object itself then you must use the 'this' keyword before. For example: 'this._data' below)
export let dataHandler = {
    _data: {}, // it is a "cache for all data received: boards, cards and statuses. It is not accessed from outside.
    _api_get: function (url, callback) {
        // it is not called from outside
        // loads data from API, parses it and calls the callback with it

        fetch(url, {
            method: 'GET',
            credentials: 'same-origin'
        })
        .then(response => response.json())  // parse the response as JSON
        .then(json_response => callback(json_response));  // Call the `callback` with the returned object
    },
    _api_post: function (url, data, callback) {
        fetch(url, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => callback(response));
    },
    init: function () {
    },
    getBoards: function (callback) {
        // the boards are retrieved and then the callback function is called with the boards

        // Here we use an arrow function to keep the value of 'this' on dataHandler.
        //    if we would use function(){...} here, the value of 'this' would change.
        this._api_get('/get-boards', (response) => {
            this._data['boards'] = response;
            callback(response);
        });
    },
    getBoard: function (boardId, callback) {
        // the board is retrieved and then the callback function is called with the board
    },
    getStatuses: function (callback) {
        // the statuses are retrieved and then the callback function is called with the statuses
    },
    getStatus: function (statusId, callback) {
        // the status is retrieved and then the callback function is called with the status
    },
    getCardsByBoardId: function (boardId, callback) {
        this._api_get('/get-cards/' + boardId, (response) => {
            this._data['cards' + boardId] = response;
            callback(boardId, response);
        });
    },
    getCard: function (cardId, callback) {
        // the card is retrieved and then the callback function is called with the card
    },
    createNewBoard: function (boardTitle, callback) {
        this._api_post('/add_board', {'title': boardTitle}, (response) => {
            callback(response);
        });
    },
    renameBoard: function (boardTitle, boardId, callback) {
        this._api_post('/rename_board', {'title': boardTitle, 'id': boardId}, callback);
    },
    createNewCard: function (boardId, statusId, callback) {
        console.log(boardId + '--' + statusId)
        this._api_post('/add-card', {'boardId': boardId, 'statusId': statusId}, callback);
    },
    moveCard: function (cardId, statusId, callback) {
        this._api_post('/move-card', {'cardId': cardId, 'statusId': statusId}, callback);
    },
    renameCard: function(cardId, title, callback) {

    },
    renameStatus: function (statusId, title, callback) {
        this._api_post('/rename-status', {'statusId': statusId, 'title': title}, callback);
    },
    createNewStatus: function (boardId, callback) {
        this._api_post('/add-status', {'boardId': boardId}, callback);
    }
    // here comes more features
};
