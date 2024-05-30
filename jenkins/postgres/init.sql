CREATE ROLE gitea WITH ENCRYPTED PASSWORD 'gitea';
ALTER ROLE gitea WITH LOGIN;

CREATE DATABASE gitea;
GRANT ALL PRIVILEGES ON DATABASE gitea TO gitea;
\c gitea postgres
GRANT ALL ON SCHEMA public TO gitea;
