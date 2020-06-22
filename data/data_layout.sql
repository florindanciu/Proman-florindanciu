DROP TABLE IF EXISTS users, cards, board_statuses, statuses, boards;

CREATE TABLE boards (
    id serial primary key,
    title text NOT NULL
);

CREATE TABLE statuses (
    id serial primary key,
    title text NOT NULL
);

CREATE TABLE board_statuses (
    board_id integer NOT NULL,
    status_id integer NOT NULL,
    FOREIGN KEY (board_id) REFERENCES boards (id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses (id) ON DELETE CASCADE,
    PRIMARY KEY (board_id, status_id)
);

CREATE TABLE cards (
    id serial primary key,
    board_id integer,
    title varchar,
    status_id integer,
    cards_order integer,
    archived boolean DEFAULT(false),
    FOREIGN KEY (board_id, status_id) REFERENCES board_statuses (board_id, status_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE users (
    id serial primary key,
    username varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    password varchar(150) NOT NULL
);

INSERT INTO boards(title) VALUES ('board_1'), ('board_2');

INSERT INTO statuses(title) VALUES ('new'),('in progress'), ('testing'), ('done');

INSERT INTO board_statuses
    VALUES (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4);

INSERT INTO cards(board_id, title, status_id, cards_order)
    VALUES
    (1,'new card 1',1,0),
    (1,'new card 2',1,1),
    (1,'in progress card',2,0),
    (1,'planning',3,0),
    (1,'done card 1',4,0),
    (1,'done card 1',4,1),
    (2,'new card 1',1,0),
    (2,'new card 2',1,1),
    (2,'in progress card',2,0),
    (2,'planning',3,0),
    (2,'done card 1',4,0),
    (2,'done card 1',4,1);

-- ALTER SEQUENCE cards_id_seq RESTART WITH 1;
-- UPDATE cards SET id=nextval('cards_id_seq');
