CREATE TABLE m_election(
vote_id VARCHAR(20) NOT NULL PRIMARY KEY,
poll_title VARCHAR(50) NOT NULL,
poll_doc VARCHAR(255),
cand_num INTEGER NOT NULL,
create_date VARCHAR(14)
);

CREATE TABLE m_votes(
vote_id VARCHAR(20) NOT NULL,
cand_no SMALLINT NOT NULL,
cand_name VARCHAR(50) NOT NULL,
vote_num INTEGER,
image_path VARCHAR(255),
last_update VARCHAR(14),
create_date VARCHAR(14),
FOREIGN KEY (vote_id) references m_election(vote_id)
);
