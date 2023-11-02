CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    idade INT,
    curso VARCHAR(255)
);

INSERT INTO alunos (nome, idade, curso) VALUES ('Guilherme', 21, 'Análise e Desenvolvimento de Sistemas');
INSERT INTO alunos (nome, idade, curso) VALUES ('Lariça', 24, 'Análise e Desenvolvimento de Sistemas');
INSERT INTO alunos (nome, idade, curso) VALUES ('Mozar', 23, 'Análise e Desenvolvimento de Sistemas');


CREATE TABLE IF NOT EXISTS professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    titulo VARCHAR(255),
    curso VARCHAR(255)
);

INSERT INTO professores (nome, titulo, curso) VALUES ('Ricardo', 'Coordenador e Professor', 'Análise e Desenvolvimento de Sistemas');
INSERT INTO professores (nome, titulo, curso) VALUES ('Lariça', 'Professor', 'Análise e Desenvolvimento de Sistemas');
INSERT INTO professores (nome, titulo, curso) VALUES ('Mozar', 'Professor', 'Análise e Desenvolvimento de Sistemas');
