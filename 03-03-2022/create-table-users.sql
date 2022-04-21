DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id     TEXT UNIQUE NOT NULL,
    user_name   TEXT NOT NULL,
    user_email  TEXT UNIQUE NOT NULL,
    age         TEXT NOT NULL,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;
